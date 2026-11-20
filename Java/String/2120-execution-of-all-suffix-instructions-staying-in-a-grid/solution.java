import java.util.*;
class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        ArrayList<Integer> arr= new ArrayList<>();
        for(int i=0;i<s.length();i++)
        {
            int row=startPos[0];
            int col=startPos[1];
            int curr=0;
            int j=i;
            while(row<n && col<n && j<s.length())
            {
                if(s.charAt(j)=='U')
                {
                    if(row>0)
                    {
                        row--;
                        curr++;
                        j++;
                    }
                    else
                    {
                        break;
                    }
                }

                else if(s.charAt(j)=='D')
                {
                    if(row<n-1)
                    {
                        row++;
                        curr++;
                        j++;
                    }
                    else{
                        break;
                    }
                }
                
                else if(s.charAt(j)=='L')
                {
                    if(col>0)
                    {
                        col--;
                        curr++;
                        j++;
                    }
                    else
                    {
                        break;
                    }
                }

                else if(s.charAt(j)=='R')
                {
                    if(col<n-1)
                    {
                        col++;
                        curr++;
                        j++;
                    }
                    else
                    {
                        break;
                    }
                }
     
            }
            arr.add(curr);
        }
        int[] ans = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            ans[i] = arr.get(i);
        }
        return ans;
    }
    
}