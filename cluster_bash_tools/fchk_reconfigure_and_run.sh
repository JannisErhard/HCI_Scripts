#!/bin/bash
El=$1
workdir=$PWD
for charge in  17 18 19
do
  cd "$El"_"$charge"_*/
  cp ~/HCI_Scripts/apost3d.py ./
  sbatch run_dice.sh
  cd -
done
