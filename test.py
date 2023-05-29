from datetime import datetime       
aika1 = datetime(1920, 2, 14, 13, 0)
aika2 = datetime(1920, 2, 14, 13, 1)
e = aika2 - aika1                   
print(e.seconds) 