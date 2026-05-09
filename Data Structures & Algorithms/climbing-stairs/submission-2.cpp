class Solution {
public:
    int dp[31] ;
    int help(int s, int n){
        if(s==n) return 1;
        if(s>n) return 0;
        if(dp[s]!= -1) return dp[s];
        int ans = help(s+1,n)+help(s+2,n);
        dp[s] = ans;
        return dp[s];
    }
    int climbStairs(int n) {
        for(int i = 0 ; i<31 ; i++)dp[i]=-1;
        return help(0,n);
    }
};
