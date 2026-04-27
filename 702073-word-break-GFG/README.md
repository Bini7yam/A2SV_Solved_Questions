# [Word Break](https://www.geeksforgeeks.org/problems/word-break1352/1)
## Medium
You are given a string s and a list dictionary[] of words. Your task is to determine whether the string s can be formed by concatenating one or more words from the dictionary[].
Note: From&nbsp;dictionary[], any word can be taken any number of times and in any order.
Examples :
Input: s&nbsp;= "ilike", dictionary[] = ["i", "like", "gfg"]Output: true
Explanation: s can be breakdown as "i like".

Input: s&nbsp;= "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: true
Explanation: s can be breakdown as "i like gfg".
Input: s&nbsp;= "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: false
Explanation: s cannot be formed using dictionary[] words.
Constraints:1 ≤ s.size() ≤ 30001 ≤ dictionary.size() ≤ 10001 ≤ dictionary[i].size() ≤ 100