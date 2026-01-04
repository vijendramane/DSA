class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        # Build adjacency list for the tree
        children = [[] for _ in range(n + 1)]
        for u, v in hierarchy: s
            children[u].append(v)
        
        # Convert to 1-indexed
        present = [0] + present 
        future = [0] + future
          
        # Tree DP with knapsack optimization
        # For each node, return a dict: cost -> max_profit for that cost
        def dfs(node, parent_bought):
            # Get cost for this node 
            if parent_bought: 
                node_cost = present[node] // 2
            else:
                node_cost = present[node]
            
            node_profit = future[node] - node_cost 
            
            # If no children, return simple options
            if not children[node]:
                return {0: 0, node_cost: node_profit}
            
            # Get child options
            child_results = []
            for child in children[node]:
                options_no_buy = dfs(child, False)
                options_with_buy = dfs(child, True)
                child_results.append((options_no_buy, options_with_buy))
            
            # Option 1: Don't buy this node
            # Merge all children (with parent_bought=False)
            dp_no_buy = {0: 0}
            for options_no_buy, _ in child_results:
                new_dp = {}
                for cost1, profit1 in dp_no_buy.items():
                    for cost2, profit2 in options_no_buy.items():
                        new_cost = cost1 + cost2
                        new_profit = profit1 + profit2
                        if new_cost <= budget:
                            if new_cost not in new_dp or new_dp[new_cost] < new_profit:
                                new_dp[new_cost] = new_profit
                dp_no_buy = new_dp
            
            # Option 2: Buy this node
            # Merge all children (with parent_bought=True)
            dp_buy = {node_cost: node_profit}
            for _, options_with_buy in child_results:
                new_dp = {}
                for cost1, profit1 in dp_buy.items():
                    for cost2, profit2 in options_with_buy.items():
                        new_cost = cost1 + cost2
                        new_profit = profit1 + profit2
                        if new_cost <= budget:
                            if new_cost not in new_dp or new_dp[new_cost] < new_profit:
                                new_dp[new_cost] = new_profit
                dp_buy = new_dp
            
            # Merge both options
            result = {}
            for cost, profit in dp_no_buy.items():
                if cost not in result or result[cost] < profit:
                    result[cost] = profit
            for cost, profit in dp_buy.items():
                if cost not in result or result[cost] < profit:
                    result[cost] = profit
            
            return result
        
        # Start DFS from CEO (node 1)
        all_options = dfs(1, False)
        
        # Find maximum profit
        return max(all_options.values()) if all_options else 0


# Test cases
sol = Solution()
print("Example 1:", sol.maxProfit(2, [1,2], [4,3], [[1,2]], 3))  # Expected: 5
print("Example 2:", sol.maxProfit(2, [3,4], [5,8], [[1,2]], 4))  # Expected: 4
print("Example 3:", sol.maxProfit(3, [4,6,8], [7,9,11], [[1,2],[1,3]], 10))  # Expected: 10
print("Example 4:", sol.maxProfit(3, [5,2,3], [8,5,6], [[1,2],[2,3]], 7))  # Expected: 12
