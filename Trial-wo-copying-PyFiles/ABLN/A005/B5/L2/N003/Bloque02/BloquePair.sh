#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A005/B5/L2/N003/Bloque02
#SBATCH --partition=medium
#SBATCH --job-name=P0055200302
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloquePair.out

python2.7 BloquePair.py
