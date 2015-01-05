class RoundFloatManual(object):
    def __init__(self, value):
        assert isinstance(value, float), \
            "Value must be a float!"
        self.value = round(value, 2)

    def __str__(self):
        return "%.2f" % self.value

    __repr__ = __str__

class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        assert 0 < hr, \
            "hour should in range(0, 24)"
        assert 0 < min, \
            "minutes should in range(0, 60)"

        if min > 59:
            hr += min/60
            min %= 60

        self.hr = hr
        self.min = min

    def __str__(self):
        return "%d : %d" % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

