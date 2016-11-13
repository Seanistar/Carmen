# 2016.11.10 - seangrit
# MovingAverage : a moving average of a sequence of numbers.
# MovingAverage(n)  constructor, where n = number of values to average over
# append(self, a)   append a to the sequence
# value(self)       average of the n most recently appended values,
#                   or all if fewer than n; None if none

class MovingAverage(object):
    # private attributes:
    # __nPoints     number of values to average over
    # __points      list of at most that many values
    # __length      length of __points, kept current
    # __value       average of values in __points [v2]
    # justification for memoizing __value:
    # value() is called much more frequently that append()

    def __init__(self, nPoints):
        self.__points = []
        self.__length = 0
        self.__nPoints = nPoints

    def append(self, newValue):
        points = self.__points
        if self.__length == self.__nPoints:
            points.pop(0)
        else:
            self.__length += 1
        points.append(newValue)
        # [v2]
        #self.__value = sum(points) / self.__length

    def value(self):
        points = self.__points
        length = self.__length
        if length > 0:
            return sum(points) / length
        else:
            return None
        # [v2]
        #if self.__length > 0: return self.__value
        #else: return None



