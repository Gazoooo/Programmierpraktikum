factor = 10
complete = 0
x = 0

for _ in range(0,1000):
    x += 1
    if (x >= factor):
        complete += 1
        x -= factor
    
    
print(f"Mit Faktor {factor} code {complete}-mal ausgeführt.")
    
