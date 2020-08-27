# import re  # regex tool
from setuptools import setup


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="Crypto",
    version="1.0.0",  # Required
    packages=["crypto"],
    entry_points={"console_scripts": ["crypto = crypto:main"]},
    description="An encrypting / decrypting utility for Linux/Windows. ",
    long_description=long_descr,
    author="Samuel Oloruntoba Lagunju",
    author_email="taofsamuel@gmail.com",
    url="https://github.com/SamueLagunju/Crypto.git",
)
