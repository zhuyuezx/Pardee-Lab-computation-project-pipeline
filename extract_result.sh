if [ $# -lt 1 ] || [ $# -gt 2 ]; then
	echo "Usage: ./extract_result.sh [to which folder] [from which folder(optional)]"
	exit 1
fi

to=$1
if [ $# -lt 2 ]; then
	from="/tmp/alphafold"
else
	from=$2
fi
#echo "extracting ${from} to ${to}"

cd $from
for folder in "$from"/*; do
	cd $folder
	cp "ranked_0.pdb" "${folder}.pdb"	
	cd ..
done
mv *.pdb $to

