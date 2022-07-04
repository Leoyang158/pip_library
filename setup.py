from setuptools import setup

from test import __version__

setup(
    name='test',
    version=__version__,

    url='https://github.com/Leoyang158/pip_library',
    author='Leo Yang',
    author_email='leoyang158@gmail.com',

    py_modules=['test'],
)