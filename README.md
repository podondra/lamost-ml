# LAMOST Spectra Machine Learning

Machine Learning in LAMOST survey.

## Projects

1. **candidates**, command line utility for working with candidates
2. **china-xmatch**, cross-matching of some our candidates with result from
	chinese colleague
3. **lamost-dr1-preprocessing**, script for LAMOST DR1 preprocessing
4. **normalized-vs-raw**, experiment which shows that neural network manages
	both raw and normalized spectra

## Ondrejov Dataset

This work makes use of
[Ondrejov Dataset](https://github.com/podondra/ondrejov-dataset)
which is going to be available soon online on [Zenodo](https://zenodo.org/).

The dataset should be stored as `data/ondrejov-dataset.csv`.

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
