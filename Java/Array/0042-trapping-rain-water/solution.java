class Solution {
    public int trap(int[] height) {
        int n=height.length;
        int[] prefix=new int[n];
        int[] suffix=new int[n];

        int left=0;
        for(int i=0;i<n;i++)
        {
            left=Math.max(left,height[i]);
            prefix[i]=left;
        }
        int right=0;
        for(int i=n-1;i>=0;i--)
        {
            right=Math.max(right,height[i]);
            suffix[i]=right;
        }
        int count=0;
        for (int i=0;i<n;i++)
        {
            count+=Math.min(prefix[i],suffix[i])-height[i];
        }
        return count;

    }
}