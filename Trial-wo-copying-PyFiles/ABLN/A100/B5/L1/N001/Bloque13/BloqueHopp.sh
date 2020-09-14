#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A100/B5/L1/N001/Bloque13
#SBATCH --partition=medium
#SBATCH --job-name=H1005100113
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloqueHopp.out

python2.7 BloqueHopp.py
