#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{

if (argc!=2){

    printf("Missin coman line\n");
return 1;
}
printf("h3llo, %s\n",argv[1]);
return 0;
}