from setuptools import find_packages, setup

setup(
    name="appbase",
    version="0.8.1",
    url="https://github.com/stckme/appbase",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    description="Helps develop python applications",
    long_description=open("README.rst").read(),
    packages=find_packages(),
    install_requires=[
        "blinker",
        "jsonschema",
        "gevent",
        "peewee",
        "psycopg2",
        "psycogreen",
        "flask",
        "html2text",
        "redis",
        "arnold",
        "requests_oauthlib",
    ],
    author="Shekhar Tiwatne",
    author_email="pythonic@gmail.com",
    test_suite="tests",
)
