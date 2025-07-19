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
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.moreTools import FieldPlacers
inp = qg()
cop(inp)

# %%
co()
# %%

# %%
ques.verify(Solver0520fde7().handlers.solve)