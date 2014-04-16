class Game:

    def calculate_points(self, game):
        score = 0
        for i, frame in enumerate(game):
            score += sum(frame)
            if i == 9:
                score += self.handle_last_frame(frame, game)
                break
            else:
                if self.is_spare(frame) and i < (len(game) - 1):
                    score += game[i+1][0]
                if self.is_strike(frame) and i < (len(game) - 2):
                    score += self.get_2_balls(i, game)
        return score

    def handle_last_frame(self, frame, game):
        # return after spare and after strike
        score = 0
        if self.is_spare(frame):
            score += game[10][0]
        if self.is_strike(frame):
            score += self.get_2_balls(9, game)
        return score

    def is_spare(self, frame):
        return frame[0] != 10 and sum(frame) == 10

    def is_strike(self, frame):
        return frame[0] == 10

    def get_2_balls(self, frame_id, game):
        sum_p = sum(game[frame_id + 1])
        if self.is_strike(game[frame_id + 1]):
            sum_p += game[frame_id + 2][0]
        return sum_p












# issue: i+2 is     total_score += total_score[i+2][0]
# IndexError: list index out of range
