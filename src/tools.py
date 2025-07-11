import numpy as np
class Labels:
    train ="train"
    test = "test"
    input="input"
    output="output"

class ArcQuestion:
    def __init__(self, question):
        self.question = question
    def shape(self,idx=0, inputOrOutput= Labels.input):
        return len(self.question[Labels.train][idx][inputOrOutput]), len(self.question["train"][idx][inputOrOutput][0])
    def get(self,idx=0, inputOrOutput= Labels.input):
        return self.question[Labels.train][idx][inputOrOutput]
    def verify(self, solver):
        assert len(self.question[Labels.train]) >= 1
        for ob in self.question[Labels.train]:
            res = solver(ob[Labels.input])
            assert res.isEqual(Field(ob[Labels.output])), (ob[Labels.output], res.get())
    def getTestOutput(self, solver):
        return [solver(ob[Labels.input]) for ob in self.question[Labels.test]]

class ArrayTools:
    def flipVertically(arr):
        return arr[::-1]
    def flipHorizontally(arr):
        res = np.array(arr)[:, ::-1]
        return res.tolist()

class Field:
    def __init__(self, arr):
        self.arr = np.array(arr, dtype=int)
    def shape(self):
        return self.arr.shape
    def place(self, firstPoint, arr):
        assert isinstance(firstPoint, tuple), "firstPoint must be of type tuple"
        assert isinstance(arr, Field), "arr must be of type Field"
        sx,sy = arr.shape()
        x,y = firstPoint
        for i in range(sx):
            for j in range(sy):
                self.arr[x+i][y+j] = arr.arr[i][j]
    def copy(self):
        return Field(self.arr.tolist.copy())
    
    def set_shape(self, shape):
        self.arr = np.zeros(shape, dtype=int)
    def get(self):
        return self.arr.tolist()
    def isEqual(self, other):
        assert isinstance(other, Field), "other must be of type Field"
        self.shape() == other.shape()
        return (self.arr == other.arr).all()