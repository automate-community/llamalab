"""
## How to use

```shell
# Default syntax
$ py llamalab <module> <command> <parameters>

# Type -- --help on any command to get help text
$ py llamalab # To get help
```

```python
import llamalab as llama

llama.Cloud.send(**kwargs)
```

## Easy to Install

```shell
# Using git
$ git clone https://github.com/SerTor-Automate/llamalab
$ cd llamalab
$ pip install -r requirements.txt
$ py setup.py install
```

## Contributing

You can propose a feature request opening an issue, or a pull request.

Here is a list of llamalab contributors:

<a href="https://github.com/SerTor-Automate/llamalab/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=SerTor-Automate/llamalab" />
</a>
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="llamalab",
    version="0.1",
    author="Adrián Toral",
    author_email="adriantoral@sertor.es",
    description="Llamalab python modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Website": "https://github.com/SerTor-Automate/llamalab",
        "Issues": "https://github.com/SerTor-Automate/llamalab/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["llamalab"],
    package_dir={"": "src"},
    install_requires=["fire~=0.4.0", "setuptools~=47.1.0", "requests~=2.24.0"],
    python_requires=">=3.6",
    keywords='python, python3',
)
