from setuptools import setup
setup(
    name = 'stretch-pass',
    packages = ['stretch_pass'],
    version = '0.1.3',
    description = 'Derive high-entropy passwords from passphrases using a slow key derivation function (a.k.a. key stretching)',
    author = 'Charles Pascoe',
    url='https://github.com/cpascoe95/stretch-pass',
    download_url='https://github.com/cpascoe95/stretch-pass/archive/v0.1.3.tar.gz',
    author_email = 'charles@cpascoe.co.uk',
    keywords = ['password', 'passpharse', 'kdf', 'hash', 'stretch', 'stretching'],
    classifiers = [ # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities'
    ],
    install_requires = [
        'argon2-cffi==16.3.0',
        'pyperclip==1.5.27'
    ],
    entry_points={
        'console_scripts': [
            'stretch-pass = stretch_pass:main'
        ]
    }
)
