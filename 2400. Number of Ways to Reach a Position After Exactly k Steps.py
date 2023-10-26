class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        MOD=1e9+7
        
        dp={}
        
        def A(currpos,k):
            if (currpos,k) in dp:
                return dp[(currpos,k)]
				
			#base case 
            if currpos==endPos and k==0:
                return 1
			#base case
            if k<=0:
                return 0
            
            
            ans1,ans2=0,0
			#move left
            ans1+=A(currpos-1,k-1)
            #move right
            ans2+=A(currpos+1,k-1)
            #sum of left + right possibilities
            dp[(currpos,k)]=(ans1+ans2)%MOD
			#return the result
            return dp[(currpos,k)]
        
        return int(A(startPos,k)%MOD)
            
            
            ```