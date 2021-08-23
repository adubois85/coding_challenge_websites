[665. Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/)

<br>

**Note:** LeetCode used to list this problem's difficulty as *Easy*.  It's now listed as *Medium*.

<br>

Given an array `nums` with `n` integers, your task is to check if it could become non-decreasing by modifying **at most one element**.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every `i` (**0-based**) such that (`0 <= i <= n - 2`).

<br>

**Example 1:**

```
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
```

**Example 2:**

```
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
```

<br>

**Constraints:**

+    `n == nums.length`
+    `1 <= n <= 10`<sup>`4`</sup>
+    `-10`<sup>`5`</sup>` <= nums[i] <= 10`<sup>`5`</sup>
