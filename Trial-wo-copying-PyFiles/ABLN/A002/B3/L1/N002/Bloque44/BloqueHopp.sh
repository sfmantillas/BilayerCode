#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A002/B3/L1/N002/Bloque44
#SBATCH --partition=medium
#SBATCH --job-name=H0023100244
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloqueHopp.out

python2.7 BloqueHopp.py
