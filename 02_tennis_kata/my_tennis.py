# class Player:
#     def __init__(self, name, points=0):
#         self.name = name
#         self.points = points

class MyTennisGame:
    POINTS_NAMES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }
    EQUAL_POINTS_NAMES = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1
        # raise error

    def score(self):
        if self.p1points == self.p2points:
            return self.EQUAL_POINTS_NAMES.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            subtraction = self.p1points - self.p2points
            #todo: that is not solution bcs 4-1,etc possible
            # return {
            #     1: f"Advantage {self.player1_name}",
            #     -1: f"Advantage {self.player2_name}",
            #     2: f"Win for {self.player1_name}",
            # }.get(subtraction, f"Win for {self.player2_name}")

        return self.POINTS_NAMES[self.p1points] + '-' + self.POINTS_NAMES[self.p2points]
