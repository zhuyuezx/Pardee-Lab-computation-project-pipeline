#!/bin/bash

if [ $# -lt 1 ]; then
	echo "Usage: ./run_alphafold.sh [input fasta path] [output directory]"
	exit 1
fi
input=$1
if [ $# -eq 1 ]; then
	output="/tmp/alphafold"
else
	output=$2
fi

temp=""
if [ -d $input ]; then
	for sub in ${input}/*; do
		if [[ "$sub" == *".fasta" ]]; then
			temp+=$sub","
		fi
	done
	temp=${temp::-1}
fi
input=$temp
echo "files found: ${input}"

if [ -d $output ]; then
	echo "saving results to ${output}"
else
	mkdir $output
	echo "saving results to ${output}"
fi

python3 docker/run_docker.py --fasta_paths=$input \
	--max_template_date=2021-05-14 --output_dir=$output \
	--data_dir=/mnt/disks/data --model_preset=multimer \
	--num_multimer_predictions_per_model=1
