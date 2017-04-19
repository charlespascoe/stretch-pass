from stretch_pass import consts
from stretch_pass import log
import re
import os
import sys
import stat


class Config:
    def __init__(self, path, opts={}, args={}):
        self.path = path

        self.time_cost = self.parse_option(opts, args, 'TIME_COST', consts.DEFAULT_TIME_COST, int, lambda val: 0 < val and val <= 2**16)
        self.parallelism = self.parse_option(opts, args, 'PARALLELISM', consts.DEFAULT_PARALLELISM, int, lambda val: 0 < val and val <= 64)
        self.memory_cost = self.parse_option(opts, args, 'MEMORY_COST', consts.DEFAULT_MEMORY_COST, int, lambda val: 8 * self.parallelism <= val and val <= 2**32)
        self.password_length = self.parse_option(opts, args, 'PASSWORD_LENGTH', consts.DEFAULT_PASSWORD_LENGTH, int, lambda val: 0 < val and val <= 2**16)
        self.salt = self.parse_option(opts, args, 'SALT', None, bytes.fromhex, lambda val: len(val) >= 8, 'SALT must be at least 8 bytes')

        for key in opts:
            log.info(self, 'Unknown option in config: {}'.format(key))

        log.debug(self, 'Loaded config (with defaults):')
        log.debug(self, self)

    def parse_option(self, opts, args, key, default, parse=None, validate=None, validation_message=None):
        val = None
        from_args = False

        if key in opts:
            val = opts[key]

            del opts[key]

        if key in args and vars(args)[key] is not None:
            val = vars(args)[key]
            from_args = True

        if val is None:
            return default

        if parse is not None:
            try:
                val = parse(val)
            except Exception:
                log.info(self, 'Invalid {} value: "{}", defaulting to {}'.format(key, val, default))
                return default

        if validate is not None and not validate(val):
            msg = 'Invalid {} value: "{}", defaulting to {}'.format(key, val, default)

            if validation_message is not None:
                msg = validation_message

            if from_args:
                log.msg(msg)
            else:
                log.info(self, msg)

            return default

        return val

    @staticmethod
    def load(args):
        path = os.path.abspath(os.path.expanduser(args.config_path))

        if not os.path.isfile(path):
            log.msg('===== BEGIN IMPORTANT MESSAGE =====')
            log.msg('A new config file is being created at {}'.format(path))
            log.msg('It will contain the salt used for deriving passwords.')
            log.msg('It is VERY important that you do not lose/delete this file,')
            log.msg('otherwise you will not be able to generate the passwords again.')
            log.msg('Feel free to back up this file to a safe location.')
            log.msg('===== END IMPORTANT MESSAGE =====')
            Config.create_default(path)

        log.info('Config', 'Attempting to load config from {}'.format(path))

        with open(path, 'r') as f:
            lines = f.readlines()

        opts = {}

        for line in lines:
            if len(line.strip()) > 0 and not line.startswith('#'):
                match = re.search('([A-Z_]+)\\s*=(.*)', line)

                if match is None:
                    log.info('Config', 'Could not parse config entry: "{}"'.format(line))
                else:
                    opts[match.group(1)] = match.group(2).strip()

        return Config(path, opts, args)

    @staticmethod
    def create_default(path):
        with open(path, 'w') as f:
            f.write('SALT=' + Config.new_salt().hex())
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)

    @staticmethod
    def new_salt():
        log.debug('Config', 'Generating new salt')
        salt = os.urandom(consts.SALT_LENGTH)
        log.debug('Config', 'Generated new salt: {}'.format(log.format_bytes(salt)))
        return salt

    def params(self):
        return (
            '    time_cost:       {}\n'.format(self.time_cost) +
            '    memory_cost:     {}\n'.format(self.memory_cost) +
            '    parallelism:     {}\n'.format(self.parallelism) +
            '    password_length: {}'.format(self.password_length)
        )

    def __str__(self):
        return (
            self.params() + '\n' +
            '    salt:            {}'.format('<None>' if self.salt is None else log.format_bytes(self.salt))
        )
