#include <stdio.h>
#include <string.h>

void copyString(char* input) {
    char buffer[10];
    strcpy(buffer, input);
    printf("Copia effettuata: %s\n", buffer);
}

int main() {
    char userInput[50];
    printf("Inserisci una stringa: ");
    fgets(userInput, 50, stdin);
    copyString(userInput);
    return 0;
}
