# [Longest Zig-Zag Sub Sequence](https://www.geeksforgeeks.org/problems/longest-zig-zag-sub-sequence2656/1)
## Hard
Given an array nums of n&nbsp;positive integers. The task is to find the longest Zig-Zag subsequence problem such that all elements of this are alternating (numsi-1 &lt; numsi &gt; numsi+1&nbsp;or numsi-1&nbsp;&gt; numsi&nbsp;&lt; numsi+1).
&nbsp;

Example 1:

Input: nums = {1,5,4}
Output: 3
Explanation: The entire sequenece is a 
Zig-Zag sequence.


Examplae 2:

Input: nums = {1,17,5,10,13,15,10,5,16,8}
Ooutput: 7
Explanation: There are several subsequences
that achieve this length. 
One is {1,17,10,13,10,16,8}.


&nbsp;

Your Task:
You don't need to read or print anyhting. Your task is to complete the function ZigZagMaxLength()&nbsp;which takes the sequence&nbsp; nums as input parameter and returns the maximum length of alternating sequence.

Expected Time Complexity:&nbsp;O(n)
Expected Space Complexity:&nbsp;O(1)

Constraints:
1 &lt;= n &lt;= 105
