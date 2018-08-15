# LAMOST Spectra Machine Learning

Machine Learning in LAMOST survey.

## Projects

Short description of projects in this repository.

### Candidates

Command line utility for working with candidates.

### China Cross-matching

Cross-matching of some our candidates with result from chinese colleagues.

### Spark LAMOST Preprocessing

Preprocessing project for LAMOST spectra which uses Spark for parallelism.

### LAMOST DR1 Preprocessing

Script for LAMOST DR1 preprocessing.

### Normalized vs Raw

Experiment which shows that neural network manages both raw and normalized
spectra.

### Iterative CNN

Code for the paper concerning discovery of emission-line stars in LASMOST
survey.

## Ondrejov Dataset

This work makes use of
[Ondrejov Dataset](https://github.com/podondra/ondrejov-dataset)
which is going to be available soon online on [Zenodo](https://zenodo.org/).

## Docker Container Information

To run docker container:

	$ nvidia-docker run -d -p 8888:8888 \	# notebook on localhost:8888
		-v $PATH_TO_NOTEBOOKS:/notebooks \
		-v $PATH_TO_LAMOST_DATA:/lamost:ro \
		--name $CONTAINER_NAME \
		tensorflow/tensorflow:latest-gpu-py3

It is needed to use `nvidia-docker` command else the container will not be
able to use CUDA libraries.

To find URL of the Docker container with secret token:

	docker exec CONTAINER jupyter notebook list

## TODO list

- Have a one big container is not reasonable as different project may depend
	on different versions.
