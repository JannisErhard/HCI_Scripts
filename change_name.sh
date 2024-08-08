for i in `find -iname "*.fchk"`
do 
echo $i
sed "s/RO\ calculation/RO\_calculation/g" $i > tmp
mv tmp $i
done 
