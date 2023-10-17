//Finding repetition in array using hashmap
//if a repetition is found then we calculate the length or 
//number of cards we hab to pick to get that repetition
//Maintain another variable to store min length
//VOILAAAAA...
class Solution {
    public int minimumCardPickup(int[] cards) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int ans = Integer.MAX_VALUE;

        for(int i=0; i<cards.length; i++){

            if(map.containsKey(cards[i])){
            int idx = map.get(cards[i]);
                int res = i - idx + 1;
                ans = Math.min(ans, res);
            }

            map.put(cards[i], i);
        }
        return ans==Integer.MAX_VALUE ?-1 :ans;
    }
}