class force:
    def __init__(self, name, rank, rifle):
        self.name = name
        self.rank = rank
        self.rifle = rifle
class personnel(force):
    def __init__(self, name, rank, rifle, ):
        force.__init__(self, name, rank, rifle)
        self.name = name
        self.rank = rank
        self.rifle = rifle
p1 = personnel("isaac", "star", "ak-47")

