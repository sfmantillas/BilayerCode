#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A001/B4/L2/N003/Bloque04
#SBATCH --partition=medium
#SBATCH --job-name=H0014200304
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloqueHopp.out

python2.7 BloqueHopp.py
