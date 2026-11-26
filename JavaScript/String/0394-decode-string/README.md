# [394. Decode String](https://leetcode.com/problems/decode-string/)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)
![Topics](https://img.shields.io/badge/Topics-String-informational)

## 📝 Problem Description

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Original
Python3
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"


Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"


Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

---

## 📊 Submission Details

- **Submitted On:** 11/26/2026, 3:24:14 PM
- **Language:** `String`, `Stack`, `Recursion`
- **Runtime:** N/A 
- **Memory:** N/A 

---
*Automatically pushed using **[LeetCode GitHub Auto-Sync](https://github.com)**.*
