#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A002/B3/L0/N001/Bloque33
#SBATCH --partition=medium
#SBATCH --job-name=H0023000133
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloqueHopp.out

python2.7 BloqueHopp.py
