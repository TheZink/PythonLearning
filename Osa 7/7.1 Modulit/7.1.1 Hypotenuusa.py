import math
def hypotenuusa(kateetti1: float, kateetti2: float):
    answer = math.sqrt(kateetti1 ** 2 + kateetti2 ** 2)
    return answer

if __name__ == "__main__":
    print(hypotenuusa(3,4))