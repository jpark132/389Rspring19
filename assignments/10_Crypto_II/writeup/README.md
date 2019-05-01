# Crypto II Writeup

Name: Joon Park
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Joon Park

## Assignment Writeup

### Part 1 (70 Pts)
CMSC389R-{m3ss@g3_!n_A_b0ttl3} is the message after decrypting

### Part 2 (30 Pts)

1. Both of the encrypted photos have some altering to obscure the original image. Although it seems the cipher block chaining encryption does a better job of encrypting data as the image just seems to be static and unrecognizable compared to the electronic codebook encryption in which I could still make out the original method.

2. EBC is the most basic of the encryption methods and takes 2 inputs, the message and the key and encrypts each block of data with that key. That makes it easier to find a pattern if the data is repeated and why we can see similarities to the original image in the ecb encrypted image. CBC is more secure. With CBC each block of data is dependent on the blocks of data that were encrypted before it which makes it harder to decrypt. It also uses an initialization vector to encrypt the first block (because all the other blocks are encrypted based on the first block).

*Your reflection goes here*
