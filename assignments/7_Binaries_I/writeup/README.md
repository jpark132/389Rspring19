# Writeup 7 - Binaries I

Name: *Joon park*
Section: *0112*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Joon park*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
printf('#include <stdio.h>

int main()
{

   int a = 485163226; // icebooda
	int b = 4277009102; //0xfeedface

	printf("a = %d\n", a);
	printf("b = %d\n", b);

	//swaps a and b
	int store = a;
	a = b;
	b = store;

	printf("a = %d\n", a);
	printf("b = %d\n", b);

   return 0;
}');
```

### Part 2 (10 Pts)

The program swaps a and b which is icebooda and feedface
