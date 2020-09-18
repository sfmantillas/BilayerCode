#!/bin/bash
# This script clears the terminal, displays a greeting and gives information
# about currently connected users.  The two example variables are set and displayed.

clear				# clear terminal window

echo "Hi, $USER!"		# dollar sign is used to get content of variable
echo

#FILES=02-Script.sh

if [ -d ./ABLN ]; then rm -rf ./ABLN; fi

sed '1 c\AAA' -i ParametersABLN.txt
sed '2 c\BBB' -i ParametersABLN.txt
sed '3 c\LLL' -i ParametersABLN.txt
sed '4 c\NNN' -i ParametersABLN.txt

mkdir ABLN
#xargs -a List-Files-0.txt cp -t ABLN
cp ParametersABLN.txt ./ABLN
cp HamiltonCalculator.sh ./ABLN
cp BloquePair.sh ./ABLN

cd ABLN 

echo "FIRST SCRIPT."
echo "  Make Folders Alpha and copy files inside them... "
echo

for a in {001,002,005,010}; do
    echo "    A$a"
    #ls
    sed -i "s/AAA/${a}/g" ParametersABLN.txt
    sed -i "s/AaA/${a}/g" HamiltonCalculator.sh
    #sed -i "s/AaA/${a}/g" BloquePair.sh
    sed -i "s/AAA/A${a}/g" HamiltonCalculator.sh
    #sed -i "s/AAA/A${a}/g" BloquePair.sh
    #cat ParametersABLN.txt
    for b in {01,02,05}; do 
        echo "        B$b"
        sed -i "s/BBB/${b}/g" ParametersABLN.txt
        sed -i "s/BbB/${b}/g" HamiltonCalculator.sh
        #sed -i "s/BbB/${b}/g" BloquePair.sh
        sed -i "s/BBB/B${b}/g" HamiltonCalculator.sh
        #sed -i "s/BBB/B${b}/g" BloquePair.sh
        #cat ParametersABLN.txt
        for l in {0,1,2,3}; do 
            echo "            L$l"
            sed -i "s/LLL/${l}/g" ParametersABLN.txt
            sed -i "s/LlL/${l}/g" HamiltonCalculator.sh
            #sed -i "s/LlL/${l}/g" BloquePair.sh
            sed -i "s/LLL/L${l}/g" HamiltonCalculator.sh
            #sed -i "s/LLL/L${l}/g" BloquePair.sh
            for n in {001,002,005,010}; do 
                echo "        N$n"
                sed -i "s/NNN/${n}/g" ParametersABLN.txt
                sed -i "s/NnN/${n}/g" HamiltonCalculator.sh
                #sed -i "s/NnN/${n}/g" BloquePair.sh
                sed -i "s/NNN/N${n}/g" HamiltonCalculator.sh
                #sed -i "s/NNN/N${l}/g" BloquePair.sh
                
                mkdir -p A$a/B$b/L$l/N$n
                
                cp ParametersABLN.txt ./A$a/B$b/L$l/N$n
                cp HamiltonCalculator.sh ./A$a/B$b/L$l/N$n
                cp BloquePair.sh ./A$a/B$b/L$l/N$n
                
                sed -i '4 c\NNN' ParametersABLN.txt >/dev/null
                sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/NNN" HamiltonCalculator.sh >/dev/null
                #sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/NNN" BloquePair.sh >/dev/null
                sed -i "4 c\#SBATCH --job-name=H${a}${b}${l}NnN" HamiltonCalculator.sh >/dev/null
                #sed -i "4 c\#SBATCH --job-name=P${a}${b}${l}NnN" BloquePair.sh >/dev/null
                done
            sed -i '3 c\LLL' ParametersABLN.txt >/dev/null
            sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/LLL/NNN" HamiltonCalculator.sh >/dev/null
            #sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/LLL/NNN" BloquePair.sh >/dev/null
            sed -i "4 c\#SBATCH --job-name=H${a}${b}LlLNnN" HamiltonCalculator.sh >/dev/null
            #sed -i "4 c\#SBATCH --job-name=P${a}${b}LlLNnN" BloquePair.sh >/dev/null
            done
        sed -i '2 c\BBB' ParametersABLN.txt >/dev/null
        sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/BBB/LLL/NNN" HamiltonCalculator.sh >/dev/null
        #sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/BBB/LLL/NNN" BloquePair.sh >/dev/null
        sed -i "4 c\#SBATCH --job-name=H${a}BbBLlLNnN" HamiltonCalculator.sh >/dev/null
        #sed -i "4 c\#SBATCH --job-name=P${a}BbBLlLNnN" BloquePair.sh >/dev/null
        done
    sed -i '1 c\AAA' ParametersABLN.txt >/dev/null
    sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/AAA/BBB/LLL/NNN" HamiltonCalculator.sh >/dev/null
    #sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/AAA/BBB/LLL/NNN" BloquePair.sh >/dev/null
    sed -i "4 c\#SBATCH --job-name=HAaABbBLlLNnN" HamiltonCalculator.sh >/dev/null
    #sed -i "4 c\#SBATCH --job-name=PAaABbBLlLNnN" BloquePair.sh >/dev/null
    #cat ParametersABLN.txt
    done

mkdir Seeds
mv ParametersABLN.txt ./Seeds 
mv HamiltonCalculator.sh ./Seeds 
#mv BloquePair.sh ./Seeds 

echo "FINISHED."
