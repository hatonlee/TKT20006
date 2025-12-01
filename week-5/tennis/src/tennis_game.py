class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1


    def get_score(self):
        scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

        # game
        if self.player1_score >= 4 and self.player1_score - self.player2_score >= 2:
            return f"Win for {self.player1_name}"
        if self.player2_score >= 4 and self.player2_score - self.player1_score >= 2:
            return f"Win for {self.player2_name}"

        # deuce
        if self.player1_score == self.player2_score >= 3:
            return "Deuce"

        # advantage
        if self.player1_score >= 3 and self.player2_score >= 3:
            if self.player1_score == self.player2_score + 1:
                return f"Advantage {self.player1_name}"
            elif self.player2_score == self.player1_score + 1:
                return f"Advantage {self.player2_name}"

        # all
        if self.player1_score == self.player2_score < 3:
            return f"{scores[self.player1_score]}-All"

        # normal
        return f"{scores[self.player1_score]}-{scores[self.player2_score]}"
