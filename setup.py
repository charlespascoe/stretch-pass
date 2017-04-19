from distutils.core import setup
setup(
  name = 'stretch-pass',
  packages = ['stretch-pass'],
  version = '0.1.2-b',
  description = 'Derive high-entropy passwords from passphrases using a slow key derivation function (a.k.a. key stretching)',
  author = 'Charles Pascoe',
  author_email = 'charles@cpascoe.co.uk',
  url = 'https://github.com/cpascoe95/stretch-pass',
  download_url = 'https://github.com/cpascoe95/stretch-pass/archive/feature/pypi.tar.gz',
  keywords = ['password', 'passpharse', 'kdf', 'hash', 'stretch', 'stretching'],
  classifiers = [],
  entry_points={
    'console_scripts': [
        'stretch-pass = stretch-pass:main'
    ]
  }
)
