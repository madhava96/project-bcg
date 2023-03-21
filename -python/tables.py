with open("f.txt" , "w") as f:
    for i in range(1, 51):
        for j in range(1, 11):
            f.write('{} x {} = {}\n' .format(i,j,i*j))
        f.write("\n")
f.close()
with open('f.txt','r') as f:
    s = f.readlines()[-2]
print(s)
