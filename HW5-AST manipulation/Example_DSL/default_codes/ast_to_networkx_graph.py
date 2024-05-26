import networkx as nx


# Function to add nodes and edges to the NetworkX graph
def add_to_graph(graph, node, parent=None):
    if node is not None:
        # Add the current node to the graph
        graph.add_node(node.number, label=node.value)
        # If there's a parent, add an edge from the parent to the current node
        if parent is not None:
            graph.add_edge(parent.number, node.number)
        # add the child nodes to the graph
        for child in node.children:
            add_to_graph(graph, child, node)


def transform_ast_to_networkx(ast_root_node):
    graph = nx.DiGraph()
    add_to_graph(graph,ast_root_node)
    return graph


def show_ast(ast_root_node):
    from matplotlib import pyplot as plt
    from networkx.drawing.nx_pydot import graphviz_layout

    graph = transform_ast_to_networkx(ast_root_node)

    options = {
        "font_size": 12,
        "node_size": 500,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 1,
        "width": 1,
    }

    import pydot
    pos = graphviz_layout(graph, prog="dot")
    nx.draw(graph, pos, node_size=500, labels=nx.get_node_attributes(graph, "label"), alpha=0.5, node_color="cyan",
            with_labels=True)
    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()

