#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define STRING_LEN 5 // Length of the random string

// Function to generate a random lowercase string
void generate_random_string(char *str, int length) {
    for (int i = 0; i < length; i++) {
        str[i] = 'a' + (rand() % 26);
    }
    str[length] = '\0';
}

// Function to convert a string to hexadecimal
void string_to_hex(const char *str, char *hex) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        sprintf(hex + (i * 2), "%02x", (unsigned char)str[i]);
    }
    hex[len * 2] = '\0';
}

// Function to convert hex to Little Endian format
void convert_to_little_endian(const char *hex, char *little_endian) {
    int len = strlen(hex);
    for (int i = 0; i < len; i += 2) {
        little_endian[len - 2 - i] = hex[i];
        little_endian[len - 1 - i] = hex[i + 1];
    }
    little_endian[len] = '\0';
}

// Function to validate user input
int validate_input(const char *user_input, const char *correct) {
    return strcmp(user_input, correct) == 0;
}

// Function to print the flag if both answers are correct
void print_flag() {
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("Flag file not found!\n");
        return;
    }
    
    char flag[100];
    fgets(flag, sizeof(flag), file);
    printf("Congratulations! Here is your flag: %s\n", flag);
    fclose(file);
}

int main() {
    srand(time(NULL)); // Seed for randomness

    char original[STRING_LEN + 1], hex[STRING_LEN * 2 + 1];
    char little_endian_hex[STRING_LEN * 2 + 1], big_endian_hex[STRING_LEN * 2 + 1];
    char user_little_hex[STRING_LEN * 2 + 1], user_big_hex[STRING_LEN * 2 + 1];

    // Generate and display random string
    generate_random_string(original, STRING_LEN);
    printf("Generated String: %s\n", original);

    // Convert to hex
    string_to_hex(original, hex);

    // Convert to Little and Big Endian hex
    convert_to_little_endian(hex, little_endian_hex);
    strcpy(big_endian_hex, hex); // Big endian is the same as original hex

    // Ask user for Little Endian hex
    printf("Enter the Little Endian hex: ");
    scanf("%s", user_little_hex);

    // Validate Little Endian input
    if (!validate_input(user_little_hex, little_endian_hex)) {
        printf("Incorrect Little Endian hex! Exiting...\n");
        return 1;
    } else {
        printf("Correct Little Endian hex!\n");
    }

    // Ask user for Big Endian hex
    printf("Enter the Big Endian hex: ");
    scanf("%s", user_big_hex);

    // Validate Big Endian input
    if (!validate_input(user_big_hex, big_endian_hex)) {
        printf("Incorrect Big Endian hex! Exiting...\n");
        return 1;
    } else {
        printf("Correct Big Endian hex!\n");
    }

    // If both answers are correct, print the flag
    print_flag();

    return 0;
}
