#!/bin/bash
#SBATCH --job-name=DUMMY_NAME
#SBATCH --account=def-ayers
#SBATCH --time=01-00:00
#SBATCH --mem=125G
#SBATCH --cpus-per-task=32
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module load python/3.11.5
source /home/jerhard/envs/1RMDFT/bin/activate 
python ./B_Singlepoint.py > out 
