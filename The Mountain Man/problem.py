from hold import Hold


class Problem:
    def __init__(self, filename):
        self.holds = []
        with open(filename, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                else:
                    h_type, h_x, h_y = line.split(" ")
                    self.holds.append(Hold(int(h_type), (int(h_x), int(h_y))))
