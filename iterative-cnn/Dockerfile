# use an official Python runtime as a parent image
FROM tensorflow/tensorflow:1.8.0-gpu-py3

# install git so spectraml can be installed from GitHub
RUN apt-get update && apt-get install -y git

# create directory for Python's packages installation
# so that spectraml can be correctly installed
WORKDIR /requirements

# copy requirements.txt to the container
COPY requirements.txt .

# install Python's packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# change workdir to default tensorflow Docker path
WORKDIR /notebooks
