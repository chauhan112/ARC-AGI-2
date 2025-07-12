from .tools import ArrayTools, Field, ArcQuestion,Labels
def sol_00576224(inp):
    finp = ArrayTools.flipHorizontally(inp)
    av = [Field(inp), Field(finp)]
    res = Field([])
    res.set_shape((6,6))
    for j in range(3):
        for i in range(3):
            res.place((j*2, i*2), av[j %2])
    return res

def sol_007bbfb7(inp):
    res = Field([])
    finp = Field(inp)
    res.set_shape((9,9))
    for j in range(3):
        for i in range(3):
            if inp[j][i] > 0:
                res.place((j*3, i*3), finp)
    return res

class Solver009d5c81:
    def set_question(self, question: ArcQuestion):
        self.question = question
        self.process()
    def process(self):
        from .objectedness import Main as GridMain
        valMap = {}
        for ob in self.question.question[Labels.train]:
            inp = ob[Labels.input]
            out = ob[Labels.output]
            s, _ = sorted(GridMain.get_objs(inp, True), key=lambda x: x.area)
            b = GridMain.get_objs(out, True)[0]
            valMap[s.uid] = b.value
        self.valMap = valMap
    def solve(self, inp):
        from .objectedness import Main as GridMain, GridObject
        s, b  = sorted(GridMain.get_objs(inp, True), key=lambda x: x.area)
        assert isinstance(b, GridObject), "b must be of type GridObject"
        b.replace_value(self.valMap[s.uid])
        res = Field([])

        res.set_shape(ArrayTools.shape(inp))
        res.place(b.bounding_rect[0],Field(b.rect_obj) )
        return res

def sol_00d62c1b(inp):
    grg = GridObjectGetter()
    grg.set_grid(inp)
    grg.vals_allower = lambda x: True
    objs = grg.extract_objects()
    mo =list(filter(lambda x: x.value == 0 and not x.touchesBoundry(), objs))
    for m in mo:
        m.replace_value(4)
    res = Field(inp.copy())
    for m in mo:
        res.place(m.bounding_rect[0],Field(m.rect_obj) )
    return res