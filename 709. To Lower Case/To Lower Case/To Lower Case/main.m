//
//  main.m
//  To Lower Case
//
//  Created by cm_zhaichunlin on 2019/3/19.
//  Copyright © 2019 cmcm. All rights reserved.
//

#import <Foundation/Foundation.h>

/**
 *  Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
 
 Example 1:
 
 Input: "Hello"
 Output: "hello"
 Example 2:
 
 Input: "here"
 Output: "here"
 Example 3:
 
 Input: "LOVELY"
 Output: "lovely"
 */

char* toLowerCase(char* str) {
    
    int interval = 'a'-'A';
    int index = 0;
    while (str[index] != '\0') {
        if ((str[index]>='A') && (str[index]<='Z')) {
            str[index] = str[index]+interval;
        }
        index++;
    }
    return str;
}

char* toLowerCaseSafe(char* str) {
    char *lowerS = malloc(strlen(str)*sizeof(char));
    strcpy(lowerS, str);
    
    int interval = 'a'-'A';
    int index = 0;
    while (lowerS[index] != '\0') {
        if ((lowerS[index]>='A') && (lowerS[index]<='Z')) {
            lowerS[index] = (char)lowerS[index]+interval;
        }
        index++;
    }
    return lowerS;
}


int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
//        NSLog(@"Hello, World!");
//        char *str = (char*)malloc(8*sizeof(char));
//        strcpy(str, "AvbFD.,D");
//        char *lowerStr = toLowerCase(str);
//        printf("lowerStr ----- %s\n", lowerStr);
        
        char *str1 = "AvbFD.,D";
        char *lowerStrSafe = toLowerCaseSafe(str1);
        printf("safe lowerStr ----- %s\n", lowerStrSafe);
    }
    return 0;
}
