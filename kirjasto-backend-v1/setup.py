from setuptools import setup

setup(
    name="kirjasto-backend-v1",
    version="1.0",
    description="",
    keywords="",
    author="",
    packages=["kirjasto-backend-v1"],
    entry_points={"console_scripts": ["kirjasto-backend-v1=kirjasto-backend-v1.main:main"]},
    include_package_data=True,
    zip_safe=False
    )