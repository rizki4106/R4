from setuptools import setup

def readme():
    with open("README.md") as f:
        README = f.read()
    return README

setup(
    name="R4",
    version="0.0.1",
    description="R4 is a python package for encrypt your important data",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/rizki4106/R4.git",
    license="MIT",
    classifiers=[
        "Licence :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    packages=['R4'],
    include_package_data=True,
)