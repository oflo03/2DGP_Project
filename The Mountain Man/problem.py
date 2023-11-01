class Problem:
    def __init__(self, filename):
        self.holds = []
        with open(filename, 'r') as file:
            str = file.read()
        for ch in str:
            self.holds.append(int(ch))