from setuptools import setup, find_packages

setup(
    name="primordial-wrapper",
    version="1.2.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    extras_require={
        "dev": [
            "pytest",
            "requests-mock",
        ],
    },
    description="Wrapper for Primordial API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="KirbyHacks",
    url="https://github.com/KirbyHacks/primordial-wrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
