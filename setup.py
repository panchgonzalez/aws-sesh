from setuptools import setup

setup(
    name="sesh",
    version="0.0.1",
    url="https://github.com/panchgonzalez/aws-sesh",
    author="Francisco Gonzalez",
    author_email="fg@panch.io",
    description="AWS MFA session manager",
    entry_points={
        "console_scripts": ["sesh=sesh.cli:sesh"]
    },
)