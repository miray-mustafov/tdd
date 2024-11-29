"""
todo: Questions
    use _get_players_points in every _function(maybe will make it too dependable?)
     or pass them as parameters to the functions every time like i have done now?
"""


class TennisGame1:
    POINTS_NAMES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
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
        # todo: logical to raise ValueError and make test for it ?

    def score(self):
        p1_points, p2_points = self._get_players_points()

        if p1_points == p2_points:
            return self._get_score_when_equal_points(p1_points)
        elif p1_points >= 4 or p2_points >= 4:
            return self._get_score_when_points_more_than_4(p1_points, p2_points)

        return self._get_score_when_points_less_than_4(p1_points, p2_points)

    def _get_players_points(self):
        return self.p1points, self.p2points

    def _get_score_when_equal_points(self, equal_points):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(equal_points, "Deuce")

    def _get_score_when_points_more_than_4(self, p1_points, p2_points):
        diff = p1_points - p2_points

        if abs(diff) == 1:
            return f"Advantage {self.player1_name if diff > 0 else self.player2_name}"
        if abs(diff) >= 2:
            return f"Win for {self.player1_name if diff > 0 else self.player2_name}"

        return ValueError('Any msg helper for developers ??')  # todo ?

    def _get_score_when_points_less_than_4(self, p1_points, p2_points):
        return self.POINTS_NAMES[p1_points] + '-' + self.POINTS_NAMES[p2_points]
