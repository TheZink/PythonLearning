def samat(a, b, c):
    if len(a) < b or len(a) < c:
        return False
    if a[b:b+1] == a[c:c+1]:
        return True
    if a[b:b+1] != a[c:c+1]:
        return False
if __name__ == "__main__":
    print(samat("koodari", 1, 2))