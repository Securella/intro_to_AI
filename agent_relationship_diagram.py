import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def draw_task4_architecture_structured():
    """
    Diagram with manually defined layout:
      - AI Pentesting Manager (top)
      - Rule & Inference Mechanism below Manager
      - Reconnaissance, Exploitation, Privilege Escalation Agents (middle row)
      - Reporting Agent slightly below
      - Clouds (bottom)
      - Color-coded edges
      - tight_layout and a bigger figure size
    Saveing figure as 'task4_architecture_structured.png' with bbox_inches='tight'.
    """

    G = nx.DiGraph()

    # 1) Nodes
    rule_node = {"Rule & Inference Mechanism": "Central logic for rule-based decisions"}
    agents = {
        "AI Pentesting Manager":       "Coordinates tasks & learns from feedback",
        "Reconnaissance Agent":       "Scans & identifies vulnerabilities",
        "Exploitation Agent":         "Simulates attack vectors",
        "Privilege Escalation Agent": "Attempts privilege escalation",
        "Reporting Agent":            "Generates comprehensive reports"
    }
    clouds = ["Azure", "AWS", "GCP"]

    # Nodes with colors
    G.add_node("Rule & Inference Mechanism", color='gold')
    for a in agents:
        G.add_node(a, color='lightblue')
    for c in clouds:
        G.add_node(c, color='lightgray')

    # 2) Edges by color/style
    agent_to_rule = [
        ("AI Pentesting Manager",       "Rule & Inference Mechanism"),
        ("Rule & Inference Mechanism",  "AI Pentesting Manager"),

        ("Reconnaissance Agent",       "Rule & Inference Mechanism"),
        ("Rule & Inference Mechanism", "Reconnaissance Agent"),

        ("Exploitation Agent",         "Rule & Inference Mechanism"),
        ("Rule & Inference Mechanism", "Exploitation Agent"),

        ("Privilege Escalation Agent", "Rule & Inference Mechanism"),
        ("Rule & Inference Mechanism", "Privilege Escalation Agent"),

        ("Reporting Agent",            "Rule & Inference Mechanism"),
        ("Rule & Inference Mechanism", "Reporting Agent")
    ]

    agent_to_cloud = [
        ("Reconnaissance Agent",       "Azure"),
        ("Reconnaissance Agent",       "AWS"),
        ("Reconnaissance Agent",       "GCP"),

        ("Exploitation Agent",         "Azure"),
        ("Exploitation Agent",         "AWS"),
        ("Exploitation Agent",         "GCP"),

        ("Privilege Escalation Agent", "Azure"),
        ("Privilege Escalation Agent", "AWS"),
        ("Privilege Escalation Agent", "GCP"),

        ("Reporting Agent",            "Azure"),
        ("Reporting Agent",            "AWS"),
        ("Reporting Agent",            "GCP")
    ]

    feedback_loop = [
        ("Reporting Agent",       "AI Pentesting Manager"),
        ("AI Pentesting Manager", "Reporting Agent")
    ]

    def add_edges(edge_list, color, style):
        for (u, v) in edge_list:
            G.add_edge(u, v, edge_color=color, style=style)

    add_edges(agent_to_rule,  color='tab:blue',  style='solid')
    add_edges(agent_to_cloud, color='tab:green', style='solid')
    add_edges(feedback_loop,  color='tab:red',   style='dashed')

    # 3) Manual layout
    positions = {
        "AI Pentesting Manager":       (0, 4),
        "Rule & Inference Mechanism":  (0, 3),

        "Reconnaissance Agent":       (-3, 2),
        "Exploitation Agent":         (0, 2),
        "Privilege Escalation Agent": (3, 2),

        "Reporting Agent":            (0, 1),

        "Azure":                      (-2, 0),
        "AWS":                        (0, 0),
        "GCP":                        (2, 0)
    }

    color_map = [G.nodes[n].get('color', 'lightgray') for n in G.nodes()]

    # 4) Plot
    plt.figure(figsize=(14, 10))  # Larger figure
    nx.draw_networkx_nodes(G, positions, node_size=3000, node_color=color_map)
    nx.draw_networkx_labels(G, positions, font_size=9, font_weight='bold')

    for (u, v) in G.edges():
        edge_attr = G[u][v]
        nx.draw_networkx_edges(
            G,
            positions,
            edgelist=[(u, v)],
            arrows=True,
            arrowstyle='->',
            arrowsize=15,
            edge_color=edge_attr['edge_color'],
            style=edge_attr['style'],
            connectionstyle='arc3,rad=0.05'
        )

    # Agents with descriptions
    annotation_map = {**rule_node, **agents}
    for node, desc in annotation_map.items():
        x, y = positions[node]
        plt.text(
            x, y - 0.3, desc,
            fontsize=8,
            ha='center',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray')
        )

    plt.title("Rule-Driven Multi-Agent System", fontsize=12)
    plt.axis('off')

    legend_elements = [
        Line2D([0], [0], color='tab:blue',  linestyle='solid',  label='Agent ↔ Rule'),
        Line2D([0], [0], color='tab:green', linestyle='solid',  label='Agent → Cloud'),
        Line2D([0], [0], color='tab:red',   linestyle='dashed', label='Feedback Loop')
    ]
    plt.legend(handles=legend_elements, loc='lower right', fontsize=9)

    plt.tight_layout()
    plt.savefig("task4_architecture_structured.png", dpi=300, bbox_inches="tight")
    plt.show()


# Save
draw_task4_architecture_structured()
