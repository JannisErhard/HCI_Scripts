for i in `sh ~/HCI_Scripts/cluster_bash_tools/check_status.sh  | grep MEM  | awk '{printf "%s_%s_%s\n", $1, $2, $3}'`
do
  cd $i
  if [ $1 == 1 ]
  then
    sh ~/HCI_Scripts/cluster_bash_tools/update_mem.sh
    sbatch run_dice.sh
  elif [ $1 == 2 ]
  then
    sh ~/HCI_Scripts/cluster_bash_tools/second_update_mem.sh
    sbatch run_dice.sh
  fi
  cd -
done
