#!/usr/bin/env python3
import argparse
import log
import consts
from config import Config


VERSION = '0.0.0'


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', action='count', default=0, dest='verbosity')
    parser.add_argument('-V', '--version', dest='version', help='Show version and exit', action='store_true')
    parser.add_argument('--log-file', type=str, dest='log_file', help='Path to log file (use with --verbose)')

    parser.add_argument(
        '-C',
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

if __name__ == '__main__':
    main()
