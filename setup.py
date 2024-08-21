from setuptools import setup, find_packages

setup(
    name="sync-async",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    description="A utility for creating synchronous and asynchronous compatible methods.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/islati/sync-async",
    author="Islati // Skreet Media Inc // Wogwon Society",
    author_email="islati@wogwon.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": ["pytest", "pytest-asyncio","pytest-cov","twine"]
    },
)
