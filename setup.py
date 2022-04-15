import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytypecho",
    version="2.1.0",
    author="Veoco",
    author_email="one@nomox.cn",
    description="Python Typecho Client (XMLRPC)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/veoco/PyTypecho",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)