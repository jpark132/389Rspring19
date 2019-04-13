/*
 * Name: *Joon Park*
 * Section: *0112*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Joon park*
 */

/* your code goes here */

#include <stdio.h>

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
}
