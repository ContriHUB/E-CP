from setuptools import setup, find_packages

setup(
    name='ecp',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'ecp = src.Cli.cli:entry_point',
        ],
    },
)