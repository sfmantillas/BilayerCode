#!/bin/bash
# This script clears the terminal, displays a greeting and gives information
# about currently connected users.  The two example variables are set and displayed.

clear				# clear terminal window

echo "Hi, $USER!"		# dollar sign is used to get content of variable
echo

#FILES=02-Script.sh

if [ -d ./ABLN ]; then rm -rf ./ABLN; fi

mkdir ABLN
#xargs -a List-Files-0.txt cp -t ABLN
#cp 02-Script.sh /.ABLN

cd ABLN 

echo "FIRST SCRIPT."
echo "  Make Folders Alpha and copy files inside them... "
echo


mkdir A0.01
xargs -a List-Files-A.txt cp -t A0.01
#echo "    A0.01"
mkdir A0.02
xargs -a List-Files-A.txt cp -t A0.02
#echo "    A0.02"
mkdir A0.05
xargs -a List-Files-A.txt cp -t A0.05
#echo "    A0.05"

mkdir A0.10
xargs -a List-Files-A.txt cp -t A0.10
#echo "    A0.10"
mkdir A0.20

xargs -a List-Files-A.txt cp -t A0.20
#echo "    A0.20"
mkdir A0.50

xargs -a List-Files-A.txt cp -t A0.50
#echo "    A0.50"

mkdir A1.00
xargs -a List-Files-A.txt cp -t A1.00
#echo "    A1.00"
mkdir A2.00
xargs -a List-Files-A.txt cp -t A2.00
#echo "    A2.00"
mkdir A5.00
xargs -a List-Files-A.txt cp -t A5.00
#echo "    A5.00"

#FilesToBeingCopied=02-Script.sh

echo "  Folders done and filled."
echo

cd A0.01
sed -i 's/vermin/pony/g' metamorphosis.txt
echo "  In A0.01 running 02-Script.sh"
echo
./02-Script.sh
cd ..

cd A0.02
echo "  In A0.02 running 02-Script.sh"
echo
./02-Script.sh
cd ..

cd A0.05
echo "  In A0.05 running 02-Script.sh"
echo
./02-Script.sh
cd ..


cd A0.10
echo "  In A0.10 running 02-Script.sh"
echo
./02-Script.sh
cd ..

cd A0.20
echo "  In A0.20 running 02-Script.sh"
echo
./02-Script.sh
cd ..

cd A0.50
echo "  In A0.50 running 02-Script.sh"
echo
./02-Script.sh
cd ..


cd A1.00
echo "  In A1.00 running 02-Script.sh"
echo
./02-Script.sh
cd ..

cd A2.00
echo "  In A2.00 running 02-Script.sh"
echo
./02-Script.sh
cd ..

cd A5.00
echo "  In A5.00 running 02-Script.sh"
echo
./02-Script.sh
cd ..

echo "ARCHIVER DONE"


#echo "I will now fetch you a list of connected users:"
#echo							
#w				# show who is logged on and
#echo				# what they are doing

#echo "I'm setting two variables now."
#COLOUR="black"					# set a local shell variable
#VALUE="9"					# set a local shell variable
#echo "This is a string: $COLOUR"		# display content of variable 
#echo "And this is a number: $VALUE"		# display content of variable
#echo

#echo "I'm giving you back your prompt now."
#echo
