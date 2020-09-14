#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A100/B5/L0/N001/Bloque34
#SBATCH --partition=medium
#SBATCH --job-name=P1005000134
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output BloquePair.out

python2.7 BloquePair.py
