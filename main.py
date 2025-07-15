#%%

from src import Reader, ArcQuestion, ArrayTools, ColorMap, ArrayTools, Field, Labels, ObjMaker, GridObject, GridMain, GridObjectGetter
train_path = r"C:\Users\rajab\Desktop\stuffs\TimeLine\2025\07_July\ARC-AGI-2\data\arc-agi_training_challenges.json"
from src import arc_agi as agi
reader = Reader(train_path)

ques = ArcQuestion(reader.data["05a7bcf2"])
# ArrayTools.copy2Clipboard(ques.get(1, Labels.output))


def copyRes(sol, ind=0):
    inp = ques.get(ind, Labels.input)
    eout = sol(inp).arr.tolist()   
    ArrayTools.copy2Clipboard(eout)
def copyInp (ind=0):
    inp = ques.get(ind, Labels.input)
    ArrayTools.copy2Clipboard(inp)
def copyOut (ind=0):
    inp = ques.get(ind, Labels.output)
    ArrayTools.copy2Clipboard(inp)
def copF(f):
    cop(f.arr.tolist())
cop = ArrayTools.copy2Clipboard
ci = copyInp
co = copyOut
cr = copyRes
qg = ques.get
# %%

# %%
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.solver05a7bcf2 import Solver05a7bcf2, ToGoDirection
solver = Solver05a7bcf2()
ques = ArcQuestion(reader.data["05a7bcf2"])
ques.verify(solver.handlers.solve)

# %%
ci()
# %%
co()
# %%
ques.verify(solver.handlers.solve)
# %%
len()
# %%
cop(inp)
# %%
inp = qg()
get_objs_and_directions = solver.handlers.get_objs_and_directions
solve_down_oriented = solver.handlers.solve_down_oriented
rotx = solver.handlers.rotx
_, _, _, direction = get_objs_and_directions(inp)
rotMap = {ToGoDirection.right: 3, ToGoDirection.up: 2, ToGoDirection.left: 1, ToGoDirection.down: 0}
rot = rotMap[direction]
newArr = rotx(inp, rot)
# res = solve_down_oriented(newArr)
cop(newArr)
# %%
ci()
# %%
direction
# %%


# %%
direction
# %%
def get_direction(arr):

    get_colored_objs = solver.handlers.get_colored_objs
    get_move_direction = solver.handlers.get_move_direction
    objs = GridMain.get_objs( arr, True)
    ys,b, r = get_colored_objs(objs)
    assert len(b) == 1
    assert len(r) == 1
    b = b[0]
    r = r[0]

    from src import Vector
    obj = ys[0]
    target = b
    (x1, y1) = target.bounding_rect[0]
    (x2, y2) = target.bounding_rect[1]
    vec = Vector(x2 - x1, y2 - y1)
    (x,y), _ = obj.bounding_rect
    if vec.x > vec.y: # vertical direction
        if y < y1:
            print("right")
        else:
            print("left")
    else:
        if x < x1:
            print("down")
        else:
            print("up")
# %%
y[0].bounding_rect
# %%
cop(inp)
# %%
i = rotx(inp, 3)
cop(i)
get_direction(i)
# %%
ci()
# %%
obj.rect_obj
# %%
obj.bounding_rect
# %%
cop(i)