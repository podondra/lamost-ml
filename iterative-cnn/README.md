# Iterative CNN

All information concerning the project are in the Jupyter notebook.

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
