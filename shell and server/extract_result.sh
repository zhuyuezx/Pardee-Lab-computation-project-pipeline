if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    echo "This script helpes to extract alphafold predictions stored in multiple folders under given path"
    echo "and put all results in designated path"

    echo "Please input the folder where you want extract result from and press ENTER"
    echo "If you directly press ENTER, source path will be set to \"tmp/alphafold\":"
    read from
    if [ -z "$from" ]; then
        from="/tmp/alphafold"
    fi

    echo " "
    echo "Please input the folder where you want to put all extracted results and press ENTER"
    echo "Please input absolute path here, for example, if you want to put it in home page"
    echo "enter \"/home/alphafold_user\":"
    read to

    if [ -d $from ]; then
        if [ -d $to ]; then
            echo "extracting from ${from} to ${to}"
        else 
            mkdir $to
            echo "extracting from ${from} to ${to}"
        fi
        cd $from
        for folder in ${from}/*; do
            cd $folder
            cp "ranked_1.pdb" "${folder}.pdb"	
            cd ..
        done
        mv *.pdb $to
    else 
        echo "No such source path found, please check your input"
        exit 0
    fi
    exit 0
fi

to=$1
if [ $# -lt 2 ]; then
    from="/tmp/alphafold"
else
    from=$2
fi
echo "extracting ${from} to ${to}"

cd $from
for folder in "$from"/*; do
    cd $folder
    cp "ranked_0.pdb" "${folder}.pdb"	
    cd ..
done
mv *.pdb $to

