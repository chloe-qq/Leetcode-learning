class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        in form of a Graph, such that there is an edge between stones that shares a row or column.
        Every time we perform union on two stones that have never been connected so far, 
        we will decrement the connected component count by one as we merge two components into one.
        减去一个就 相当于 把2个合并为一个了
        """
        N = len(stones)
        parent = [i for i in range(N)]
        size = [1 for _ in range(N)]
        def isSameRowCol(s1,s2):
            if (s1[0] == s2[0] or s1[1]==s2[1]):
                return True
            return False
        
        def find(i):
            s = stones[i]
            if (i!=parent[i]):
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            p1 = find(i)
            p2 = find(j)

            if (p1 == p2):
                return 0
            if (size[p1] > size[p2]):
                size[p1] += size[p2]
                parent[p2] = p1
            else:
                size[p2] += size[p1]
                parent[p1] = p2
            return 1
        count = N
        for i in range(N):
            for j in range(i+1, N):
                if (isSameRowCol(stones[i],stones[j])):
                    count -= union(i,j)
        return N - count
        


        

        