#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open('hashes.txt','r').readlines()
    passwords = open('passwords.txt','r').readlines()
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            c=c.strip()
            p=p.strip()
            input = c+p
            hash = hashlib.sha256(input.encode())
            for h in hashes:
                if(hash.hexdigest() == h.strip()):
                    print(input+":"+hash.hexdigest())



            # print hashes as 'input:hash
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
