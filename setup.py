from distutils.core import setup
setup(
  name = 'stretch-pass',
  packages = ['stretch-pass'],
  version = '0.1.2-a',
  description = 'Derive high-entropy passwords from passphrases using a slow key derivation function (a.k.a. key stretching)',
  author = 'Charles Pascoe',
  author_email = 'charles@cpascoe.co.uk',
  url = 'https://github.com/cpascoe95/stretch-pass',
  download_url = 'https://github.com/cpascoe95/stretch-pass/archive/040ab11a7a36c12bfa70a7dac04be71bd08c3969.tar.gz',
  keywords = ['password', 'passpharse', 'kdf', 'hash', 'stretch', 'stretching'],
  classifiers = [],
)
