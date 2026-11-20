class Solution {
    public int maxProfit(int[] prices) {
        int n=prices.length;
        int profit=0;
        int ans=0;
        int mini=prices[0];
        for(int i=1;i<n;i++)
        {
            if (prices[i]<mini){
                mini=prices[i];
            }
            profit=prices[i]-mini;
            ans=Math.max(profit,ans);
        }

        return ans;
    }
}