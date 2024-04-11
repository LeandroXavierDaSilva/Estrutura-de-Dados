# Crie funções que receba uma referência ao nó raiz de uma árvore binária, que armazena números inteiros, e determinam:
# 1. número de nós de forma recursiva
# 2. maior valor armazenada na árvore de forma iterativa
# 3. se um item N está armazenada na árvore binária de forma recursiva

from Node import Node
from Queue import Queue

def contagemNos(root):
    if not root:
        return 0
    return contagemNos(root.left) + contagemNos(root.right) + 1

def maiorValor(root):
    q = Queue(contagemNos(root))
    q.enqueue(root)
    max_value = root.data
    while not q.isEmpty():
        node = q.dequeue()
        if node.data > max_value:
            max_value = node.data
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)

    return max_value

def procuraN(root, n):
    if not root:
        return False
    
    return root.data == n or procuraN(root.left, n) or procuraN(root.right, n)

n = Node(1)
n.left = Node(5)
n.right = Node(11)
n.left.left = Node(4)
n.left.right = Node(9)
n.right.left = Node(21)
n.right.right = Node(8)

print(contagemNos(n))
print(maiorValor(n))
print(procuraN(n, 21))
print(procuraN(n, 7))
