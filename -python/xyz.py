import random

column = input("No of Column: ")
rows = input("No of Rows: ")
randomDataList = random.sample(range(10,99), int(column)* int(rows))

print(randomDataList)
createMatrix(int(column), int(rows), randomDataList)
