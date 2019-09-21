from pathlib import Path

from setuptools import setup

setup(
    name="zera",
    version=1,
    packages=["zera"],
    author="Furkan Onder",
    author_email="furkantahaonder@gmail.com",
    description="static website generator",
    license="MIT",
    keywords="static web generator html markdown",
    url="https://github.com/furkanonder/Zera",
    include_package_data=True,
    entry_points={"console_scripts": ["zera = zera.zera:main"]},
)
