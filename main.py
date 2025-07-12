#%%
import sys
sys.path.insert(0, 'C:\\Users\\rajab\\Desktop\\cloud\\cloud\\Global\\code\\libs\\RLibs')
from timeline.t2024.arc.Viewer import ARCViewer
from src.reader import Reader
from src.tools import Labels, ArrayTools, Field
from src.tools import ArcQuestion, Labels

train_path = r"C:\Users\rajab\Desktop\stuffs\TimeLine\2025\07_July\ARC-AGI-2\data\arc-agi_training_challenges.json"
reader = Reader(train_path)
viewer = ARCViewer()
viewer.process.model.process.fileLoc = train_path
viewer.process.model.handlers.load()

from src.objectedness import Main as GridMain, GridObjectGetter, GridObject
ques = ArcQuestion(reader.data["00dbd492"])
# ArrayTools.copy2Clipboard(ques.get(1, Labels.output))

# %%


def copyRes(ind=0):
    inp = ques.get(ind, Labels.input)
    eout = sol_00d62c1b(inp).arr.tolist()   
    ArrayTools.copy2Clipboard(eout)
def copyInp (ind=0):
    inp = ques.get(ind, Labels.input)
    ArrayTools.copy2Clipboard(inp)
def copyOut (ind=0):
    inp = ques.get(ind, Labels.output)
    ArrayTools.copy2Clipboard(inp)

# %%
# copyres()
copyInp(1)
# %%
copyOut(1)
# %%

def sol_00dbd492(inp):
    res = Field(inp)
    
    