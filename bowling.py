class BowlingGame:

    def calculate_points(self, pint_hits_in_game):
        total_score = 0
        for i, pin_hits_in_frame in enumerate(pint_hits_in_game):
            total_score += sum(pin_hits_in_frame)
            if self.is_spare(pin_hits_in_frame) and i < (len(pint_hits_in_game) - 1):
                total_score += pint_hits_in_game[i+1][0]
            if self.is_strike(pin_hits_in_frame) and i < (len(pint_hits_in_game) - 2):
                total_score += pint_hits_in_game[i+1][0]
                if self.is_strike(pint_hits_in_game[i+1]):
                    total_score += pint_hits_in_game[i+2][0]
                else:
                    total_score += pint_hits_in_game[i+1][1]
        return total_score

    def is_spare(self, pin_hits_in_frame):
        is_spare = False
        if pin_hits_in_frame[0] != 10 and sum(pin_hits_in_frame) == 10:
            is_spare = True
        return is_spare

    def is_strike(self, pin_hits_in_frame):
        is_strike = False
        if pin_hits_in_frame[0] == 10:
            is_strike = True
        return is_strike


    # problem: 11th frame we add pin hits and the bonus









# issue: i+2 is     total_score += total_score[i+2][0]
# IndexError: list index out of range
