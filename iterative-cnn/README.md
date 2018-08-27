# Iterative CNN

TODO write project summary.

## TODO List

1. implement `itercnn` module
1. put only result exploration and explanation into a Jupyter notebook
1. describe how to get data
1. write project summary into README

## Docker

To run the Docker container use:

	$ git clone https://github.com/podondra/lamost-ml
	$ cd lamost-ml/iterative-cnn
	$ docker build -t $IMAGE_NAME .
	$ nvidia-docker run \
		-it \
		-v /path/to/iterative-cnn:/notebooks \
		-p $TENSORBOARD_PORT:6006 \
		-p $JUPYTER_PORT:8888 \
		--name $CONTAINER_NAME \
		$IMAGE_NAME
