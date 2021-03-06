#     1011
#     0101
#     1010
#     1101
# & = 0000
# X = 1010
class Solution:
    def count(self, N, A, X):
        bitSetinX = 0
        ans = N
        for i in range(32)[::-1]:
            if (1 << i) & X:
                bitSetinX |= (1 << i)
            else:
                temp = bitSetinX | (1 << i)
                dontMdfy = 0
                for n in A:
                    if n & temp == temp:
                        dontMdfy += 1
                ans = min(ans, N-dontMdfy)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(N, A, X)
        print(ans)
# } Driver Code Ends