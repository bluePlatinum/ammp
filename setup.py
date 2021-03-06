import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ammp",
    author="bluePlatinum",
    author_email="jukic.rok@gmail.com",
    description="Mission Planner for KSP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bluePlatinum/ammp",
    package_dir={"": "ammp"},
    packages=setuptools.find_packages(where="ammp"),
    python_requires=">3.7"
)
