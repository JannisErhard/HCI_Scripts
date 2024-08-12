#!/bin/bash
sed "s/12:00:00/24:00:00/g" run_dice.sh  > tmp
mv tmp  run_dice.sh 
