import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pengeomgen",
    version="0.0.1",
    author="Antonio Serrano",
    author_email="toni.sm91@gmail.com",
    description="An easy geometry-definition file generator for PENELOPE PENGEOM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Toni-SM/pengeomgen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)