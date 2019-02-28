# Writeup 3 - Operational Security and Social Engineering

Name: Joon Park
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Joon Park

## Assignment Writeup

### Part 1 (40 pts)

pretext:I would do setup by changing the login and password found from the previous project so v0idcache and her password no longer worked. Then I would call elizabeth and tell her that I was an IT professional from the webhosting company and I noticed an irregularity on the webserver. I would ask if she had noticed anything with her login that was irregular. If not I would tell her that it seems someone had changed some of the credentials on the users and that only root users would be able to do so.
building rapport: I would direct her to a website to first check her browser thismachine.me to make sure her internet worked/check her browser version and her browser was not having issues. Then I would ask her to check her login and see if her login still worked. She will find it does not.
 She might ask what happened and I would explain that some of the user credentials had been changed in a mass edit and that we were trying to validate the real users in an attempt to purge the unauthorized users. I would then tell her that to do so I needed to validate the users listed and create a new login for them. I would need her 

-new password
-mothers maiden Name
-name of her first pet
-city she was born in
-atm pin

At this point I would change her password to the new one and she will log into the site successfully.

### Part 2 (60 pts)

Vulnerabilities:
-exposed ports: The 1337bank.money site also has some exposed ports that allowed me access into the linux shell that the webserver was running. Having open ports like the 1337bank site does leaves vulnerabilities as hackers can send anything to that port such as malicious code and that port would accept it.

-weak password: The password that you used to log into your account was listed on a list easily found on the internet and was able to be broken into in under 15 minutes. This is a huge flaw in your security as your password is one of the easiest ways hackers can steal your password and gain access to your account.

-exposed git: the 1337bank.money site has an exposed git folder which allows malicious visitors to download the source code for the site. This means anyone can download the sites code and see if there are any vulnerabilities within the code or see if prepares for other attacks. This just invites more attacks with a higher chance of being successful as they already know where to attack to be successful

What you can do to fix it
-exposed ports: The easiest method would be to establish a time to scan your network and find all open ports and close anything you can. This also requires you to know what services are running behind each port. It is also helpful to learn about your firewall and how to manage what gets through by methods such as ingress filtering. Ingress Filtering prevents malicious packets from entering your network by establishing a list of permitted source addresses. By narrowing down the list of ips that can send information to your network you prevent a lot of attacks from happening as any malicious packets get dropped. By actively monitoring ports you are also preventing attacks before they can happen as you leave no way for hackers to gain access to your network.
https://www.watchguard.com/wgrd-resource-center/security-fundamentals/what-is-a-port

https://searchnetworking.techtarget.com/definition/ingress-filtering


-weak passwords:This is one of the most common ways hackers get access to an account. A 6 letter password using all uppercase or all lowercase letters can be cracked in about 5 minutes. The best way to fix it is usually to just make a stronger password. Not to sound trite but your new password should
    -contain at least 8 characters
    -contain a mix of uppercase,lowercase,numbers,and special characters
    -should be changed every 90 days to prevent attackers from getting it

By doing so you make it infinitely harder for hackers to brute force your password unless they have a quantum computer as shown in the site below
https://cybersecurity.osu.edu/cybersecurity-you/passwords-authentication/passwords


-exposed git: By exposing your git folder you are basically giving hackers the source code to your website. This opens up numerous vulnerabilities such as exposing more vulnerabilities or exposing tokens, passwords,credentials, and new endpoints.
One way to fix it would be to disable file directory browsing or add a rule to ban access to the .git directory. The exact method will differ with the hosting server you are using but the point is simply to not expose the git repository files You could also not push any sensitive data to the git repository.
https://pentester.land/tutorials/2018/10/25/source-code-disclosure-via-exposed-git-folder.html
