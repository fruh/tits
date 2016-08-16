#!/usr/bin/python
# -*- coding: utf-8 -*-

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

import random
import base64
from optparse import OptionParser

import images

if __name__ == "__main__":
    parser = OptionParser(usage="%prog [-f] [-h] [--select-tits N] [--select-funny N]", version="%prog 0.1", description="Show random ASCII art pictures like tits 8).")
    parser.add_option("-f", "--funny", dest="funny", action="store_true",
                      help="Show random funny picture", default=False)
    parser.add_option("--select-funny", dest="select_funny", action="store",
                      help="Show Nth funny picture", type="int")
    parser.add_option("--select-tits", dest="select_tits", action="store",
                      help="Show Nth tits picture", type="int")

    (options, args) = parser.parse_args()

    if options.funny:
        print base64.decodestring(images.funlist[random.randrange(len(images.funlist))])
    elif options.select_funny:
        print base64.decodestring(images.funlist[options.select_funny % len(images.funlist)])
    elif options.select_tits:
        print base64.decodestring(images.titslist[options.select_tits % len(images.titslist)])
    else:
        print base64.decodestring(images.titslist[random.randrange(len(images.titslist))])