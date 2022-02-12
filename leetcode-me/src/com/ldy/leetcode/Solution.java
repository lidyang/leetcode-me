package com.ldy.leetcode;

import java.util.*;

/**
 * @author lidongyang
 * @ClassName Solution.java
 * @Description TODO
 * @createTime 2021年11月06日 13:34:00
 */
class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();

//        int[][] nums = new int[][]{{2, 2}, {3, 3}};
//        int ans = solution.maxCount(5,4,nums);


        int[][] nums = new int[][]{{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}};
        int ans = solution.numEnclaves(nums);
        int i =0;


    }

    public int numEnclaves(int[][] grid) {
        int m = grid.length;
        if (m==0){
            return 0;
        }
        int n = grid[0].length;

        for(int i=0;i<n;i++){
            dfs(grid,0,i);
            dfs(grid,m-1,i);

        }
        for(int i=0;i<m;i++){

            dfs(grid,i,0);
            dfs(grid,i,n-1);

        }

        int ans = 0;
        for(int i=0; i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == 1){
                    ans++;
                }
            }
        }

        return ans;




    }
    public void dfs(int[][] grid, int i, int j){

        int m=grid.length,n=grid[0].length;
        if(i<0 || j<0 || i>=m || j>=n){
            return;
        }
        if(grid[i][j] == 0){
            return;
        }
        grid[i][j] = 0;
        dfs(grid,i-1,j);
        dfs(grid,i+1,j);
        dfs(grid,i,j-1);
        dfs(grid,i,j+1);
    }

    public String getHint(String secret, String guess) {
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        char[] secretChars = secret.toCharArray();
        char[] guessChars = guess.toCharArray();
        int count = 0;
        for(Character c : secretChars){
            if(map.containsKey(c)){
                map.replace(c,map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for(Character c : guessChars){
            if(map.containsKey(c)){
                count++;
                if(map.get(c) == 1){
                    map.remove(c);
                }else{
                    map.replace(c,map.get(c) - 1);
                }
                continue;
            }
        }
        int aNumber = 0;
        for(int i=0;i<secretChars.length;i++){
            if (secretChars[i] == guessChars[i]){
                aNumber++;
            }
        }
        int bNumber = count - aNumber;
        return aNumber+"A"+bNumber+"B";

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