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
cp BloqueHopp.sh ./ABLN
cp BloquePair.sh ./ABLN

cd ABLN 

echo "FIRST SCRIPT."
echo "  Make Folders Alpha and copy files inside them... "
echo

for a in {001,002,005,010,020,050,100,200,500}; do
    echo "    A$a"
    #ls
    sed -i "s/AAA/${a}/g" ParametersABLN.txt
    sed -i "s/AaA/${a}/g" BloqueHopp.sh
    sed -i "s/AaA/${a}/g" BloquePair.sh
    sed -i "s/AAA/A${a}/g" BloqueHopp.sh
    sed -i "s/AAA/A${a}/g" BloquePair.sh
    #cat ParametersABLN.txt
    for b in {01,02,05,10,20,50}; do 
        echo "        B$b"
        sed -i "s/BBB/${b}/g" ParametersABLN.txt
        sed -i "s/BbB/${b}/g" BloqueHopp.sh
        sed -i "s/BbB/${b}/g" BloquePair.sh
        sed -i "s/BBB/B${b}/g" BloqueHopp.sh
        sed -i "s/BBB/B${b}/g" BloquePair.sh
        #cat ParametersABLN.txt
        for l in {0,1,2,3,4,5}; do 
            echo "            L$l"
            sed -i "s/LLL/${l}/g" ParametersABLN.txt
            sed -i "s/LlL/${l}/g" BloqueHopp.sh
            sed -i "s/LlL/${l}/g" BloquePair.sh
            sed -i "s/LLL/L${l}/g" BloqueHopp.sh
            sed -i "s/LLL/L${l}/g" BloquePair.sh
            for n in {001,002,003,004,005,006,007,008,009,010}; do 
                sed -i "s/NNN/${n}/g" ParametersABLN.txt
                sed -i "s/NnN/${n}/g" BloqueHopp.sh
                sed -i "s/NnN/${n}/g" BloquePair.sh
                sed -i "s/NNN/N${l}/g" BloqueHopp.sh
                sed -i "s/NNN/N${l}/g" BloquePair.sh
                for x in {0,1,2,3,4}; do 
                    sed -i "s/XXX/${x}/g" ParametersABLN.txt
                    sed -i "s/XxX/${x}/g" BloqueHopp.sh
                    sed -i "s/XxX/${x}/g" BloquePair.sh
                    sed -i "s/XXX/Bloque${x}/g" BloqueHopp.sh
                    sed -i "s/XXX/Bloque${x}/g" BloquePair.sh
                    for y in $(seq $x 4); do 
                        sed -i "s/YYY/${y}/g" ParametersABLN.txt
                        sed -i "s/YyY/${y}/g" BloqueHopp.sh
                        sed -i "s/YyY/${y}/g" BloquePair.sh
                        sed -i "s/YYY/${y}/g" BloqueHopp.sh
                        sed -i "s/YYY/${y}/g" BloquePair.sh
                        
                        mkdir -p A$a/B$b/L$l/N$n/Bloque$x$y 
                        
                        cp ParametersABLN.txt ./A$a/B$b/L$l/N$n/Bloque$x$y
                        cp BloqueHopp.sh ./A$a/B$b/L$l/N$n/Bloque$x$y
                        cp BloquePair.sh ./A$a/B$b/L$l/N$n/Bloque$x$y
                        #sbatch BloqueHopp.sh
                        #sbatch BloquePair.sh
                        
                        sed -i '6 c\YYY' ParametersABLN.txt >/dev/null
                        sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/N${n}/Bloque${x}YYY" BloqueHopp.sh >/dev/null
                        sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/N${n}/Bloque${x}YYY" BloquePair.sh >/dev/null
                        sed -i "4 c\#SBATCH --job-name=H${a}${b}${l}${n}${x}YyY" BloqueHopp.sh >/dev/null
                        sed -i "4 c\#SBATCH --job-name=P${a}${b}${l}${n}${x}YyY" BloquePair.sh >/dev/null
                        done
                    sed -i '5 c\XXX' ParametersABLN.txt >/dev/null
                    sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/N${n}/XXXYYY" BloqueHopp.sh >/dev/null
                    sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/N${n}/XXXYYY" BloquePair.sh >/dev/null
                    sed -i "4 c\#SBATCH --job-name=H${a}${b}${l}${n}XxXYyY" BloqueHopp.sh >/dev/null
                    sed -i "4 c\#SBATCH --job-name=P${a}${b}${l}${n}XxXYyY" BloquePair.sh >/dev/null
                    done
                sed -i '4 c\NNN' ParametersABLN.txt >/dev/null
                sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/NNN/XXXYYY" BloqueHopp.sh >/dev/null
                sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/L${l}/NNN/XXXYYY" BloquePair.sh >/dev/null
                sed -i "4 c\#SBATCH --job-name=H${a}${b}${l}NnNXxXYyY" BloqueHopp.sh >/dev/null
                sed -i "4 c\#SBATCH --job-name=P${a}${b}${l}NnNXxXYyY" BloquePair.sh >/dev/null
                done
            sed -i '3 c\LLL' ParametersABLN.txt >/dev/null
            sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/LLL/NNN/XXXYYY" BloqueHopp.sh >/dev/null
            sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/B${b}/LLL/NNN/XXXYYY" BloquePair.sh >/dev/null
            sed -i "4 c\#SBATCH --job-name=H${a}${b}LlLNnNXxXYyY" BloqueHopp.sh >/dev/null
            sed -i "4 c\#SBATCH --job-name=P${a}${b}LlLNnNXxXYyY" BloquePair.sh >/dev/null
            done
        sed -i '2 c\BBB' ParametersABLN.txt >/dev/null
        sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/BBB/LLL/NNN/XXXYYY" BloqueHopp.sh >/dev/null
        sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/A${a}/BBB/LLL/NNN/XXXYYY" BloquePair.sh >/dev/null
        sed -i "4 c\#SBATCH --job-name=H${a}BbBLlLNnNXxXYyY" BloqueHopp.sh >/dev/null
        sed -i "4 c\#SBATCH --job-name=P${a}BbBLlLNnNXxXYyY" BloquePair.sh >/dev/null
        done
    sed -i '1 c\AAA' ParametersABLN.txt >/dev/null
    sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/AAA/BBB/LLL/NNN/XXXYYY" BloqueHopp.sh >/dev/null
    sed -i "2 c\#SBATCH -D /data3/mantilla/MultiLayerGraphene/ABLN/AAA/BBB/LLL/NNN/XXXYYY" BloquePair.sh >/dev/null
    sed -i "4 c\#SBATCH --job-name=HAaABbBLlLNnNXxXYyY" BloqueHopp.sh >/dev/null
    sed -i "4 c\#SBATCH --job-name=PAaABbBLlLNnNXxXYyY" BloquePair.sh >/dev/null
    #cat ParametersABLN.txt
    done

mkdir Seeds
mv ParametersABLN.txt ./Seeds 
mv BloqueHopp.sh ./Seeds 
mv BloquePair.sh ./Seeds 

echo "FINISHED."
