def calc_treug(a, b, c):
    s = (a + b + c) / 2
    treug = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return treug