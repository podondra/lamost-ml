# use an official Python runtime as a parent image
FROM jupyter/pyspark-notebook:8ccdfc1da8d5

# create working directory first to be owned by jovyan
# else it will be owned by root and next steps will produce permission denied
RUN mkdir /home/jovyan/preprocessing

# set the working directory
WORKDIR /home/jovyan/preprocessing

# copy the current directory contents into the container at /preprocessing
ADD . /home/jovyan/preprocessing

# install any needed packeages specified in requirements.txt
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt 
