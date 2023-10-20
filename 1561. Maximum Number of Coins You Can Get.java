class Solution {
    public int maxCoins(int[] piles) {
        int max=0;
        Arrays.sort(piles);
        int temp=piles.length/3;
        for(int i=piles.length-2;temp-- >0;i-=2){
            max+=piles[i];
        }
        return max;
    }
}