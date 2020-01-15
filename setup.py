from setuptools import setup

def readme():
    with open("README.md") as f:
        README = f.read()
    return README

setup(
    name="R4",
    version="0.0.1",
    author_email="rizkimaulana348@gmail.com",
    description="R4 is a python package for encrypt your important data",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/rizki4106/R4.git",
    download_url="https://github.com/rizki4106/R4/archive/master.zip",
    keywords=["encrypt", "decrypt", "base64", "base64_encode", "base64_decode","md5"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    packages=['R4'],
    include_package_data=True,
)