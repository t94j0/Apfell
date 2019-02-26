import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apfell",
    version="0.0.1",
    author="Cody Thomas",
    author_email="",
    description="A collaborative, multi-platform, red teaming framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/its-a-feature/Apfell",
    packages=['apfell'],
    entry_points={'console_scripts': ['apfell = apfell.__init__:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
