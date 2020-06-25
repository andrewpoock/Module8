def in_dict(x, d):
    return x in d


if __name__ == '__main__':
    x = 'B'
    d = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    print(in_dict(x, d))
