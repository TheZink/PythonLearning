def anagrammi(a,b):
    if sorted(a) == sorted(b):
        return (True)
    else:
        return (False)

if __name__ == "__main__":
    kutsu = anagrammi("talo", "tloa")
    print(kutsu)
