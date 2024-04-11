# Problema 03: Dada uma pilha de inteiros, reorganize os elementos em uma fila, de tal modo que os elementos da primeira metade da pilha estão intercalados com os elementos da segunda metade da pilha.

from Stack import Stack
from Queue import Queue

def Intercalar(s):
    q = Queue(s.count)

    count = s.count // 2

    for _ in range(count): q.enqueue(s.pop())

    while not s.isEmpty():
        q.enqueue(q.dequeue())
        q.enqueue(s.pop())

    return q

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pilha: ", stack)
print("Fila: ", Intercalar(stack))
