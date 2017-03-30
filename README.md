Password Stretcher
==================

Derive high-entropy passwords from passphrases using a slow key derivation function (sometimes referred to as [key stretching](https://en.wikipedia.org/wiki/Key_stretching)).

Why?
----

Password stretching makes it significantly harder to guess the password for a hash/file encryption key/etc. since an attacker has to use more resources or wait longer for each password they try.

Many programs that use passwords for securing sensitive information do not have particularly complex password stretching/key derivation algorithms (e.g. GPG), which make them vulnerable to password cracking, unless a particularly long and complex passphrase is used.

`stretch-pass` allows you to generate long, high-entropy passwords from a passphrase using a slow key derivation function, which can then be used in these programs.

Setup
=====

`$ pip3 install -r requirements.txt`

Usage
=====

```
$ stretch-pass -h
usage: stretch-pass [-h] [-v] [-V] [--log-file LOG_FILE]
                    [--config CONFIG_PATH] [-t TIME_COST] [-m MEMORY_COST]
                    [-p PARALLELISM] [-l PASSWORD_LENGTH] [-s SALT]
                    [-u USERNAME] [-c]
                    [--passphrase PASSPHRASE | --stdin-passphrase | -C]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  -V, --version         Show version and exit
  --log-file LOG_FILE   Path to log file (use with --verbose)
  --config CONFIG_PATH  Path to config file (defaults to ~/.stretchpassrc)
  -t TIME_COST, --time-cost TIME_COST
  -m MEMORY_COST, --memory-cost MEMORY_COST
  -p PARALLELISM, --parallelism PARALLELISM
  -l PASSWORD_LENGTH, --password-length PASSWORD_LENGTH
  -s SALT, --salt SALT  The hex string to use as a salt (at least 8 bytes)
  -u USERNAME, --username USERNAME
                        Username/program name (case sensitive - used to
                        generate the password)
  -c, --clip            Copy the password to clipboard instead of STDOUT
  --passphrase PASSPHRASE
                        Pass passphrase directly instead of via prompt
  --stdin-passphrase    Read passphrase from STDIN (be aware of newline
                        characters and environment encodings)
  -C, --confirm         Prompt for the passphrase twice and verify they are
                        the same
```
