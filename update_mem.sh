#!/bin/bash
sed "s/mpirun -np 10/mpirun -np 5/g" run_dice.py > tmp; mv tmp run_dice.py
sed "s/16/32/g" run_dice.sh  | sed "s/10/5/g" > tmp; mv tmp run_dice.sh
