
class ROW:
    # Initializing ROW instance
    def __init__(self, t):
        self.cells = t

    # ROW class methods
        
    # Method to calculate distancce to heaven
    def d2h(self, data):
        for _, col in data.cols.y:
            n = n + 1
            d = d + abs(col.heaven - col.norm(self.cells([col.at])))**2
        return (d**0.5)/(n**0.5)