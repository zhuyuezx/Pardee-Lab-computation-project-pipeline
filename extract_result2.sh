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
for i in $(seq 1 109); do
	cd "high_brightness${i}"
    echo "high_brightness${i}"	
    cp "ranked_0.pdb" "high_brightness${i}.pdb"	
    mv "high_brightness${i}.pdb" $to
	cd ..
done

