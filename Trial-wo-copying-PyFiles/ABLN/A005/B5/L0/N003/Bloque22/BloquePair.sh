#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A005/B5/L0/N003/Bloque22
#SBATCH --partition=medium
#SBATCH --job-name=P0055000322
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloquePair.out

python2.7 BloquePair.py
