#!/bin/bash
for i in `sh ~/HCI_Scripts/check_status.sh  | grep TIME  | awk '{printf "%s_%s_%s\n", $1, $2, $3}'`
do
  echo $i
  cd $i
  sh ~/HCI_Scripts/update_time.sh
  sbatch run_dice.sh
  cd -
done
