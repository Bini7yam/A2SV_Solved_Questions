# [Longest Palindromic Substring](https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string1956/1)
## Medium
Given a string&nbsp;s, return the&nbsp;longest palindromic substring&nbsp;in s. If there are multiple answers,&nbsp;return the one that appears first in the given string s.
Note:&nbsp;Substring is a&nbsp;contiguous&nbsp;sequence of characters within a string, i.e. s[ i . . . . j ] where 0 ≤ i ≤ j &lt; len(s).
Examples :
Input: s = "forgeeksskeegfor"
Output: geeksskeeg
Explanation: There are several possible palindromic substrings like "kssk", "ss", "eeksskee" etc. But the substring "geeksskeeg" is the longest among all.
Input: s = "abacac"
Output: aba
Explanation: The palindromic substrings "aba", "aca" and "cac" all have the same length. Since "aba" appears first, it is the answer.
Input: s = "geeks"
Output: ee
Explanation: The longest palindromic substring present in the given string is "ee".
Constraints:1 ≤ |s| ≤ 103