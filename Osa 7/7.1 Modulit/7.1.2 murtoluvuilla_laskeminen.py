from fractions import Fraction
def jaa_palasiksi(amoung: int):
    answer = []
    for time in range(amoung):
        answer.append(Fraction(1, amoung))
    return answer


if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)
    
    print()

    print(jaa_palasiksi(5))