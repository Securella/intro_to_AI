import networkx as nx
import matplotlib.pyplot as plt


def draw_architecture():
    # Directed graph
    G = nx.DiGraph()

    # Agents with descriptions
    agents = {
        "AI Pentesting Manager": "Coordinates all agents",
        "Reconnaissance Agent": "Gathers cloud system data",
        "Exploitation Agent": "Simulates attack vectors",
        "Privilege Escalation Agent": "Attempts privilege escalation",
        "Reporting Agent": "Generates security reports"
    }

    # Cloud environments
    cloud_envs = ["Azure", "AWS", "GCP"]

    # Nodes to graph
    for agent in agents.keys():
        G.add_node(agent, color='lightblue')
    for env in cloud_envs:
        G.add_node(env, color='lightgray')

    # Interactions (edges)
    connections = [
        ("AI Pentesting Manager", "Reconnaissance Agent"),
        ("AI Pentesting Manager", "Exploitation Agent"),
        ("AI Pentesting Manager", "Privilege Escalation Agent"),
        ("AI Pentesting Manager", "Reporting Agent"),
        ("Reconnaissance Agent", "Azure"),
        ("Reconnaissance Agent", "AWS"),
        ("Reconnaissance Agent", "GCP"),
        ("Exploitation Agent", "Azure"),
        ("Exploitation Agent", "AWS"),
        ("Exploitation Agent", "GCP"),
        ("Privilege Escalation Agent", "Azure"),
        ("Privilege Escalation Agent", "AWS"),
        ("Privilege Escalation Agent", "GCP"),
        ("Reporting Agent", "Azure"),
        ("Reporting Agent", "AWS"),
        ("Reporting Agent", "GCP"),
        ("Reporting Agent", "AI Pentesting Manager")
    ]

    G.add_edges_from(connections)

    # Positions for agents and cloud environments
    positions = {
        "AI Pentesting Manager": (0, 3),
        "Reconnaissance Agent": (-2, 1),
        "Exploitation Agent": (0, 1),
        "Privilege Escalation Agent": (2, 1),
        "Reporting Agent": (0, -1),
        "Azure": (-3, -2),
        "AWS": (0, -2),
        "GCP": (3, -2)
    }

    # Colors for nodes
    color_map = ["lightblue" if node in agents else "lightgray" for node in G.nodes()]

    # Graph
    plt.figure(figsize=(12, 7))
    nx.draw(G, positions, with_labels=True, node_color=color_map, edge_color='gray', node_size=3500, font_size=10, font_weight='bold', arrows=True)

    # Agent descriptions (annotations)
    for agent, description in agents.items():
        plt.text(positions[agent][0], positions[agent][1] - 0.3, description, fontsize=9, ha='center', bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

    # Diagram
    plt.title("Multi-Agent System for Automated Penetration Testing")
    plt.show()


# Full architecture
draw_architecture()
