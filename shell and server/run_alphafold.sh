#!/bin/bash

if [ $# -ge 1 ]; then
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
    exit 0
fi

echo "This script helps to read all *.fasta files in one designated folder, "
echo "run alphafold prediction on all of them,"
echo "and store results in designated path (\"/tmp/alphafold\" in default)"
echo " "
echo "Please type the source folder path here and press ENTER"
echo "If the folder is inside current path, directly type its name"
echo "or you can input the relative path or absolute path:"

read input
temp=""
if [ -d $input ]; then
    for sub in ${input}/*; do
        if [[ "$sub" == *".fasta" ]]; then
            temp+=$sub","
        fi
    done
    temp=${temp::-1}
else
    echo "no such source folder found, please check the path"
    exit 0 
fi
input=$temp
echo "files found: ${input}"

echo " "
echo "Please type the path where you want to store the results here and press ENTER"
echo "If you directly press ENTER, results will be stored at \"tmp/alphafold\":"
read output
if [[ "$output" == "" ]]; then
    output="/tmp/alphafold"
fi

if [ -d $output ]; then
    echo "saving results to ${output}"
else
    mkdir $output
    echo "saving results to ${output}"
fi

echo "If you want to use multimer (there are multiple chains in the sequence), enter YES"
echo "Else, just directly press ENTER"
read mode
if [ -z "$mode" ]; then
	python3 docker/run_docker.py --fasta_paths=$input \
		--max_template_date=2021-05-14 --output_dir=$output \
		--data_dir=/mnt/disks/data \
		--num_multimer_predictions_per_model=1
else
	python3 docker/run_docker.py --fasta_paths=$input \
		--max_template_date=2021-05-14 --output_dir=$output \
		--data_dir=/mnt/disks/data --model_preset=multimer \
		--num_multimer_predictions_per_model=1
fi
