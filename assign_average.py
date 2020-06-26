def switch_average(x):
    switcher = {
        'A': '90',
        'B': '80',
        'C': '70',
        'D': '60',
        'F': '0',
    }
    return switcher.get(x, "Invalid input")


if __name__ == '__main__':
    print(switch_average('A'))
