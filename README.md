# Metadata Harvester

[![Version](https://img.shields.io/docker/v/fnndsc/pl-mdharvest?sort=semver)](https://hub.docker.com/r/fnndsc/pl-mdharvest)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-mdharvest)](https://github.com/FNNDSC/pl-mdharvest/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-mdharvest/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-mdharvest/actions/workflows/ci.yml)

`pl-mdharvest` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Abstract

...

## Installation

`pl-mdharvest` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-mdharvest` as a container:

```shell
apptainer exec docker://fnndsc/pl-mdharvest mdharvester [--args values...] input/ output/
```

To print its available options, run:

```shell
apptainer exec docker://fnndsc/pl-mdharvest mdharvester --help
```

## Examples

`mdharvester` requires two positional arguments: a directory containing
input data, and a directory where to create output data.
First, create the input directory and move input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
apptainer exec docker://fnndsc/pl-mdharvest:latest mdharvester [--args] incoming/ outgoing/
```

## Development

Instructions for developers.

### Building

Build a local container image:

```shell
docker build -t localhost/fnndsc/pl-mdharvest .
```

### Running

Mount the source code `mdharvester.py` into a container to try out changes without rebuild.

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/mdharvester.py:/usr/local/lib/python3.12/site-packages/mdharvester.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/pl-mdharvest mdharvester /incoming /outgoing
```

### Testing

Run unit tests using `pytest`.
It's recommended to rebuild the image to ensure that sources are up-to-date.
Use the option `--build-arg extras_require=dev` to install extra dependencies for testing.

```shell
docker build -t localhost/fnndsc/pl-mdharvest:dev --build-arg extras_require=dev .
docker run --rm -it localhost/fnndsc/pl-mdharvest:dev pytest
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/fnndsc/pl-mdharvest:1.2.3 .
docker push docker.io/fnndsc/pl-mdharvest:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to _ChRIS_.

```shell
docker run --rm docker.io/fnndsc/pl-mdharvest:1.2.3 chris_plugin_info -d docker.io/fnndsc/pl-mdharvest:1.2.3 > chris_plugin_info.json
```

Intructions on how to upload the plugin to _ChRIS_ can be found here:
https://chrisproject.org/docs/tutorials/upload_plugin

