


sum = 1
product = -4032

boundNumber = sum
if abs(product) > abs(sum):
    boundNumber = product

start = -abs(boundNumber)
end = abs(boundNumber)+1

for x in range(start, end):
    #print(f"\nx :  {x}\n")
    for y in range(start, end):
        #print(f"y :  {y}")
        if x + y == sum:
            if x * y == product:
                print(f"{x} & {y}")
                exit()
print("no factor numbers found")