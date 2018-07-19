# LAMOST Spectra Machine Learning

Machine Learning in LAMOST survey.

## Ondrejov Dataset

This work makes use of
[Ondrejov Dataset](https://github.com/podondra/ondrejov-dataset)
which is going to be available soon online on [Zenodo](https://zenodo.org/).

The dataset should be stored as `data/ondrejov-dataset.csv`.

## Docker Container Information

To run docker container:

	nvidia-docker run -d -p 8888:8888 \	# have the jupyter notebook on localhost:8888
		-v $PATH_TO_NOTEBOOKS:/notebooks \	# e.g. /data/podondra/lamost-ml
		-v $PATH_TO_LAMOST_DATA:/lamost:ro \	# e.g. /data/public/LAMOST-DR1/fits
		--name podondruv tensorflow/tensorflow:latest-gpu-py3

To find URL of the Docker container with secret token:

	docker exec CONTAINER jupyter notebook list
