#!/bin/bash
for j in */
do 
  i=`ls $j/*.out | tail -n 1`
  job=`echo $i | sed "s/-/ /g" | sed "s/\.out//g" | tail -n 1 | awk '{print $NF}'`
  IS=`echo $i | sed "s/\_/\ /g" | sed "s/\//\ /g" | tail -n 1 | awk '{print $1, $2, $3}'`
  MEM=`seff $job | grep "Memory Utilized"`
  echo $IS $MEM
done  | sort -rgk 6
