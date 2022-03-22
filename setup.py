from setuptools import setup


setup(
    name="sesh",
    version="0.0.1",
    license="",
    author="Francisco Gonzalez",
    author_email="fg@panch.io",
    description="AWS Session Manager",
    entry_points={
        "console_scripts": ["sesh=sesh.cli:sesh"]
    },
)