#!/bin/bash
# Activate the environment for our project, then kick off pycharm.

# EDIT THIS: set to your installation
PYCHARM_DIR=pycharm-2017.3.3
VENV=~/venv/pcf
source ${VENV}/bin/activate && /opt/${PYCHARM_DIR}/bin/pycharm.sh &
