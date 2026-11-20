class Solution {
    public int reverseBits(int n) {
        int ans=0;
        int curr=0;
        for (int i=0;i<32;i++)
        {
            if ((n&1)==1)
            {
                ans|=(1<<(31-i));
            }
            curr++;
            n>>=1;
        }
        return ans;
    }
}