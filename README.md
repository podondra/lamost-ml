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
[Ondrejov Dataset](https://github.com/podondra/ondrejov-dataset).

## Docker Information

Nice paper about reproducible research with Docker:
https://arxiv.org/abs/1410.0846.

If it is needed to use GPU for computations use `nvidia-docker` command
instead of `docker` else the container will not be able to use CUDA libraries.

To find URL of the Docker container with secret token:

	docker exec CONTAINER jupyter notebook list

Helpful tutorial can be found at
[Docker documentation](https://docs.docker.com/get-started/part2/)
and
[Best practices for writing Dockerfiles](
https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
).
