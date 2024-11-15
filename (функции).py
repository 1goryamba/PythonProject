def percents (x, y):
    """What precentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    print (str (y) + " is " + str (result) + "percents of" + str (x))

    percents(200, 50)