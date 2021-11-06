package com.ldy.leetcode;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * @author lidongyang
 * @ClassName Solution.java
 * @Description TODO
 * @createTime 2021年11月06日 13:34:00
 */
class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums = new int[]{0,1,2,3};
        int ans = solution.missingNumber(nums);


    }


    public int missingNumber(int[] nums) {
        int ans = 0;

        for(int i:nums){
            ans = ans ^ i;
        }
        for(int i=0;i<=nums.length;i++){
            ans = ans^i;
        }

        return ans;

    }
}