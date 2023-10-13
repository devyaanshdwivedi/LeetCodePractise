class Solution {
    public int maxRotateFunction(int[] nums) {
        int sum = 0, curr = 0, max = Integer.MIN_VALUE;
        for(int i =0;i<nums.length;i++)
        {
            sum += (i*nums[i]);
            curr += nums[i];
        }
        for(int i=nums.length-1;i>=0;i--)
        {
            sum += (curr - (nums.length * nums[i]));
            max = Math.max(max, sum);
        }
        return max;
    }
}