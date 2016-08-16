#!/bin/bash
# This file is part of tits.
# Copyright (C) 2016 fruh

# Tits is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Tits is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

# encode all resources to base64
for f in $(find ./res/ -name '*.txt'); do cat $f | base64 -w 0 > ${f}.base64; done

# create py source
file=src/images.py
echo "#!/usr/bin/python" > $file
echo "# -*- coding: utf-8 -*-" >> $file
echo "" >> $file
echo "# This file is part of tits." >> $file
echo "# Copyright (C) 2016 fruh" >> $file
echo "" >> $file
echo "# Tits is free software: you can redistribute it and/or modify" >> $file
echo "# it under the terms of the GNU Lesser General Public License as published by" >> $file
echo "# the Free Software Foundation, either version 3 of the License, or" >> $file
echo "# (at your option) any later version." >> $file
echo "" >> $file
echo "# Tits is distributed in the hope that it will be useful," >> $file
echo "# but WITHOUT ANY WARRANTY; without even the implied warranty of" >> $file
echo "# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the" >> $file
echo "# GNU Lesser General Public License for more details." >> $file
echo "" >> $file
echo "# You should have received a copy of the GNU Lesser General Public License" >> $file
echo "# along with Foobar.  If not, see <http://www.gnu.org/licenses/>." >> $file
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