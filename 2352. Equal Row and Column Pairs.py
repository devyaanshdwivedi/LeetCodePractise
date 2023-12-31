class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        sumrow=[]
        sumcol=[]
        n=len(grid)
        for i in range(n):
            sumrow.append(sum(grid[i]))
            s=0
            for j in range(n):
                s+=grid[j][i]
            sumcol.append(s)
        
        res=0
        for i in range(n):
            for j in range(n):
                if sumrow[i]==sumcol[j]:
                    test=True
                    for k in range(n):
                        if grid[i][k]!=grid[k][j]:
                            test=False
                            break
                    if test:
                        res+=1
        return res