public class Solution {
    public int solve(int[] A) 
    {
        int odd = 0;
        int even = 0;
        for(int i = 0; i<A.length; i++)
        {
            if(A[i]%2 == 0)
                even++;
            else
                odd++;
        }
        return Math.min(even, odd);
    }
}