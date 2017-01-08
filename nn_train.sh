#!/bin/bash
#SBATCH -t 1-10:00:00
#SBATCH -n 1
#SBATCH -p gpu

module load python

export PYTHONPATH=$HOME/pythonpackages/lib/python:$PYTHONPATH

module load cuda

module load cudnn

cd $HOME/prednet

srun python ego_train.py