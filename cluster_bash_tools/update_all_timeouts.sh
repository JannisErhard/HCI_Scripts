#!/bin/bash
for i in `sh ~/HCI_Scripts/cluster_bash_tools/check_status.sh  | grep TIME  | awk '{printf "%s_%s_%s\n", $1, $2, $3}'`
do
  echo $i
  cd $i
  if [ $1 == 1 ]
  then
    sh ~/HCI_Scripts/cluster_bash_tools/update_time.sh
  elif [ $1 == 3 ]
  then
    sh ~/HCI_Scripts/cluster_bash_tools/third_update_time.sh
  fi
  sbatch run_dice.sh
  cd -
done
