import math
'''Ask Josh to help you out with this code for COMP304 soon'''
class Node:
    def __init__(self, value=None, children=None, is_max_node=True, name=""):
        self.value = value
        self.children = children if children is not None else []
        self.is_max_node = is_max_node
        self.name = name # For easier debugging/visualization

    def is_leaf(self):
        return not self.children

    def evaluate_node(node):
        """
        Placeholder for your evaluation function for leaf nodes.
        For this example, it simply returns the pre-assigned value.
        """
        return node.value

    def isTerminal(node):
        return node.value is not None

    def getChildren(node):
        return node.children

    def minimax_alpha_beta(node, alpha, beta, depth=0):
        """
        Implements the Minimax algorithm with Alpha-Beta pruning.

        Args:
            node: The current Node object in the game tree.
            alpha: The alpha value (best value found so far for the maximizer).
            beta: The beta value (best value found so far for the minimizer).
            pruned_nodes: List to collect pruned nodes information.

        Returns:
            A tuple (score, path) where:
                score: The evaluated value for the node.
                path: A list of nodes representing the best path from this node.
                    Returns None if the path is pruned.
        """
        best = None
        if node.is_leaf():
            return node.evaluate_node(), None
        elif node.is_max_node:
            for c in node.children: 
                score, path = c.minimax_alpha_beta(alpha, beta, depth+1) #for MAX
                if score >= beta:
                    return score, None
                elif score > alpha:
                    alpha = score 
                    best = c.name, path
            return alpha, best
        else:
            for c in node.children:
                score, path = c.minimax_alpha_beta(alpha, beta, depth+1) #for MIN
                if score <= alpha:
                    return score, None
                elif score < beta:
                    beta = score 
                    best = c.name, path
            return beta, best
     
# Example Usage (from Figure 14.6 concept)
# Create the tree structure
# Leaf nodes (values)

min_3_2 = Node(value=2, is_max_node=False, name="Val 2")
min_3_9 = Node(value=9, is_max_node=False, name="Val 9")
min_3_8 = Node(value=8, is_max_node=False, name="Val 8")
min_3_5 = Node(value=5, is_max_node=False, name="Val 5")
min_3_3 = Node(value=3, is_max_node=False, name="Val 3")
min_3_6 = Node(value=6, is_max_node=False, name="Val 6")
min_3_7 = Node(value=7, is_max_node=False, name="Val 7")
min_3_10= Node(value=10, is_max_node=False, name="Val 10")
min_3_1 = Node(value=1, is_max_node=False, name="Val 1")

# Level 3 nodes
max_2_D = Node(children=[min_3_2, min_3_9], is_max_node=True, name="Max 2D")
max_2_E = Node(children=[min_3_8], is_max_node=True, name="Max 2E")
max_2_F = Node(children=[min_3_5, min_3_3], is_max_node=True, name="Max 2F")
max_2_G = Node(children=[min_3_6], is_max_node=True, name="Max 2G")
max_2_H = Node(children=[min_3_7, min_3_10], is_max_node=True, name="Max 2H")
max_2_I = Node(children=[min_3_1], is_max_node=True, name="Max 2I")

# Level 2 nodes
min_1_A = Node(children=[max_2_D, max_2_E], is_max_node=False, name="Min 1A")
min_1_B = Node(children=[max_2_F, max_2_G], is_max_node=False, name="Min 1B")
min_1_C = Node(children=[max_2_H, max_2_I], is_max_node=False, name="Min 1C")

# Level 1 node (root's children)
max_0 = Node(children=[min_1_A, min_1_B, min_1_C], is_max_node=True, name="Max 0") # This will be the root for this example

# Run the algorithm
initial_alpha = -math.inf
initial_beta = math.inf
pruned_nodes = []

# Let's assume Max 0 is the root of the game we are playing
root_score, root_path = max_0.minimax_alpha_beta(initial_alpha, initial_beta) # type: ignore

print(f"Root Score: {root_score}")
if root_path is not None:
    path_names_list = ["Max 0"]
    path_names_list.extend([root_path[0]])
    path_names_list.extend([root_path[1][0]])
    path_names_list.extend([root_path[1][1][0]])

    path_names = " -> ".join(path_names_list)
    print(f"Best Path: {path_names}")
else:
    print("No specific best path found")

# Print pruning information
if pruned_nodes:
    print("\n--- Pruning Information ---")
    for prune_info in pruned_nodes:
        print(prune_info)
else:
    print("\nNo pruning occurred")

print("\n--- Illustrating partial tree (if Min 1A were the root)---")
min1a_score, min1a_path = min_1_A.minimax_alpha_beta(initial_alpha, initial_beta)

print(f"Min 1A Score: {min1a_score}")
if min1a_path is not None:
    path_names_list = ["Min 1A"]
    path_names_list.extend([min1a_path[0]])
    path_names_list.extend([min1a_path[1][0]])
    path_names = " -> ".join(path_names_list)
    print(f"Best Path from Min 1A: {path_names}")
else:
    print("No specific best path found (e.g., due to pruning at this level)")

"""
---Expected Output---

Root Score: 8
Best Path: Max 0 -> Min 1A -> Max 2E -> Val 8

--- Pruning Information ---
Alpha pruning at Min 1B after Max 2F, pruned: ['Max 2G']

--- Illustrating partial tree (if Min 1A were the root) ---
Min 1A Score: 8
Best Path from Min 1A: Min 1A -> Max 2E -> Val 8
"""