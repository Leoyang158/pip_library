import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='testboxTryOut',
    version='0.0.3',
    author='Mike Huls',
    author_email='leoyang158@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Leoyang158/pip_library',
    project_urls = {
    },
    license='MIT',
    packages=['testboxTryOut'],
    install_requires=['requests'],
)