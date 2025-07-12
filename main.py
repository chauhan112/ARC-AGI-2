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

# %%
ques = ArcQuestion(reader.data["00d62c1b"])
ArrayTools.copy2Clipboard(ques.get(4, Labels.output))

# %%
ArrayTools.copy2Clipboard(ques.get(1, Labels.input))
