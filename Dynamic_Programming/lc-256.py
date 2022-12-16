# 256. Paint House
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # recursion
        self.totalLevel = len(costs)
        def find_optimal(level, choice):
            total_cost = costs[level][choice]
            if (level == self.totalLevel-1):
                pass
            elif (choice == 0):
                # red
                total_cost += min(find_optimal(level+1,1),find_optimal(level+1,2))
            elif (choice == 1):
                # red
                total_cost += min(find_optimal(level+1,0),find_optimal(level+1,2))
            elif (choice == 2):
                # red
                total_cost += min(find_optimal(level+1,1),find_optimal(level+1,0))
            return total_cost
        if (not costs):
            return 0
        return min(find_optimal(0,0),find_optimal(0,1),find_optimal(0,2))

            
    def minCost(self, costs: List[List[int]]) -> int:    
        for n in reversed(range(len(costs) - 1)):
            # Total cost of painting nth house red.
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            # Total cost of painting nth house green.
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            # Total cost of painting nth house blue.
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        if len(costs) == 0: return 0
        return min(costs[0]) # Return the minimum in the first row.