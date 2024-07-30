#!/bin/bash
workdir=$PWD
for i in Ca
#As Br Co  Cr  Cu  Fe  Ga  Ge  Kr  Mn  Ni  Sc  Se  Ti  V  Zn
do
  cp apost3d.py  dice_template_noPT.py  make_dice_jobs.py $i/
  cd $i
  python make_dice_jobs.py $i
  for j in */
    do 
    cp apost3d.py $j/
    cp *.pkl $j/
    cd $j
    #sbatch run_dice.sh
    cd -
  done
  cd $workdir
done
