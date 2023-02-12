import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="donotprint",
    version="1.0.0",
    author="geng_MAX",
    author_email="geng_MAX@hotmail.com",
    description="function print work or not work",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geng-Max/donotprint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3',
)
