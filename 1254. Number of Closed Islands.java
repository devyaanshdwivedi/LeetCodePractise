class Solution {
    static int[] dir = new int[]{1,0,-1,0,1};
    public int closedIsland(int[][] grid) {

        ArrayDeque<int[]> dq = new ArrayDeque<>();
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==0){
                    dq.add(new int[]{i,j});
                    boolean flag = true;
                    while(!dq.isEmpty()){
                        int[] t = dq.poll();
                        if(t[0]==0 || t[0]==grid.length-1 || t[1]==0 || t[1]==grid[0].length-1)
                            flag = false;
                            grid[t[0]][t[1]]=3;
                            for(int k=1;k<dir.length;k++){
                                int a = t[0]+dir[k-1];
                                int b = t[1]+dir[k];
                                if(a<0 || a>=grid.length || b<0 || b>=grid[0].length || grid[a][b]>=1)
                                    continue;
                                dq.add(new int[]{a,b});
                            }
                    }
                    if(flag){
                        count++;
                    }
                }
            }
        }

        return count;
    }
}