#!/bin/bash

workdir=$PWD

for j in */
do 
  cd $j
  for i in `ls *.out | tail -n 1`
  do
    job=`echo $i | sed "s/-/ /g" | sed "s/\.out//g" | awk '{print $NF}'`
    IS=`echo $j | sed "s/\_/\ /g" | sed "s/\//\ /g" | awk '{print $1, $2, $3}'`
    MEM=`seff $job | grep "State"`
    echo $IS $MEM
  done
  cd $workdir 
done
