#!/bin/bash
sed "s/24:00:00/48:00:00/g" run_dice.sh  > tmp
mv tmp  run_dice.sh 
