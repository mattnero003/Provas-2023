class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.depth = node.depth + 1
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                node.right.depth = node.depth + 1
            else:
                self._insert(value, node.right)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif (value < node.value and node.left is not None):
            return self._find(value, node.left)
        elif (value > node.value and node.right is not None):
            return self._find(value, node.right)

    def delete(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        """ remove a node from the tree """

        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # Case 1: node has no children
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: node has one child
        elif node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            child.parent = node_parent
        # Case 3: node has two children
        else:
            successor = min_value_node(node.right)
            node.key = successor.key
            self.delete_node(successor)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ')
            self._print_tree(node.right)

    def print_tree_postorder(self):
        if self.root is not None:
            self._print_tree_postorder(self.root)

    def _print_tree_postorder(self, node):
        if node is not None:
            self._print_tree_postorder(node.left)
            self._print_tree_postorder(node.right)
            print(str(node.value) + ' ')

    def height(self, node):
        if node is None:
            return -1
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def count_nodes(self):
        if self.root is None:
            return 0
        else:
            return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def sum_values(self):
        if self.root is None:
            return 0
        else:
            return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        else:
            return node.value + self._sum_values(node.left) + self._sum_values(node.right)

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

    def print_leaves(self):
        if self.root is not None:
            self._print_leaves(self.root)

    def _print_leaves(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.value)
            self._print_leaves(node.left)
            self._print_leaves(node.right)

    def print_non_leaves(self):
        if self.root is not None:
            self._print_non_leaves(self.root)

    def _print_non_leaves(self, node):
        if node is not None:
            if node.left is not None or node.right is not None:
                print(node.value)
            self._print_non_leaves(node.left)
            self._print_non_leaves(node.right)

    def print_depths(self):
        if self.root is not None:
            self._print_depths(self.root)

    def _print_depths(self, node):
        if node is not None:
            print(f'Node {node.value} depth: {node.depth}')
            self._print_depths(node.left)
            self._print_depths(node.right)
def menu():

    tree = BinaryTree()

    while True:
        print(
            "1. Inserir\n2. Buscar\n3. Imprimir em ordem crescente\n4. Imprimir em ordem decrescente\n5. Contar elementos\n6. Somar elementos\n7. Encontrar maior elemento\n8. Encontrar menor elemento\n9. Imprimir folhas\n10. Imprimir não folhas\n11. Remover\n12. Imprimir profundidade de cada nó\n13. Calcular altura da árvore\n14. Sair")
        option = int(input("Escolha uma opção: "))
        if option == 1:
            value = int(input("Insira o valor: "))
            tree.insert(value)
        elif option == 2:
            value = int(input("Insira o valor a ser buscado: "))
            result = tree.find(value)
            if result is not None:
                print("Valor encontrado.")
            else:
                print("Valor não encontrado.")
        elif option == 3:
            print("Árvore em ordem crescente:")
            tree.print_tree()
        elif option == 4:
            print("Árvore em ordem decrescente:")
            tree.print_tree_postorder()
        elif option == 5:
            print(f"Contagem de nós: {tree.count_nodes()}")
        elif option == 6:
            print(f"Soma dos valores: {tree.sum_values()}")
        elif option == 7:
            print(f"Maior valor: {tree.find_max()}")
        elif option == 8:
            print(f"Menor valor: {tree.find_min()}")
        elif option == 9:
            print("Folhas da árvore:")
            tree.print_leaves()
        elif option == 10:
            print("Nós não folhas:")
            tree.print_non_leaves()
        elif option == 11:
            value = int(input("Insira o valor a ser removido: "))
            tree.delete(value)
        elif option == 12:
            print("Profundidade de cada nó:")
            tree.print_depths()
        elif option == 13:
            print(f"Altura da árvore: {tree.height(tree.root)}")
        elif option == 14:
            break

def draw_tree(canvas, node, x, y, horizontal_spacing, vertical_spacing):
    if node is not None:
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, outline="black")
        canvas.create_text(x, y, text=str(node.value))

        if node.left is not None:
            x_left = x - horizontal_spacing
            y_left = y + vertical_spacing
            canvas.create_line(x, y, x_left, y_left, fill="black")
            draw_tree(canvas, node.left, x_left, y_left, horizontal_spacing / 2, vertical_spacing)

        if node.right is not None:
            x_right = x + horizontal_spacing
            y_right = y + vertical_spacing
            canvas.create_line(x, y, x_right, y_right, fill="black")
            draw_tree(canvas, node.right, x_right, y_right, horizontal_spacing / 2, vertical_spacing)

def display_tree(tree):
    window = tk.Tk()
    window.title("Binary Tree Visualization")
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    if tree.root is not None:
        draw_tree(canvas, tree.root, 400, 50, 200, 100)

    window.mainloop()

def menu():
    tree = BinaryTree()

    while True:
        print(
            "1. Inserir\n2. Buscar\n3. Imprimir em ordem crescente\n4. Imprimir em ordem decrescente\n5. Contar elementos\n6. Somar elementos\n7. Encontrar maior elemento\n8. Encontrar menor elemento\n9. Imprimir folhas\n10. Imprimir não folhas\n11. Remover\n12. Imprimir profundidade de cada nó\n13. Calcular altura da árvore\n14. Visualizar Árvore\n15. Sair")
        option = int(input("Escolha uma opção: "))
        if option == 1:
            value = int(input("Insira o valor: "))
            tree.insert(value)
        elif option == 2:
            value = int(input("Insira o valor a ser buscado: "))
            result = tree.find(value)
            if result is not None:
                print("Valor encontrado.")
            else:
                print("Valor não encontrado.")
        elif option == 3:
            print("Árvore em ordem crescente:")
            tree.print_tree()
        elif option == 4:
            print("Árvore em ordem decrescente:")
            tree.print_tree_postorder()
        elif option == 5:
            print(f"Contagem de nós: {tree.count_nodes()}")
        elif option == 6:
            print(f"Soma dos valores: {tree.sum_values()}")
        elif option == 7:
            print(f"Maior valor: {tree.find_max()}")
        elif option == 8:
            print(f"Menor valor: {tree.find_min()}")
        elif option == 9:
            print("Folhas da árvore:")
            tree.print_leaves()
        elif option == 10:
            print("Nós não folhas:")
            tree.print_non_leaves()
        elif option == 11:
            value = int(input("Insira o valor a ser removido: "))
            tree.delete(value)
        elif option == 12:
            print("Profundidade de cada nó:")
            tree.print_depths()
        elif option == 13:
            print(f"Altura da árvore: {tree.height(tree.root)}")
        elif option == 14:
            display_tree(tree)
        elif option == 15:
            break