import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-flipper", # Replace with your own username
    version="0.0.1",
    author="Lucas & Fatih",
    author_email="legeek568@gmail.com",
    description="A small code for DIY flipper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Raspberry Pie",
    ],
    python_requires='>=3.6',
)