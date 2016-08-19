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

import base64
import time
from optparse import OptionParser

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
