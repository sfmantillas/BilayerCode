#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A500/B4/L0/N003/Bloque04
#SBATCH --partition=medium
#SBATCH --job-name=P5004000304
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloquePair.out

python2.7 BloquePair.py
