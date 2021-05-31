class DesicionTree():
    def __init__(self, root):
        self.root = root

    def predict(self, data):
        return self.root.predict(data)


class Node():
    def __init__(self, q):
        self.question = q

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

    def predict(self, data):
        ans = self.question.ask(data)
        if ans:
            return self.left.predict(data)
        else:
            return self.right.predict(data)


class Leaf():
    def __init__(self, category):
        self.category = category

    def predict(self, data):
        return self.category


class Question():
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def ask(self, df):
        return df[self.column] < self.value
