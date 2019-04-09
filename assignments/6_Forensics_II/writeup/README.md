# Writeup 6 - Forensics

Name: *Joon park*
Section: **

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Joon Park*

## Assignment Writeup

### Part 1 (45 Pts)

1) The IP address attacked was 142.93.136.81
2)The hackers were using nmap to find vulnerable ports on which they could access
3) The ip addresses were
	159.203.113.181
	185.199.110.153
4) the hackers were using port 20 to steal the files on the server
5)The hackers stole a picture (JPEG file)
	a. It was a picture /JPEG file
	b. The photo was taken in "The Hand, Ramble General Artigas" in Punta Del Este, Uruguay
	c. The photo was taken in 2018:12:23 at 17:16:24
	d. The camera was an Iphone 8 camera
	e. The photo was taken 4.5m below sea level

6) The attackers left the file greetz.fpff
7) The hackers were able to get very easy access to the server as the rockyou.txt password hasn't been changed. Having better security through better passwords is one way we could have prevented this attack.
### Part 2 (55 Pts)

2 i) greetz.fpff was generated on 2019-03-27 04:15:05
  ii) it was authored by fl1nch
  iii) there were 5 sections with the flag in section 4
       1 - stype: 0x1
	  	 value: hey you, keep looking :)
	  2 - stype: 0x6
	  	 value: 52.336035 4.880673
	  3 - stype: 0x8
	  	 value:
	  4 - stype: 0x1
	  	 value: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
	  5 - stype: 0x1
	  	 value: 'Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

	iv) the flag was in section 4 }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
