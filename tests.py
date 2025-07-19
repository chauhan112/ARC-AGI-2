#%%


# %%
      
#    0520fde7   
#      
#  0962bcdd 
from src import Reader
train_path = r"C:\Users\rajab\Desktop\stuffs\TimeLine\2025\07_July\ARC-AGI-2\data\arc-agi_training_challenges.json"
reader = Reader(train_path)
from src import ArcQuestion
from src import arc_agi as agi
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.solverExtend import SolverExtender045e512c, Solver05269061
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.solver05a7bcf2 import Solver05a7bcf2
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.Solver0607ce86 import Solver0607ce86
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.Solver05f2a901 import Solver05f2a901
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.solver0692e18c import Solver0692e18c
from src.rlib.timeline.t2025.July.arc_agi_2.solvers.solvers import Solver_06df4c85, solve_070dd51e,solver08ed6ac7, Solver09629e4f
solvers = {
    "00576224": (False, agi.sol_00576224),
    "007bbfb7": (False, agi.sol_007bbfb7),
    "009d5c81": (True, agi.Solver009d5c81),
    "00d62c1b": (False, agi.sol_00d62c1b),
    "00dbd492": (True, agi.Solver00dbd492),
    "017c7c7b": (False, agi.Solver017c7c7b().solve),
    "025d127b": (False, agi.sol_025d127b),
    "03560426": (False, agi.sol_03560426),
    "045e512c": (False, SolverExtender045e512c().solve),
    "05269061": (False, Solver05269061().handlers.solve),
    "05a7bcf2": (False, Solver05a7bcf2().handlers.solve),
    "0607ce86": (False, Solver0607ce86().handlers.solve),
    "05f2a901": (False, Solver05f2a901().handlers.solve),
    "0692e18c": (False, Solver0692e18c().handlers.solve),
    "06df4c85": (False, Solver_06df4c85().handlers.solve),
    "070dd51e": (False, solve_070dd51e),
    "08ed6ac7": (True, lambda: solver08ed6ac7().handlers),
    "09629e4f": (False, Solver09629e4f().handlers.solve),
}
for key, (requires_question, solver) in solvers.items():
    ques = ArcQuestion(reader.data[key])
    if requires_question:
        sq = solver()
        sq.set_question(ques)
        ques.verify(sq.solve)
    else:
        ques.verify(solver)



# %%
