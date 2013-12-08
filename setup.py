import sys

from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test


class PyTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='SpamIpsum',
    version='0.1dev',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/khris/spamipsum',
    license='MIT Licence',
    author='Hong Segi',
    author_email='khris' '@' 'khrislog.net',
    description='Placeholder for ugly real world',
    tests_require=['pytest'],
    cmdclass={'test': PyTest}
)
