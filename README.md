
[![Medium Badge](https://badgen.net/badge/icon/medium?icon=medium&label)](https://medium.com/analytics-vidhya/simple-camera-models-with-numpy-and-matplotlib-92281f15f9b2)

## Introduction

This repository contains a notebook and a library to explain the operation of some simple camera models. The theory presented is almost entirely taken from the book [Multiple View Geometry in Computer Vision](https://www.robots.ox.ac.uk/~vgg/hzbook/) by Richard Hartley and Andrew Zisserman, in particular from chapter 6 "Camera Models". The purpose of this work is therefore not to explain the theory but to apply it, trying to improve the reader's understanding of these concepts.

## Get Started

In order to use the notebook and library here, you must first create and activate a virtual environment using Anaconda. If you have not yet installed Anaconda, you can do so by following [these](https://docs.anaconda.com/anaconda/install/) instructions. After that you just need to run the following commands:
```bash
$ cd camera-models
$ conda env create --prefix ./env --file environment.yml
$ conda activate ./env
$ jupyter notebook
```
