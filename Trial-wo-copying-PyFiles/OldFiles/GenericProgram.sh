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

cd ABLN 

echo "FIRST SCRIPT."
echo "  Make Folders Alpha and copy files inside them... "
echo

for a in {001,002,005,010,020,050,100,200,500}                                                                                  #Inicio del ciclo de constantes de acoplación
    do
        echo "    A$a"
        #ls
        sed -i "s/AAA/${a}/g" ParametersABLN.txt
        #cat ParametersABLN.txt
        for b in {1,2,3,4,5}
            do 
                echo "        B$b"
                sed -i "s/BBB/${b}/g" ParametersABLN.txt
                #cat ParametersABLN.txt
                for l in {0,1,2,3,4,5}
                #for l in {0,1}
                    do
                        echo "            L$l"
                        sed -i "s/LLL/${l}/g" ParametersABLN.txt
                        for n in {001,002,003,004,005,006,007,008,009,010,015,020,025,030,035,040,045,050,060,070,080,090,100}
                        #for n in {001,002}
                            do
                                #echo "N$n"
                                sed -i "s/NNN/${n}/g" ParametersABLN.txt
                                mkdir -p A$a/B$b/L$l/N$n 
                                cp ParametersABLN.txt ./A$a/B$b/L$l/N$n
                                sed -i '4 c\NNN' ParametersABLN.txt >/dev/null
                            done
                        sed -i '3 c\LLL' ParametersABLN.txt >/dev/null
                    done
                sed -i '2 c\BBB' ParametersABLN.txt >/dev/null
            done
        sed -i '1 c\AAA' ParametersABLN.txt >/dev/null
        #cat ParametersABLN.txt
    done

mkdir Seeds
mv ParametersABLN.txt ./Seeds

echo "FINISHED."
