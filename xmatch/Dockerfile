# use an official Python runtime as a parent image
FROM jupyter/scipy-notebook:8ccdfc1da8d5

# install Python's packages as jovyan user
RUN conda config --set ssl_verify no
RUN conda install pip git
RUN pip install git+https://github.com/podondra/spectraml.git@fdae35886986c53c3e5602cb964b1d49e4cf355b#egg=spectraml
