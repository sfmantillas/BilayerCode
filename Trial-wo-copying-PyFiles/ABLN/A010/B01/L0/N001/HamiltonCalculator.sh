#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A010/B01/L0/N001
#SBATCH --partition=medium
#SBATCH --job-name=H010010001
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output HamiltonCalculator.out

python2.7 HamiltonCalculator.py
