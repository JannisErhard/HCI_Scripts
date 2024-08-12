#!/bin/bash
sed "s/03:00:00/06:00:00/g" run_dice.sh  > tmp
mv tmp  run_dice.sh 
