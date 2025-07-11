#%%
import sys
sys.path.insert(0, 'C:\\Users\\rajab\\Desktop\\cloud\\cloud\\Global\\code\\libs\\RLibs')
from timeline.t2024.arc.Viewer import ARCViewer
from src.reader import Reader

# %%
train_path = r"C:\Users\rajab\Desktop\stuffs\TimeLine\2025\07_July\ARC-AGI-2\data\arc-agi_training_challenges.json"
reader = Reader(train_path)
viewer = ARCViewer()
viewer.process.model.process.fileLoc = train_path
viewer.process.model.handlers.load()


# %%
# Question 1
from src.tools import ArcQuestion, Labels
from src.solver import sol_00576224
ques = ArcQuestion(reader.data["00576224"])
ques.verify(sol_00576224)

# %%
# Question 2
from src.tools import ArcQuestion
from src.solver import sol_007bbfb7
ques2 = ArcQuestion(reader.data["007bbfb7"])
ques2.verify(sol_007bbfb7)

# %%
# Question 3
from src.tools import ArcQuestion
from src.solver import sol_009d5c81
ques3 = ArcQuestion(reader.data["009d5c81"])
ques3.verify(sol_009d5c81)