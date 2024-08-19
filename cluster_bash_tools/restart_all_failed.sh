#!/bin/bash
for i in `sh ~/HCI_Scripts/cluster_bash_tools/check_status.sh  | grep Failed  | awk '{printf "%s_%s_%s\n", $1, $2, $3}'`
do
  cd $i
    sbatch run_dice.sh
  cd -
done
