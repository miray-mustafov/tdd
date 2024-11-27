class TennisGame1:
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
            return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            subtraction = self.p1points - self.p2points
            result = None
            if subtraction == 1:
                result = f"Advantage {self.player1_name}"
            elif subtraction == -1:
                result = f"Advantage {self.player2_name}"
            elif subtraction >= 2:
                result = f"Win for {self.player1_name}"

            return result or f"Win for {self.player2_name}"

        points_to_word = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        return points_to_word[self.p1points] + '-' + points_to_word[self.p2points]
