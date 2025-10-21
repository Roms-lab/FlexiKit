from setuptools import setup, find_packages

setup(
    name="FlexiKit",
    version="0.1.2",
    author="Zachary Sherwood",
    author_email="zachary.sherwood2009@gmail.com",
    description="Python library for many uses across the board.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0+',
)

