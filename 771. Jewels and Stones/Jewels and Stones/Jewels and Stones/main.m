//
//  main.m
//  Jewels and Stones
//
//  Created by cm_zhaichunlin on 2019/3/18.
//  Copyright © 2019 cmcm. All rights reserved.
//

#import <Foundation/Foundation.h>

/**
 *  You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
 
 The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
 
 Example 1:
 
 Input: J = "aA", S = "aAAbbbb"
 Output: 3
 Example 2:
 
 Input: J = "z", S = "ZZ"
 Output: 0
 Note:
 
 S and J will consist of letters and have length at most 50.
 The characters in J are distinct.
 */

/**
 *  解法
 *  声明数组temp记录S中重复元素个数，下标用（字符-'A'）标记，元素为下标对应字符在S中重复个数，
    遍历S后，遍历J，根据转换，找到temp中对应下标，取出count即可。
 */
int numJewelsInStones(char* J, char* S) {
    int temp['z'-'A' + 1] = {0};
    for (int index = 0; index < strlen(S); index++) {
        int tempIndex = S[index] - 'A';
        temp[tempIndex] += 1;
    }
    
    int count = 0;
    while (*J != '\0') {
        int index = *J - 'A';
        count += temp[index];
        J++;
    }
    
    return count;
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
//        NSLog(@"Hello, World!");
        
        char *J = "z";
        char *S = "ZZZz";
        int num = numJewelsInStones(J, S);
        printf("jewels num: %d\n", num);
    }
    return 0;
}


