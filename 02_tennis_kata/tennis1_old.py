"""
todo: ? Why the win is not printed directly winner at won_point func ?
todo: ? Not extensible if two more players are added for couple tennis
"""


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":  # todo: abstaction must be passed not hardcoded
            self.p1points += 1
        else:  # todo: make it specific
            self.p2points += 1
        # todo raise error in else case

    def score(self):
        result = ""
        temp_score = 0  # todo:  unused
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            # todo: dictionary solution for better readability and to avoid IF statements
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                result = "Advantage player1"
            elif minus_result == -1:
                result = "Advantage player2"
            elif minus_result >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):  # todo: cant even describe how bad the code in the else is
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
