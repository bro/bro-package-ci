from setuptools import setup, find_packages

setup(name='bro-package-ci',
    version='0.7.0',
    zip_safe=True,
    packages=find_packages(),
    install_requires=[],
    entry_points = {
        'console_scripts': [
            'bro-package-check = bro_package_check.check:main',
        ]
    }
)
