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


//        int[][] nums = new int[][]{{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}};
//        int ans = solution.numEnclaves(nums);

//        int ans = solution.countOperations(2,3);
        int[] nums = new int[] {3,1,3,2,4,3};
        int ans = solution.minimumOperations(nums);
        System.out.println(ans);
        int i =0;
        "qsd".toCharArray()



    }

    public String repeatLimitedString(String s, int repeatLimit) {

        int[]  count  = new int[26];
        for(char c: s.toCharArray()){
            count[c-'a']++;
        }
        int i = 25;
        int c = 0;
        StringBuilder sb = new StringBuilder();
        while(true){
            while(i >= 0 && count[i] == 0){
                i--;
            }
            if(i < 0) {
                break;
            }
            while(count[i]>0 && c < repeatLimit){
                count[i]--;
                c++;
                sb.append((char)('a'+i));
            }
            c=0;
            if(count[i] == 0){
                continue;
            }
            else{
                int j = i-1;
                while(j>=0 && count[j] == 0){
                    j--;
                }
                if(j<0) {
                    break;
                }
                sb.append((char)('a'+j));
                count[j]--;
            }
        }
        return sb.toString();
    }





    public List<Long> maximumEvenSplit(long finalSum) {
        List<Long> ans = new ArrayList();
        if (finalSum % 2 == 0){
            long now = 2;
            while(finalSum >0){
                if (finalSum < now){
                    ans[ans.size()-1] += finalSum;
                    break;
                }else{
                    ans.add(now);
                    finalSum = finalSum - now;
                    now =now+2;
                }

            }
        }
        return ans;

    }


    public long[] sumOfThree(long num) {
        if(num%3 != 0){
            return new long[]{};
        }
        long ans = num/3;
//        long res[] =  new long[3];
//        res = new long[]{ans - 1, ans, ans + 1};
//        return res;

        return  new long[]{ans - 1, ans, ans + 1};

    }


    public int countPairs(int[] nums, int k) {
        int ans = 0;
        int len = nums.length;
        for (int i=0;i<len;i++){
            for(int j=i+1;j<len;j++){
                if((nums[i] == nums[j]) && i*j%k==0){
                    ans++;
                }
            }
        }
        return ans;

    }

    public long minimumRemoval(int[] beans) {
        int ans = Integer.MAX_VALUE;
        Arrays.sort(beans);
        for(int i=beans.length-1;i>=0;i--){
            int temp = 0;
            for(int j=0;j<beans.length;j++){
                if(beans[j]>=beans[i]) {
                    temp += beans[j] - beans[i];
                    if(temp > ans || temp<0){
                        break;
                    }
                } else{
                    temp += beans[j];
                    if(temp > ans || temp<0){
                        break;
                    }
                }
            }
            if(temp>=0 && temp<ans ){
                ans =  temp;
            }
        }
        return ans;

    }

    public int minimumOperations(int[] nums) {
        Map<Integer, Integer> map1 = new HashMap<Integer, Integer>();
        Map<Integer, Integer>map2 = new HashMap<Integer, Integer>();
        int maxNum1 = 0;
        int key1 =nums[0];
        int key2 = nums[1];
        int maxNum2 = 0;

        for (int i=0;i<nums.length;i++){
            if(i%2==0){
                map1.put(nums[i], map1.getOrDefault(nums[i],0)+1);
                if(map1.get(nums[i]) > maxNum1){
                    maxNum1 = map1.get(nums[i]);
                    key1=nums[i];
                }
            }else{
                map2.put(nums[i], map2.getOrDefault(nums[i],0)+1);
                if(map2.get(nums[i]) > maxNum2){
                    maxNum2 = map2.get(nums[i]);
                    key2 = nums[i];
                }
            }
        }

        int ans = 0;
        if(key1 == key2){

        }
        else{
            ans = nums.length-maxNum1-maxNum2;
        }

        return



    }

    public int countOperations(int num1, int num2) {

        int ans = 0;
        while (num1!=0 && num2!=0){
            if(num1>num2){
                num1 = num1-num2;
                ans++;
            } else{
                num2=num2-num1;
                ans++;
            }
        }
        return ans;

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