#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

commands=('../c/main ../cpp/main')
files=('fs.txt')
ks=('5')
for command in $commands;
do
    for f in $files;
    do
        for k in $ks;
        do
            #printf "/usr/bin/time -v -a performance "$command" "$f" "$k" >> out""\n"
            #eval $("/usr/bin/time -v -o ./time -a "$command" "$f" "$k" >> ./out")
            echo -e $command" "$f" "$k"\n" >> ./out
            echo -e $command" "$f" "$k"\n" >> ./time
            cmd="/usr/bin/time -v -o ./time -a "$command" "$f" "$k" >> ./out"
            eval "$cmd"
            echo -e "\n\n" >> ./out
            echo -e "\n\n" >> ./time
            #$command" "$f" "$k)
        done
    done
done