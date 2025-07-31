def distance_euclidienne(v1, v2):
    s = 0
    for i in range(len(v1)):
        s += (v1[i] - v2[i]) ** 2
    return s ** 0.5

def distance_manhattan(v1, v2):
    s = 0
    for i in range(len(v1)):
        s += abs(v1[i] - v2[i])
    return s

def distance_tchebychev(v1, v2):
    max_val = 0
    for i in range(len(v1)):
        d = abs(v1[i] - v2[i])
        if d > max_val:
            max_val = d
    return max_val

def distance_canberra(v1, v2):
    s = 0
    for i in range(len(v1)):
        num = abs(v1[i] - v2[i])
        den = abs(v1[i]) + abs(v2[i]) + 1e-10
        s += num / den
    return s
