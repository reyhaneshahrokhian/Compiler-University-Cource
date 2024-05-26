import networkx as nx


class PostOrderASTTraverser:
    def __init__(self):
        self.node_attributes = ['label']

    def __add_to_graph(self, graph, node, parent=None):
        if node is not None:
            # Add the current node to the graph
            graph.add_node(node.number, label=node.value)
            # If there's a parent, add an edge from the parent to the current node
            if parent is not None:
                graph.add_edge(parent.number, node.number)
            # add the child nodes to the graph
            for child in node.children:
                self.__add_to_graph(graph, child, node)

    def traverse_ast(self, ast_root_node):
        graph = nx.DiGraph()
        self.__add_to_graph(graph, ast_root_node)
        post_order_traversal = []
        for node in nx.dfs_postorder_nodes(graph, source=ast_root_node.number):
            node_object_in_traversal = {}
            for node_attribute in self.node_attributes:
                node_object_in_traversal[node_attribute] = graph.nodes[node].get(node_attribute)

            post_order_traversal.append(node_object_in_traversal)

        return post_order_traversal
