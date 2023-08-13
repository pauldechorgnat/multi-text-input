import json
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

with open("long_description.md") as f:
    long_description = f.read()

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=[package_name],
    include_package_data=True,
    data_files=[("config", ["long_description.md"])],
    license=package['license'],
    description=package.get('description', package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers = [
        'Framework :: Dash',
    ],    
)
