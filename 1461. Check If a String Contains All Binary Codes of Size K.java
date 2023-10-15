class Solution {
    public boolean hasAllCodes(String s, int k) {
       HashMap<String,Integer> hashMap = new HashMap<>();
        int totalNum = (int)Math.pow(2,k);
        for (int i=0;i<=s.length()-k;i++){
            hashMap.put(s.substring(i,i+k),1);
        }
        for (int i=0;i<totalNum;i++){
           if(!hashMap.containsKey(String.format("%" + k + "s", Integer.toBinaryString(i)).replaceAll(" ", "0"))){
               return false;
            }
        }
        return true; 
    }
}