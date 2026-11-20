import java.util.*;

class Solution {

    List<String> res = new ArrayList<>();

    public void f(String s, int open, int close, int n)
    {
        if(open == n && close == n)
        {
            res.add(s);
            return;
        }

        if(open < n)
        {
            f(s + "(", open + 1, close, n);
        }

        if(close < open)
        {
            f(s + ")", open, close + 1, n);
        }
    }

    public List<String> generateParenthesis(int n) 
    {
        f("", 0, 0, n);
        return res;
    }
}