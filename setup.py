from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in star/__init__.py
from star import __version__ as version

setup(
	name="star",
	version=version,
	description="deskripsi tes",
	author="BTI UMS",
	author_email="bti@ums.ac.id",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
