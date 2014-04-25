class Game:

    def calc_score(self, game):
        score = 0
        LAST_FRAME = 9
        for i, frame in enumerate(game):
            score += sum(frame)
            if i == LAST_FRAME:
                return score + self.handle_last_frame(frame, game)
            elif self.is_spare(frame):
                    score += game[i+1][0]
            elif self.is_strike(frame):
                    score += self.get_bonus(i, game)
        return score

    def handle_last_frame(self, frame, game):
        # return after spare and after strike
        score = 0
        if self.is_spare(frame):
            score += game[10][0]
        if self.is_strike(frame):
            score += self.get_bonus(9, game)
        return score

    def is_spare(self, frame):
        return frame[0] != 10 and sum(frame) == 10

    def is_strike(self, frame):
        return frame[0] == 10

    def get_bonus(self, frame_id, game):
        bonus = sum(game[frame_id + 1])
        if self.is_strike(game[frame_id + 1]):
            bonus += game[frame_id + 2][0]
        return bonus

