class Player:

    def __init__(self, name):
        self.name = name
        self.points = {
        "1"                : 0,
        "2"                : 0,
        "3"                : 0,
        "4"                : 0,
        "5"                : 0,
        "6"                : 0,
        "pair"             : 0,
        "two pairs"        : 0,
        "three of a kind"  : 0,
        "four of a kind"   : 0,
        "full house"       : 0,
        "small straight"   : 0,
        "large straight"   : 0,
        "yatzee"           : 0,
        "chance"           : 0
        }
        self.checklist = ["1",
                          "2",
                          "3",
                          "4",
                          "5",
                          "6",
                          "pair",
                          "two pairs",
                          "three of a kind",
                          "four of a kind",
                          "full house",
                          "small straight", 
                          "large straight",
                          "yahtzee",
                          "chance"]
    def get_score_total(self):
        s = 0
        subtotal = 0
        for p in self.points.values():
            s += p
        for r in range(1, 7):
            subtotal += self.points[str(r)]
        if r >= 63:
            s += 50
        return s
        