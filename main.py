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


# %%
co()
# %%


# %%


# %%
cop(solver.handlers.rotx(go.rect_obj, 3))

# %%


# %%
solver = Solver05a7bcf2()
inp = reader.data["05a7bcf2"]["test"][0]["input"]
res = solver.handlers.solve(inp)
copF(res)
# %%
ci()
# %%
co()
# %%
ques.getTestOutput(solve)
# %%
len()
# %%
cop(reader.data["05a7bcf2"]["test"][0]["input"])
# %%
