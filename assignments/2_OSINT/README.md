OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

1. What is `v0idcache`'s real name?
	v0idcache's real name is Eliazabeth Moffet. I was able to find this by simply searching on various social media sites. This specific piece of information was found on her twitter account.She works in the netherlands.

2. Where does `v0idcache` work? What is the URL to their website?
v0idcache works at 1337bank.money which is also the url to the site. It is presumably a shady site that hacks into banks and allows you to "make money while you sleep". The physical location is listed as the Netherlands on her twitter account

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.
twitter handle - @v0idcache I was able to find her twitter account through just social media searching 

email v0idcache@protonmail.com - this was found on the actual website 1337bank.money

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
There are 3 main ips
142.93.136.81 - this one is located in Canada
162.255.118.62 - This is located in the united states
216.87.152.33 - this is also located in the united states

 went on DNS dumpster and typed in the domain 1337bank.money. This gave me information such as the location of the servers as well as multiple ips. The history has changed from time to time so I just uploaded a screenshot of the history.

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.
I was able to find a flag located in the html 
<!-- Good find! CMSC389R-{h1dd3n_1n_plain_5ight} --> 
the second was in the robots.txt file -Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

6. What ports are open on the website? What services are running behind these ports? How did you discover this?

ports open that I found were 
22- this is the port that the vm is running on 
80 - this is the port that the python django werkzeug service is running on
1337 - this was an open port that allowed me access to the bash shell

These ports were found using nmap and scanning each port individually. Another flag in nmap allowed for me to see what os and services that were running on each open port.

7. Which operating system is running on the server that is hosting the website? How did you discover this?
I was able to find out that the server is running linux. I was able to find this through a flag (-A) in nmap that shows what os the server was running

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
cmsc389r- {YWX4H3d3Bz6dx9lG320dv0JZH} - AB3400.txt I found this flag after I was able to get into the server from my brute force attack

CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}- after finding more information on a dns information website(dnsdumpster) I found multiple ips, their locations and this flag text


### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.

Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
