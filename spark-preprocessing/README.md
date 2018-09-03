# Spark LAMOST Preprocessing

Script with code to run parallel preprocessing of LAMOST spectra.
Uses [spectraml](https://github.com/podondra/spectraml).

## Docker

TODO Docker in this setting does not work.

First build the image using:

	$ docker build -t spark-preprocessing

Then run `bash` inside the container so the CLI can be used:

	$ docker run -i -t -v /path/to/data:/home/jovyan/data:ro \
		spark-preprocessing bash

Do not forget to mount in the data in *read-only* mode.

## Spark Environment

Set up environment if using Spark 2.3.1 installed in virtual environment:

	$ python3 -m venv venv  # or use virtualenv -p python3 venv
	$ source venv/bin/activate  # active the environment
	$ pip install --upgrade pip setuptools wheel  # update basic packages
	$ pip install -r requirements.txt  # install required packages

Export needed enviromental variables. Spark 2.3.1 supports only Java 8+, e.g.:

	$ export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

Link Hadoop native library by setting `LD_LIBRARY_PATH`, e.g.:

	$ export LD_LIBRARY_PATH=/opt/hadoop/lib/native

These commands are applicable on `antares`. On other machines it is needed to
correct the paths.
