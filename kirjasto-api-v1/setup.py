from setuptools import setup

setup(
    name="kirjasto-api-v2",
    version="1.0",
    description="",
    keywords="",
    author="",
    packages=["kirjasto-api-v2"],
    entry_points={"console_scripts": ["kirjasto-api-v2=kirjasto-api-v2.main:main"]},
    include_package_data=True,
    zip_safe=False
    )