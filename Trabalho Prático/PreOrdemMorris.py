# Problema 04: Implemente o percurso em pré-ordem de uma árvore binária usando o algoritmo de Morris.

from Node import Node

def PreOrdemMorris(root):
    current = root
    while current:
        if not current.left:
            print(current.data)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current
                print(current.data)
                current = current.left

            else:
                predecessor.right = None
                current = current.right

n = Node(1)
n.left = Node(5)
n.right = Node(11)
n.left.left = Node(4)
n.left.right = Node(9)
n.right.left = Node(21)
n.right.right = Node(8)

print(PreOrdemMorris(n))
# 1 -> 5 -> 4 -> 9 -> 11 -> 21 -> 8
