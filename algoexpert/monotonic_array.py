def isMonotonic(array):
    initialized = False
    upwards = False
    downwards = False

    if len(array) == 0:
        return True

    currentMaxMin = array[0]
    for n in array[1:len(array)]:
        if n > currentMaxMin:
            if not upwards and initialized:
                return False
            else:
                upwards = True
                initialized = True

        elif n < currentMaxMin:
            if not downwards and initialized:
                return False
            else:
                downwards = True
                initialized = True

        if n > currentMaxMin and upwards:
            currentMaxMin = n
        elif n < currentMaxMin and downwards:
            currentMaxMin = n

    return True


print(isMonotonic([-1, -5, -10, -1100, -900, -1101, -1102, -9001]))
