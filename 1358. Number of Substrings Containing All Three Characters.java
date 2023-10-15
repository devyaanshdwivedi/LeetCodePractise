class Solution {
    public int numberOfSubstrings(String s) {
        int[] map = new int[3];
        int start = 0; int end = 0;
        int count = 0;
        while (end<s.length()) {
            char ch=s.charAt(end);
            map[ch-'a']++;
            while (allPresent(map)) {
                count += s.length() - end ;
                 // Update count for the current and future substrings
                map[s.charAt(start) - 'a']--; 
                // Reduce the count for the character at the start
                start++; // Move the start of the window forward
            }   
            end++;
        }   
        return count;
    }
    public boolean allPresent(int[] map) {
        return map[0] != 0 && map[1] != 0 && map[2] != 0;
    }
}