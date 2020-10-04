# setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # name is the DISTRIBUTION NAME of your package--must not already be taken
    # use with username to ensure it is unique
    name="example-pkg-A-B-G",
    # package version
    version="0.0.1",
    # author and author email ID the author of the package
    author="ABG",
    author_email="azaniazbaker@gmail.com",
    # describe a short, one-sentence summary of the package
    description="Sample package from python.org tutorial",
    # long description is shown on the detail package on the Python Package index
    # common pattern is to load detailed description from README.md
    long_description=long_description,
    # tell the index what type of markup is used for the long description
    long_description_content_type="text/markdown",
    # give the URL for the homepage of the project (e.g., GitHub, BitBucket, etc.)
    url=""
)
