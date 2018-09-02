# China Xmatching

See the notebook for info about this project.

## Docker

To run this code in a Docker container use:

    $ docker run \
        --user $(id -u) --group-add users \
        -p $PORT_OUT:8888 \
        -e JUPYTER_LAB_ENABLE=yes \
        -v "$PWD":/home/jovyan \
        --name $CONTAINER_NAME \
	podondra/xmatch

It uses the [jupyter/scipy-notebook](
	https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook
). Make sure to be in lamost-ml/china-xmatch so that $PWD is set correctly.
