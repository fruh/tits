#!/usr/bin/python
# -*- coding: utf-8 -*-

# /*
#  * ----------------------------------------------------------------------------
#  * "THE BEER-WARE LICENSE" (Revision 42):
#  * <fruh> wrote this file.  As long as you retain this notice you
#  * can do whatever you want with this stuff. If we meet some day, and you think
#  * this stuff is worth it, you can buy me a beer in return.   Poul-Henning Kamp
#  * ----------------------------------------------------------------------------
#  */

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