# {
#  "cells": [],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "name": "python",
#    "version": "3.8.0"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 2
# }
from setuptools import find_packages,setup
from typing import List


def get_req(file:str)->List[str]:
    '''
    This function will return the list of the requirements
    '''
    req=[]
    with open(file) as file:
        req=file.readlines()
        req=[req.replace("\n",'') for req in req]
        
        if '-e .' in req:
            req.remove('-e .')
    return req


setup(
    name="MLproject",
    version="0.0.1",
    author="Yogesh",
    author_email="yogeshsondagar52@gmail.com",
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)