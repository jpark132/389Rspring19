# Crypto II Writeup

Name: Joon Park
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Joon park

## Assignment Writeup

### Part 1 (40 Pts)

I wasn't able to finish the sql injection. My original thought process was to manipulate the field where ?id=0 in http://1337bank.money:5000/item?id=0
I tried to format the field by putting a ' and " to close the quotation and then execute the sql command to output all the passwords
1' select password from users and comment out the rest of the command with --.
This didn't work as I found out that there is a filter in place that filters out the words or and password anywhere in the field.
I tried different things like putting whitespace in between the statements to see if that would bypass the filtering /**/
using sql comments -- to try and format the rest of the string.
unfortunately none of these worked
I also tried to use different sql commands like selecting * instead of password and trying other tables that might exist but unforutnately none of those worked either.

### Part 2 (60 Pts)
Level 1 : inputting the alert script was easy as there was an input field that was really insecure. All I had to do was type a script tag in the query
Level 2: a bit harder as now we had to use events to trigger the xss injection. The hint was helpful when The script tag was escaped.
<img src = “some wrong.jpg” onerror = alert(“hi”)/> I just changed the jpg to be wrong and on the error made it run the alert function

Level3: level 3 the hints were extremely helpful but I went about it in a different way than the hints wanted me to. It wanted me to create an entirely new html object but instead I just updated the tag to include the onerror in the tag
https://xss-game.appspot.com/level3/frame#'onerror='alert("hi")'
level4:
This was kind of annoying but I had to find the exact way how the input was parsed and ended up just being able to execute the alert function by omitting a pair of single quotes ex: 
3');+alert('hi

Level 5:
I noticed that next would be executed and that during the signup site it would be set to confirm. I just changed that to the ahref form javascript:alert(hi) and submitted a bs email and it worked
javascript:alert(hi)
it did take me a while to realize I had to reload the page to get my new function loaded

level 6: This gamespot thing takes way too much time. But the last hint gave me the idea of it. By using a callback function and putting that in place of the gadget url we can have the level 6 call alert on itself
www.google.com/jsapi?callback=alert


