import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tradingrl',
    version='0.0.3',
    author='Mike Huls',
    author_email='saadsaeed150@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SaadSaeed150/tradingrl',
    license='MIT',
    packages=['tradingrl'],
    install_requires=['requests'],
)