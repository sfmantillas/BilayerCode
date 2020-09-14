#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A050/B3/L1/N002/Bloque04
#SBATCH --partition=medium
#SBATCH --job-name=P0503100204
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloquePair.out

python2.7 BloquePair.py
