"""Package setup"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="spacy-stubs",
    version="0.1",
    author="David Assefa Tofu",
    description="incomplete stubs for spacy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["spacy-stubs"],
    python_requires=">=3.6",
    install_requires=["spacy>=2.0.0", "typing_extensions"],
    package_data={"": ["*.pyi", "py.typed"]},
    extras_require={"dev": ["black", "mypy"]},
    classifiers=[  # classifiers can be found here: https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Typing :: Typed",
    ],
    zip_safe=False,
)
