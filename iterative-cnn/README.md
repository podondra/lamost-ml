# Iterative CNN

TODO write project summary.

## TODO List

1. implement `itercnn` module
1. put only result exploration and explanation into a Jupyter notebook
1. describe how to get data
1. write project summary into README

## Data

There should be following data files in `data/` directory:

- `ondrejov-dataset.csv` see https://github.com/podondra/ondrejov-dataset,
- `lamost-dr1.hdf5` file containing LAMOST spectra produced by preprocessing,
- `candidates-with-metadate.csv` file with candidates with metadata, assumption
	is that this analysis will produce a candidates list, then one can get
	metadata using candidates script in the same repo but it such be moved
	to `spectraml`.

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
