import random
from graphviz import Digraph
from IPython.display import Image, display

class MorseTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_morse_tree():
    morse_code_data = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----', ' ': ' '
    }

    root = MorseTreeNode('START')
    for char, morse_code in morse_code_data.items():
        node = root
        for dot_dash in morse_code:
            if dot_dash == '.':
                if not node.left:
                    node.left = MorseTreeNode('.')
                node = node.left
            elif dot_dash == '-':
                if not node.right:
                    node.right = MorseTreeNode('-')
                node = node.right
        node.data = char

    return root

def get_random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def visualize_morse_tree(node, graph, parent=None, code=""):
    if node:
        current_node_label = f"{node.data}\n({code})"
        color = get_random_color()
        graph.node(current_node_label, shape='circle', style='filled', fillcolor=color)

        if parent:
            label = '.' if parent.endswith('.') else '-'
            graph.edge(parent, current_node_label, label=label)

        visualize_morse_tree(node.left, graph, current_node_label, code + ".")
        visualize_morse_tree(node.right, graph, current_node_label, code + "-")


def main():
    morse_tree = build_morse_tree()
    dot = Digraph(comment='Morse Code Tree', format='png')
    dot.attr(ranksep='1', nodesep='0.5') 
    visualize_morse_tree(morse_tree, dot)
    dot.render('morse_code_tree', view=False)

    image_path = 'morse_code_tree.png'
    display_image = Image(image_path)
    display(display_image)

if __name__ == "__main__":
    main()
