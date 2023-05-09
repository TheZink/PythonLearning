def ilman_vokaaleja(mjono):
    vocals = "a" "e" "i" "o" "u" "y" "ä" "ö" "å"
    new = ""
    for i in mjono:
        if i not in vocals:
            new += i
    return new

if __name__ == "__main__":
    mjono = "abcdefghijklmnopqrstuvwxyzåäö"
    print(ilman_vokaaleja(mjono))