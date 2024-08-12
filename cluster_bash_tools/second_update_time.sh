#!/bin/bash
sed "s/06:00:00/12:00:00/g" run_dice.sh  > tmp
mv tmp  run_dice.sh 
