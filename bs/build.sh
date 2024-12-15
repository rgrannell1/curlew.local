#! /usr/bin/env bash

HERE=$(realpath -s "$(dirname "$0")")

rs build:video
rs build:html
