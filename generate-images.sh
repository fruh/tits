#!/bin/bash
# /*
#  * ----------------------------------------------------------------------------
#  * "THE BEER-WARE LICENSE" (Revision 42):
#  * <fruh> wrote this file.  As long as you retain this notice you
#  * can do whatever you want with this stuff. If we meet some day, and you think
#  * this stuff is worth it, you can buy me a beer in return.   Poul-Henning Kamp
#  * ----------------------------------------------------------------------------
#  */

# encode all resources to base64
for f in $(find ./res/ -name '*.txt'); do cat $f | base64 -w 0 > ${f}.base64; done

# create py source
file=src/images.py
echo "#!/usr/bin/python" > $file
echo "# -*- coding: utf-8 -*-" >> $file
echo "" >> $file
echo "# /*" >> $file
echo "#  * ----------------------------------------------------------------------------" >> $file
echo "#  * "THE BEER-WARE LICENSE" (Revision 42):" >> $file
echo "#  * <fruh> wrote this file.  As long as you retain this notice you" >> $file
echo "#  * can do whatever you want with this stuff. If we meet some day, and you think" >> $file
echo "#  * this stuff is worth it, you can buy me a beer in return.   Poul-Henning Kamp" >> $file
echo "#  * ----------------------------------------------------------------------------" >> $file
echo "#  */" >> $file
echo "" >> $file
cat sources.txt >> $file
echo "" >> $file

# add tits
echo "titslist = [" >> $file
for f in $(find ./res/tits/ -name '*.base64'); do echo -n '"' >> $file; cat $f >> $file; echo '",' >> $file; done
sed -i '$ s/.$//' $file
echo "]" >> $file

# add fun 
echo "funlist = [" >> $file
for f in $(find ./res/fun/ -name '*.base64'); do echo -n '"' >> $file; cat $f >> $file; echo '",' >> $file; done
sed -i '$ s/.$//' $file
echo "]" >> $file