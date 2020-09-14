#!/bin/bash -l
#SBATCH -D /A001/B1/L0/N001/Bloque00
#SBATCH --partition=medium
#SBATCH --job-name=PaA001B1L0N001Bloque00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-18:40:00

#SBATCH --output BloquePair.out

python2.7 BloquePair.py
