#include <stdio.h>
#include <stdlib.h>

int asciivalue(char asciichar){
int asci_val;

asci_val = atoi(asciichar);

return asci_val;
}

int main() {
  char print_char;
  int asci_char;
  
  print_char = 'z';
  
  asci_char = asciivalue(print_char);
  
  printf("character: %c", print_char);
  
  printf("asci value: %d", asci_char);
  
  return 0;
}