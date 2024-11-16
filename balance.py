class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


def is_balanced(expression):
    stack = Stack()
    open_brackets = {'(', '[', '{'}
    close_brackets = {')', ']', '}'}
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.isEmpty():
                return "Несбалансированно"
            if stack.peek() == bracket_pairs[char]:
                stack.pop()
            else:
                return "Несбалансированно"

    if stack.isEmpty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


# Пример использования
expression1 = "(((([{}]))))"
expression2 = "[([])((([[[]]])))]{()}"
expression3 = "{{[()]}}"
expression4 = "}{}}"
expression5 = "{{[(])]}}"
expression6 = "[[{())}]"

print(is_balanced(expression1))  # Сбалансированно
print(is_balanced(expression2))  # Сбалансированно
print(is_balanced(expression3))  # Сбалансированно
print(is_balanced(expression4))  # Несбалансированно
print(is_balanced(expression5))  # Несбалансированно
print(is_balanced(expression6))  # Несбалансированно
