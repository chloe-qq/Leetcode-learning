#build monotonously increasing (strictly speaking - non-decreasing) stack. 
# And then find previous less or equal value and reuse it's sum
# (trick: we add zeros to A and stack to avoid dealing with empty stack)


"""
从index i 到index j 的 subarray数量是j-i
subarrays ending with i-th value are basically same subarrays for (i-1)-th value with extra element A[i] 
added to each one of them and plus one extra subarray consisting of singular value A[i]. 
Adding same or bigger value to subarrays doesn't change their minimal values. 
Thus we can reuse previous sum and account for that extra singular subarray, thus result[i] = result[i-1] + A[i]
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [0]
        arr = [0] + arr
        N = len(arr)
        ans = [0]*N
        # 补0 防止stack 为empty，且以为体重说arr中每个数都是大于0
        
        
        N = len(arr)

        for i in range(N):
            while (arr[stack[-1]] > arr[i]):
                stack.pop()
            j = stack[-1]
            # 从index j 到i 的subarray数有i-j+1个
            # 这里算得是从index j+1 到i, 故而为i-j，这些array中最小值为stack[i]
            # 再加上ans[i]表示以index i结尾到subarry的sum
            ans[i] = ans[j] + (i-j)*arr[i]
            stack.append(i)
        return sum(ans)%(10**9+7)

