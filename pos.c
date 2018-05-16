#include<stdio.h>
int main()
{
int x;
printf("Enter a number: ");
scanf("%d", &x);
 if (x < 0)
    {
            printf("You entered  a negative number");
            }
    else if(x>0)
        {
            printf("You entered a positive number");
    }
    else
    {
  printf("enter the valid number");
    }
 return 0;
}
