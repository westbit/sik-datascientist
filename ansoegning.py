class PyUdvikler:
    def __init__(self):
        self.cases = []
        self.kaldenavn = "Erik Valbjørn Jensen"
        self.stedord = Stedord("Erik", "Eriks")


class Stedord:
    def __init__(self, grundform, ejefald):
        self.grundform = grundform
        self.ejefald = ejefald
