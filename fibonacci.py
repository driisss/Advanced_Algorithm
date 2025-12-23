
# Fibonacci with Memoization in C
# int fibonacci (int n, dp []){
#     if (n==0 || n==1){
#         return n;
#     }
#     if (dp[n] != -1){
#         return dp[n];
#     }
#     dp[n]= fib (n-1, dp) + fib (n-2, dp);

#     return dp[n];
# }


# Fibonacci with Memoization in Python
def fib(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]

# Example usage:
n = 5
dp = [-1] * (n + 1)
print(fib(n, dp))
