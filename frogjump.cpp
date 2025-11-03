int f(int ind, vector<int> &heights, vector<int> &dp) {
    if(ind == 0) return 0;  
    // Base case: Frog is already at first stone, cost = 0

    if(dp[ind] != -1) return dp[ind];  
    // If this state is already computed, just return it (memoization)

    int left = f(ind-1, heights, dp) + abs(heights[ind] - heights[ind-1]);  
    // Case 1: Frog jumps from (ind-1) → ind

    int right = INT_MAX;  
    if(ind > 1) 
        right = f(ind-2, heights, dp) + abs(heights[ind] - heights[ind-2]);  
    // Case 2: Frog jumps from (ind-2) → ind (only if index > 1)

    return dp[ind] = min(left, right);  
    // Store and return the minimum cost
}
