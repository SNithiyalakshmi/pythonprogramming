# include<stdio.h>
int main()
{
	int a,b, fact=1;
	printf("enter a number /n");
	scanf("%d",&b);
	for(a=1;a<=b;a++)
	fact=fact*a;
	printf("factrial&%d=%d/n",b,fact);
	return 0;
}
