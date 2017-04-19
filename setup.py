from setuptools import setup
setup(
  name = 'stretch-pass',
  packages = ['stretch_pass'],
  version = '0.1.3',
  description = 'Derive high-entropy passwords from passphrases using a slow key derivation function (a.k.a. key stretching)',
  author = 'Charles Pascoe',
  url='https://github.com/cpascoe95/stretch-pass',
  author_email = 'charles@cpascoe.co.uk',
  keywords = ['password', 'passpharse', 'kdf', 'hash', 'stretch', 'stretching'],
  classifiers = [],
  entry_points={
    'console_scripts': [
        'stretch-pass = stretch_pass:main'
    ]
  }
)
