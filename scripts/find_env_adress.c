#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
  printf("The address is at %p\n", getenv(argv[1]));
  return (0);
}