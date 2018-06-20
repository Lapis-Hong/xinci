#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
# from distutils.core import setup
from setuptools import setup, find_packages


setup(name="xinci",
      version="1.2.0",
      description="Chinese words extraction and new words discovery",
      long_description=open("README.md", "r").read(),
      long_description_content_type="text/markdown",
      author="Lapis-Hong",
      author_email="dinghongquan@sjtu.edu.cn",
      url="https://github.com/lapis-hong/xinci",
      license="MIT",
      keywords='NLP, Chinese words extraction, New words discovery',
      # Name the folder where your packages live:
      # (If you have other packages (dirs) or modules (py files) then
      # put them into the package directory - they will be found
      # recursively.)
      packages=find_packages(),
      # 'package' package must contain files (see list above)
      # I called the package 'package' thus cleverly confusing the whole issue...
      # This dict maps the package name =to=> directories
      # It says, package *needs* these files.
      package_dir={'xinci': 'xinci'},
      package_data={'xinci': ['*.*']},  # include common.dic
      # 'runner' is in the root.
      # scripts=["runner"],
      # This next part it for the Cheese Shop, look a little down the page.
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ]
)