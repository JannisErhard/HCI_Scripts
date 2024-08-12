for i in `sh ~/HCI_Scripts/check_status.sh  | grep MEM  | awk '{printf "%s_%s_%s\n", $1, $2, $3}'`
do
  cd $i
  sh ~/HCI_Scripts/update_mem.sh
  sbatch run_dice.sh
  cd -
done
