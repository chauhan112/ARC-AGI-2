#%%
import sys
sys.path.insert(0, 'C:\\Users\\rajab\\Desktop\\cloud\\cloud\\Global\\code\\libs\\RLibs')
from timeline.t2024.arc.Viewer import ARCViewer
from src.reader import Reader
from src.tools import Labels, ArrayTools

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
from src.solver import Solver009d5c81
ques3 = ArcQuestion(reader.data["009d5c81"])
solver = Solver009d5c81()
solver.set_question(ques3)
ques3.verify(solver.solve)

# %%
# Question 4
from src.tools import ArcQuestion
from src.solver import sol_00d62c1b
ques2 = ArcQuestion(reader.data["00d62c1b"])
ques2.verify(sol_00d62c1b)

