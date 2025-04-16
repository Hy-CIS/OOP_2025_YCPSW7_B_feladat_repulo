class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        print(f"\n{self.nev} légitársaság járatai:")
        for jarat in self.jaratok:
            print(jarat)
