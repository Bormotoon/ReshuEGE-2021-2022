#matematika
k = 0
for x in range(-50, 50):
    for y in range(-50, 50):
        if (y>1/3**0.5*x) and (y<-1/3**0.5*x+10) and (x>0):
            k += 1
print(k)
