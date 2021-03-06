from setuptools import find_packages, setup

setup(
    name = 'aws-switchrole',
    packages = find_packages(),
    version = '0.0.2',
    description = 'a tool to allow you to switch AWS roles on your console',
    author = 'hybby',
    author_email = 'iamdrew@gmail.com',
    url = 'https://github.com/hybby/aws-switchrole',
    download_url = 'https://github.com/hybby/aws-switchrole/archive/0.0.2.tar.gz',
    keywords = ['aws', 'iam', 'sts'],
    install_requires = [
        'awscli>=1.15.25',
        'pyperclip>=1.6.0',
    ],
    entry_points={
        'console_scripts': [ 'aws-switchrole=aws_switchrole.aws_switchrole:main' ]
    },
    classifiers = [],
)
