#%%
import sys
sys.path.insert(0, "src/rlib")
from src.rlib.LibsDB import LibsDB
exec(LibsDB.runBasic())
#%%
from src.rlib.basic import Main as ObjMaker
from src import Reader, ArcQuestion, ArrayTools, ColorMap, ArrayTools, Field, Labels, GridObject, GridMain, GridObjectGetter
from src import arc_agi as agi


train_path = r"C:\Users\rajab\Desktop\stuffs\TimeLine\2025\07_July\ARC-AGI-2\data\arc-agi_training_challenges.json"
reader = Reader(train_path)
ques = ArcQuestion(reader.data["0520fde7"])
def copyRes(sol, ind=0):
    inp = ques.get(ind, Labels.input)
    eout = sol(inp).arr.tolist()   
    ArrayTools.copy2Clipboard(eout)
def copyInp(ind=0):
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

inp = qg()
cop(inp)

# %%
i= 0
co(i)
# %%
ci(i)
# %%
objs = GridMain.get_objs(inp, True)
objs
# %%
bigObjs = [x for x in objs if x.area > 1]
# %%
bigObjs

# %%

ob = bigObjs[0]


# %%
ob.rect_obj
# %%
def replace_color(ob, colA, colB):
    ob.replace_value(color)
    return ob
def getX(size, val):
    res = []
    for i in range(size):
        row = [0] * size
        row[i] = val
        row[-1-i] = val
        res.append(row)
    return res
def getPlus(size, val):
    res = []
    for i in range(size):
        if i == size // 2:
            row = [val] * size
        else:
            row = [0] * size
            row[size//2] = val
        res.append(row)
    return res
def placer(firstPoint, arr, inst=None):
    
    inst.place(firstPoint, Field(arr))
    return inst
# %%
cop(getPlus(5, 1))
# %%
Field