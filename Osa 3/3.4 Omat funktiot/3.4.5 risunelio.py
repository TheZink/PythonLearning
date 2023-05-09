def risunelio(x):
    hash = x
    while x > 0:
        print(f"#" * hash)
        x -= 1

if __name__ == "__main__":
    risunelio(5)