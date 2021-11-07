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

        int[][] nums = new int[][]{{2, 2}, {3, 3}};
        int ans = solution.maxCount(5,4,nums);


    }

    public int maxCount(int m, int n, int[][] ops) {

        int ans = 0;
        int m_min = m;
        int n_min = n;
        for (int []op : ops){
            if ( op[0] < m_min){
                m_min = op[0];
            }
            if ( op[1] < n_min){
                n_min = op[1];
            }
        }
        return m_min*n_min;

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