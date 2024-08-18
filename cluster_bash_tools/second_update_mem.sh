#!/bin/bash
sed "s/mpirun -np 5/mpirun -np 2/g" run_dice.py > tmp; mv tmp run_dice.py
sed "s/32/125/g" run_dice.sh  | sed "s/5/2/g" > tmp; mv tmp run_dice.sh
