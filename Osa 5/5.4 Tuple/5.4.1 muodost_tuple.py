def tee_tuple(x: int, y: int, z: int):
    check = [x, y, z]
    a = min(check)
    b = max(check)
    c = sum(check)
    return(a,b,c)
        
if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))