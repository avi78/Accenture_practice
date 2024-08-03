# calculate no. of two wheeler and 4 wheeler
def calculate(v,w):
    tw = (4 * v - w) / 2
    fw = v - tw
    return (tw,fw)
v,w = 200,540
print(calculate(v,w))

# output - (130.0, 70.0)