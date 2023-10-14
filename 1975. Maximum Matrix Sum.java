class Solution {
    public long maxMatrixSum(int[][] matrix) {
        // Java greedy approach
        long sum =0;
        int count =0;
        long min = Integer.MAX_VALUE;
        // we find the positive sum of all the values, 
        // if count of negative elements is odd then one element negative will be left after using the given operation
        // if count of negative elements is even then no element negative will be left after using the given operation
        for(int i =0;i<matrix.length;i++)
        {
            for(int j =0;j<matrix[0].length;j++)
            {
                if(matrix[i][j]<0)
                    count++;
                sum  += Math.abs(matrix[i][j]);
                
                if(Math.abs(matrix[i][j])<min)
                min = Math.abs(matrix[i][j]);
            }
        }
       // for even count all the negative elements can be converted to positive values  
        if(count%2 ==0)
        {
            return sum;
        }
        // for negative subtract the smallest negative element from the sum 
        return sum - 2*min;
    }
}