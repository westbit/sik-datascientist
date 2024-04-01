class PyUdvikler:
    def __init__(self):
        self.cases = []
        self.kaldenavn = "Erik Valbjrn Jensen"
        self.stedord = Stedord("Erik", "Eriks")

    def add_case(self, case):
        self.cases.append(case)


class Stedord:
    def __init__(self, grundform, ejefald):
        self.grundform = grundform
        self.ejefald = ejefald
