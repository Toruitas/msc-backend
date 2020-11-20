# Msc Thesis Project Main Repository

Msc Creative Computing 2019-2020 Msc Final Thesis Project

By: Stuart Leitch

Supervisor: Mick Grierson

## Table of Contents:
* Companion Repositories
* Installation Instructions
* Introduction
* Project Journal


## Companion Repositories
1. [Jupyter Notebooks](https://github.com/Toruitas/msc-notebooks)
2. [Backend Server](https://github.com/Toruitas/msc-backend)
3. [Chrome Extension](https://github.com/Toruitas/msc-extension)

## Installation Instructions
### Backend server

Just your typical Python setup - using either venv or Py Poetry. 

Linux/Mac instructions are as follows:
1. `git clone https://github.com/toruitas/msc-backend mscbackend`
2. `cd mscbackend`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. Decompress the classifier so that the .pkl file is in the same folder as everything else. `tar -xf final-classifier-2.tar.xz`