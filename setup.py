from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-hkang42", # the name that you will install via pip
    version="1.2",
    author="Harrison Kang",
    author_email="H.Kand.Q@gmail.com",
    description="Add new column to DF from list. Split date into month, day, year.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/HKang42/lambdata-hkang42",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)