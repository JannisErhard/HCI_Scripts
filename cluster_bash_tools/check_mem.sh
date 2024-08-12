#!/bin/bash
for i in */*.out
do 
  job=`echo $i | sed "s/-/ /g" | sed "s/\.out//g" | awk '{print $NF}'`
  IS=`echo $i | sed "s/\_/\ /g" | sed "s/\//\ /g" | awk '{print $1, $2, $3}'`
  MEM=`seff $job | grep "Memory Utilized"`
  echo $IS $MEM
done  | sort -rgk 6
