import unittest
import bowling

class BowlingClass:

    def calculate_points(self, total_score):
        pin_sum = 0
        for i, pin_in_frame in enumerate(total_score):
            pin_sum += sum(pin_in_frame)
            if sum(pin_in_frame) == 10:
                pin_sum += total_score[i+1][0]
                if total_score[i+1][1] == 0:
                    pin_sum += total_score[i+2][0]
                elif pin_in_frame[0] == 10:
                    pin_sum += total_score[i+1][1]
        return pin_sum




# issue: i+2 is     pin_sum += total_score[i+2][0]
# IndexError: list index out of range