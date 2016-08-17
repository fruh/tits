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
import time
from optparse import OptionParser

import images

def print_image(images_base64, index, slow):
    img = base64.decodestring(images_base64[index])

    if slow:
        img_splitted = img.split("\n")

        for l in img_splitted:
            print l
            time.sleep(0.1)
    else:
        print img


def print_all(images_base64, slow):
    for i in range(len(images_base64)):
        print "Picture #%d" % i
        print_image(images_base64, i, slow)
        print ""


if __name__ == "__main__":
    parser = OptionParser(usage="%prog [options]", version="%prog 0.2", description="""Show ASCII art pictures like tits 8). By default random tits are slowly printed, but you can select one or print funny one.""")
    parser.add_option("-f", "--funny", dest="funny", action="store_true",
                      help="Show random funny picture", default=False)
    parser.add_option("-n", "--not-slow", dest="slow", action="store_false",
                      help="Print picture immediately", default=True)
    parser.add_option("--select-funny", dest="select_funny", action="store",
                      help="Show Nth funny picture", type="int")
    parser.add_option("--select-tits", dest="select_tits", action="store",
                      help="Show Nth tits picture", type="int")
    parser.add_option("--all-tits", dest="all_tits", action="store_true",
                      help="Show all tits", default=False)
    parser.add_option("--all-funny", dest="all_funny", action="store_true",
                      help="Show all funny", default=False)

    (options, args) = parser.parse_args()

    # init random
    random.seed()

    if options.funny:
        print_image(images.funlist, random.randrange(len(images.funlist)), options.slow)
    elif options.select_funny:
        print_image(images.funlist, options.select_funny % len(images.funlist), options.slow)
    elif options.select_tits:
        print_image(images.titslist, options.select_tits % len(images.titslist), options.slow)
    elif options.all_tits:
        print_all(images.titslist, options.slow)
    elif options.all_funny:
        print_all(images.funlist, options.slow)
    else:
        print_image(images.titslist, random.randrange(len(images.titslist)), options.slow)
