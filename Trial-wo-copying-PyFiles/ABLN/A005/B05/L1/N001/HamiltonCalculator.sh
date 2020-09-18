#!/bin/bash -l
#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A005/B05/L1/N001
#SBATCH --partition=medium
#SBATCH --job-name=H005051001
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1-23:40:00

#SBATCH --output HamiltonCalculator.out

python2.7 HamiltonCalculator.py
