import argon2
import base64
from stretch_pass import log

class PasswordDeriver:
    def __init__(self, config):
        self.config = config

    def compute_password(self, username, passphrase):
        salt = bytes([])

        if self.config.salt is not None:
            salt = self.config.salt

        if username is not None:
            salt += username.encode('utf8')

        if len(salt) < 8:
            raise Exception('Salt too short')

        if isinstance(passphrase, str):
            passphrase = passphrase.encode('utf8')

        log.debug(self, 'Deriving bytes...')

        result = argon2.low_level.hash_secret_raw(
            secret = passphrase,
            salt = salt,
            time_cost = self.config.time_cost,
            memory_cost = self.config.memory_cost,
            parallelism = self.config.parallelism,
            hash_len = self.config.password_length,
            type = argon2.low_level.Type.I
        )

        log.debug(self, 'Derived bytes: {}'.format(log.format_bytes(result)))

        return base64.b64encode(result).decode('utf8')[:self.config.password_length]
