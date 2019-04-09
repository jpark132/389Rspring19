OSINT (Open Source Intelligence)
Assignment details
This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!

Part 1
In class you were given an online usertag: v0idcache

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about v0idcache and answer the following questions:

What is v0idcache's real name? v0idcache's real name is Eliazabeth Moffet. I was able to find this by simply searching on various social media sites. This specific piece of information was found on her twitter account.She works in the netherlands.

Where does v0idcache work? What is the URL to their website? v0idcache works at 1337bank.money which is also the url to the site. It is presumably a shady site that hacks into banks and allows you to "make money while you sleep". The physical location is listed as the Netherlands on her twitter account

List all personal information (including social media accounts, contacts, etc) you can find about v0idcache. For each, briefly detail how you discovered them. twitter handle - @v0idcache I was able to find her twitter account through just social media searching

email v0idcache@protonmail.com - this was found on the actual website 1337bank.money Most of this was just found from either googling or techniques from intel techniques as I was just trying to see if any public social media sites had any information on the user

List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information. There are 3 main ips 142.93.136.81 - this one is located in Canada 162.255.118.62 - This is located in the united states 216.87.152.33 - this is also located in the united states
went on DNS dumpster and typed in the domain 1337bank.money. This gave me information such as the location of the servers as well as multiple ips. The history has changed from time to time so I just uploaded a screenshot of the history.

List any hidden files or directories you found on this website. For full credit, list two distinct flags. I was able to find a flag located in the html
the second was in the robots.txt file -Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L} For these I just followed examples in the slides as I guessed that easter eggs from the slides would be used as problems in the hw

What ports are open on the website? What services are running behind these ports? How did you discover this?
ports open that I found were 22- this is the port that the vm is running on 80 - this is the port that the python django werkzeug service is running on 1337 - this was an open port that allowed me access to the bash shell

These ports were found using nmap and scanning each port individually. Another flag in nmap allowed for me to see what os and services that were running on each open port.

Which operating system is running on the server that is hosting the website? How did you discover this? I was able to find out that the server is running linux. I was able to find this through a flag (-A) in nmap that shows what os the server was running.

BONUS: Did you find any other flags on your OSINT mission? (Up to 9 pts!) cmsc389r- {YWX4H3d3Bz6dx9lG320dv0JZH} - AB3400.txt I found this flag after I was able to get into the server from my brute force attack. The exact file name I was able to find from a pastebin site detailing messages from v0idcache and fl1nch. The pastebin was found just by googling v0idcache. CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}- after finding more information on a dns information website(dnsdumpster) I found multiple ips, their locations and this flag text at the bottom. This was done when I was trying to find the ip so I could nmap and find vulnerable ports CMSC389R-{h1d3_s3cret_g1ts}- I found an exposed git repository using nmap and was able to download the last commit messge using 1337bank.money/.git/COMMIT_EDITMSG. I was surprised as I didn't think nmap was supposed to find git repositories or that git repositories could be vulnerable but the nmap gave me the http address and that downloaded a file which showed me the flag.

Part 2
I was able to brute force my way into the server using a very simple method. We had the wordlist which made things a lot easier as we didn't have to guess each letter individually of the password. Therefore it was simple just to iterate through the list until we got to the correct password. I made the code continue until one of the password attempts output something other than Fail although it took me a while to realize that it was outputting Fail with a newline. Still after I found out the password I found the flag in /home/flag.txt although I originally checked usr. But home is usually where the files for the user are located. I was also able to locate the AB3400.txt in /home/files/AB3400.txt. THe flag was cmsc389r-{brut3_f0rce_m4aster}

####### the git flag###############

Please enter the commit message for your changes. Lines starting
with '#' will be ignored, and an empty message aborts the commit.
Date: Wed Feb 6 22:14:25 2019 -0500
On branch master
Initial commit
Changes to be committed:
new file: pycache/init.cpython-37.pyc
new file: pycache/app.cpython-37.pyc
new file: app.py
new file: requirements.txt
new file: static/bootstrap.min.css
new file: static/bootstrap.min.js
new file: static/hackerbank.jpg
new file: static/image (2).png
new file: static/investment.jpg
new file: static/matrix.png
new file: static/product.css
new file: static/secure-bank-account.jpg
new file: static/style.css
new file: templates/404.html
new file: templates/about.html
new file: templates/auth/login.html
new file: templates/auth/register.html
new file: templates/base.html
new file: templates/index.html
new file: templates/login_flag.html
new file: templates/robots.txt
new file: templates/secret.txt
new file: templates/user.html
new file: user.py
Changes not staged for commit:
modified: pycache/app.cpython-37.pyc
modified: app.py
modified: templates/404.html
modified: templates/about.html
modified: templates/auth/login.html
modified: templates/index.html
modified: templates/secret.txt
Untracked files:
.DS_Store
static/anonymity.jpeg
