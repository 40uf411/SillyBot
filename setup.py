#!/usr/bin/python
# -*- coding=utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()

setup (name='sillybot', version='0.1',
      description="SillyBot: fastest way to develop scrapping bots",
      long_description = readme(),      

      author='Ali Aouf',
      author_email='40uf4l1@gmail.com',
      url='https://40uf411.github.io/SillyBot/',
      license='GPL',
      package_dir={'sillybot': 'sillybot'},
      packages=['sillybot'],
      install_requires=[
          "requests",
          "selenium",
          "undetected_chromedriver",
          "wget"
      ],         
      include_package_data=True,
      package_data = {
        'sillybot': ['doc/*.*','doc/html/*', 'data/*.sqlite', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

