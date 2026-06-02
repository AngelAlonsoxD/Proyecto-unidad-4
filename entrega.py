class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def peek(self):
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

p = Pila()

p.push(10)
p.push(20)
p.push(30)

print(p.peek())      # 30
print(p.pop())       # 30
print(p.esta_vacia())# False