import matplotlib.pyplot as plt
import networkx as nx

# Parse tree structure as edges (Parent → Child)
edges = [
    ("S", "NP"), ("S", "VP"),
    ("NP", "Anne"),
    ("VP", "V"), ("VP", "NP_obj"),
    ("V", "hits"),
    ("NP_obj", "Det"), ("NP_obj", "N"),
    ("Det", "the"),
    ("N", "golf"), ("N", "ball")
]

# Directed graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Positions for nodes
pos = {
    "S": (5, 4),
    "NP": (3, 3), "VP": (7, 3),
    "Anne": (3, 2), "V": (6, 2), "NP_obj": (8, 2),
    "hits": (6, 1), "Det": (7, 1), "N": (9, 1),
    "the": (7, 0), "golf": (8, 0), "ball": (10, 0)
}

# **Fixing Colors: Making "golf" and "ball" blue (Noun)**
node_colors = {
    "S": "lightcoral",  # Root (Sentence)
    "NP": "lightblue", "VP": "lightblue",  # Phrases
    "Anne": "lightgreen", "V": "lightgreen", "NP_obj": "lightblue",  # Words/Phrases
    "hits": "yellow", "Det": "lightgray", "N": "lightblue",
    "the": "lightgray", 
    "golf": "lightblue",  # ✅ Fixed to be a noun (blue)
    "ball": "lightblue"   # ✅ Fixed to be a noun (blue)
}

# Creating color list for drawing
colors = [node_colors.get(node, "lightblue") for node in G.nodes()]

# Creating figure
fig, ax = plt.subplots(figsize=(8, 6))

# Drawing colorful tree
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=colors,
        font_size=10, font_weight="bold", edge_color="gray", arrows=False, ax=ax)

# Title
plt.title("Parse Tree for 'Anne hits the golf ball'", fontsize=14, fontweight="bold", pad=20)

# Legend at **top right**
legend_labels = {
    "lightcoral": "Root (Sentence)",
    "lightblue": "Phrases & Nouns (NP, VP, N, etc.)",  # Updated for clarity
    "lightgreen": "Subject & Verbs",
    "yellow": "Action Verb",
    "lightgray": "Determiners & Other Words"
}

# Legend
legend_patches = [plt.Line2D([0], [0], marker='o', color='w', markersize=10, 
                              markerfacecolor=color, label=label) 
                  for color, label in legend_labels.items()]

plt.legend(handles=legend_patches, loc="upper right", fontsize=10, frameon=True, title="Color Legend")

# Saving and showing
plt.savefig("parse_tree_annehitsgolfball.png", format='png', bbox_inches='tight', dpi=300)
plt.show()
