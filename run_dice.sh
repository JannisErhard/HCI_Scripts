#!/bin/sh

#SBATCH --time=TIME
#SBATCH --mem-per-cpu=MEMORY
#SBATCH --ntasks-per-node=n_tasks       # number of MPI processes: 4
#SBATCH --nodes=n_nodes                 # number of nodes
#SBATCH --account=ACC
#SBATCH --job-name=NAME
#SBATCH --output=slurm-NAME-%j.out

module restore atomdb
source ~/envs/heat_bath_fci/bin/activate


# EOM -> Exit 0 if successful
python ./run_dice.py > ./dice.log

rm *.bkp tmp*
