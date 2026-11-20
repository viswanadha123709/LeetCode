class Solution {
    public int minFlips(int a, int b, int c) {
        int ans=0;
        for(int i=0;i<32;i++)
        {
            int one=a&1;
            int two=b&1;
            int three=c&1;
            if((three==1) && ((one|two)==0))
            {
                ans++;
            }
            else if((three==0) && (one|two)==1){
                ans+=(one+two);
            }
            a>>=1;
            b>>=1;
            c>>=1;
        }
        return ans;
    }
}