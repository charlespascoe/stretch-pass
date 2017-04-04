#!/usr/bin/env python3
import argparse
import log
import consts
import sys
import pyperclip
from config import Config
from password_deriver import PasswordDeriver
from getpass import getpass


VERSION = '0.1.1'


def get_passphrase(args):
    if args.passphrase is not None:
        return args.passphrase

    if args.stdin_passphrase:
        return sys.stdin.read()

    while True:
        passphrase = getpass('Enter passphrase: ')

        if args.confirm_passphrase:
            conf_passphrase = getpass('Confirm passphrase: ')

            if passphrase != conf_passphrase:
                log.msg('Passphrases do not match\n')
                continue

        return passphrase


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', action='count', default=0, dest='verbosity')
    parser.add_argument('-V', '--version', dest='version', help='Show version and exit', action='store_true')
    parser.add_argument('--log-file', type=str, dest='log_file', help='Path to log file (use with --verbose)')

    parser.add_argument(
        '--config',
        dest='config_path',
        help='Path to config file (defaults to {})'.format(consts.DEFAULT_CONFIG_FILE),
        default=consts.DEFAULT_CONFIG_FILE
    )

    parser.add_argument('-t', '--time-cost', dest='TIME_COST')
    parser.add_argument('-m', '--memory-cost', dest='MEMORY_COST')
    parser.add_argument('-p', '--parallelism', dest='PARALLELISM')
    parser.add_argument('-l', '--password-length', dest='PASSWORD_LENGTH')
    parser.add_argument('-s', '--salt', dest='SALT', help='The hex string to use as a salt (at least 8 bytes)')

    parser.add_argument('-u', '--username', dest='username', help='Username/program name (case sensitive - used to generate the password)')

    parser.add_argument('-c', '--clip', dest='copy_to_clipboard', action='store_true', help='Copy the password to clipboard instead of STDOUT')

    password_input_group = parser.add_mutually_exclusive_group()
    password_input_group.add_argument('--passphrase', dest='passphrase', help='Pass passphrase directly instead of via prompt')
    password_input_group.add_argument('--stdin-passphrase', dest='stdin_passphrase', action='store_true', help='Read passphrase from STDIN (be aware of newline characters and environment encodings)')
    password_input_group.add_argument('-C', '--confirm', dest='confirm_passphrase', action='store_true', help='Prompt for the passphrase twice and verify they are the same')

    args = parser.parse_args()

    if args.version:
        log.msg('stretch-pass v{}'.format(VERSION))
        sys.exit(0)

    log.level = args.verbosity
    log.info('stretch-pass', 'Verbosity level: {}'.format(args.verbosity))

    if args.log_file is not None:
        log.msg('Writing logs to: {}'.format(args.log_file))
        log.log_strm = open(args.log_file, 'w')

    config = Config.load(args)

    passDer = PasswordDeriver(config)

    password = passDer.compute_password(args.username, get_passphrase(args))

    if args.copy_to_clipboard:
        pyperclip.copy(password)
        log.msg('Password copied to clipboard')
    else:
        sys.stdout.write(password)
        if sys.stdout.isatty():
            sys.stdout.write('\n')

    sys.stdout.flush()
    sys.stdout.close()

    log.log_strm.flush()
    log.log_strm.close()

if __name__ == '__main__':
    main()
