import java.util.*;
class Solution {
    public int kthFactor(int n, int k) {
        ArrayList<Integer> arr=new ArrayList<>();
        ArrayList<Integer> brr=new ArrayList<>();
        for(int i=1;i<=Math.sqrt(n);i++)
        {
            if (n%i==0)
            {
                arr.add(i);
                if (n/i!=Math.sqrt(n)){
                brr.add(n/i);
                }
            }
        }
        
        if (k>arr.size()+brr.size())
        {
            return -1;
        }
        if (k<=arr.size())
        {
            return arr.get(k-1);
        }
        return brr.get(brr.size()-(k-arr.size()));
        
    }
}