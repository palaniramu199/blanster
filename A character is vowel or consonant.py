#include<stdio.h>
#include<conio.h>
int main()
{
char s;
printf("%c",&s);
scanf("%c",&s);
if( s=='a'|| s=='e' || s=='i' || s=='o' || s=='u' || s=='A' || s=='E' || s=='I' || s=='O' || s=='U')
{
 printf("vowels");
}
 else if(s=='!'|| s=='@'|| s=='#'|| s=='$' || s=='%' || s=='&')
         {
          printf("invalid");
      }
 else
 {
  printf("Consonant");
}
getch();
}
