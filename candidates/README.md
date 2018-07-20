# Candidates Utilities

The idea of code in this directory it to support working with candidates.

It should work as skeleton so that the code is base which can be changed
to extract different metadata or render different images.

## Usage

Get into the container with `bash`:

	$ docker exec -i -t podondruv /bin/bash

Run the `candidates.py` script:

	$ cd candidates/
	$ export LC_ALL=C.UTF-8
	$ export LANG=C.UTF-8
	$ python3 candidates.py --help
