from .tools import ArrayTools, Field
def sol_00576224(inp):
    finp = ArrayTools.flipHorizontally(inp)
    av = [Field(inp), Field(finp)]
    res = Field([])
    res.set_shape((6,6))
    for j in range(3):
        for i in range(3):
            res.place((j*2, i*2), av[j %2])
    return res

def sol_007bbfb7(inp):
    res = Field([])
    finp = Field(inp)
    res.set_shape((9,9))
    for j in range(3):
        for i in range(3):
            if inp[j][i] > 0:
                res.place((j*3, i*3), finp)
    return res

def sol_009d5c81(inp):
    res = Field([])
    finp = Field(inp)
    res.set_shape((9,9))
    for j in range(3):
        for i in range(3):
            if inp[j][i] > 0:
                res.place((j*3, i*3), finp)
    return res