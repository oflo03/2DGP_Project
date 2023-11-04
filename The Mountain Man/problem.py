from hold import Hold


def change(str, idx):
    data = int(str[idx]) * 1000
    data += int(str[idx + 1]) * 100
    data += int(str[idx + 2]) * 10
    data += int(str[idx + 3])
    return data


class Problem:
    def __init__(self, filename):
        self.holds = []
        with open(filename, 'r') as file:
            str = file.read()
        for i in range(0, len(str) // 12):
            self.holds.append(Hold(int(str[i * 12]), (change(str, i * 12 + 2), change(str, i * 12 + 7))))
