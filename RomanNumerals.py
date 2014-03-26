class RomanNumerals:

    limits = {999: 'M', 899: 'CM', 499: 'D', 399: 'CD', 99: 'C', 89:'XC', 49:'L',39:'XL', 9:'X',4:'V'}


    def answer(self, i):
        if i == 9:
            return 'IX'
        elif i == 4:
            return 'IV'
        sortedkeys = sorted(self.limits)
        for key in reversed(sortedkeys):
            if i > key:
                return self.limits[key] + self.answer(i - (key + 1))
        return i * 'I'
