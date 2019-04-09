#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
offset = 0
magic, version = struct.unpack("<LL", data[0:8])
offset = offset + 8
timestamp, author, section_count = struct.unpack_from("<L8sL",data,offset)
offset = offset + 16

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("Timestamp:" + datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
print("author: %s" % str(author))
print("section count: %d" % int(section_count))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

for x in range(5):
    stype, slen = struct.unpack_from("<LL", data, offset)
    offset = offset + 8
    if(slen > 0):
    ############section 0x1 #################
        if(hex(stype) == "0x1"):
            svalue = struct.unpack_from("<{}s".format(slen),data,offset)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            print("svalue: %s" % svalue)
        ############section 0x2 #################
        elif(hex(stype) == "0x2"):
            svalue = struct.unpack_from("<{}L".format(slen),data,offset)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            print("svalue: %s" % svalue)
        ############section 0x3 #################
        elif(hex(stype) == "0x3"):
            if slen/4 != len(svalue):
                print("section 0x3 not properly formatted")
                continue
            svalue = struct.unpack_from("<{}L".format(slen),data,offset)
            offset = offset + slen

            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            for word in svalue:
                print(str(word))
    ############section 0x4 #################
        elif(hex(stype) == "0x4"):
            if slen/8 != len(svalue):
                print("section 0x4 not properly formatted")
                continue
            svalue = struct.unpack_from("<{}q".format(slen),data,offset)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            for word in svalue:
                print(str(word))
    ############section 0x5 #################
        elif(hex(stype) == "0x5"):
            if slen/8 != len(svalue):
                print("section 0x5 not properly formatted")
                continue
            svalue = struct.unpack_from("<{}d".format(slen),data,offset)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            for d in svalue:
                print(float(d))
        ############section 0x6 #################
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! work on this one
        elif(hex(stype) == "0x6"):
            if slen != 16:
                print("0x6 is not properly formatted")
                continue
            svalue = struct.unpack_from("<dd",data,offset)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            print("svalue: {} {}".format(svalue[0],svalue[1]))
######################section 0x7 ##############
        elif(hex(stype) == "0x7"):
            if slen != 4:
                print("section 0x7 is not properly formatted")
                continue
            svalue = struct.unpack_from("<L",data,offset)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            print("svalue: %d" % int(svalue))
#################section 0x8#################
        elif(hex(stype) == "0x8"):
            f = open("png", "w")
            svalue = struct.unpack_from("<{}c".format(slen),data,offset)
            png_sign = " 89  50  4e  47  0d  0a  1a  0a"
            svalue = str(png_sign) + str(svalue)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            f.write(svalue)
        elif(hex(stype) == "0x9"):
            f = open("gif87", "w")
            svalue = struct.unpack_from("<{}c".format(slen),data,offset)
            g87_sign = "G I F 8 7 a"
            svalue = str(png_sign) + str(svalue)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            f.write(svalue)
        elif(hex(stype) == "0xA"):
            f = open("gif89", "w")
            svalue = struct.unpack_from("<{}c".format(slen),data,offset)
            g87_sign = "G I F 8 9 a"
            svalue = str(png_sign) + str(svalue)
            offset = offset + slen
            print("slen: %d" % int(slen))
            print("stype: %s" % hex(stype))
            f.write(svalue)
