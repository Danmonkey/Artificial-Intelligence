class State:
    name, cap, reg, seats, pop, ccases, cdeaths, fvr, mhi, vcr = 0

    def __init__(self, name, cap, reg, seats, pop, ccases, cdeaths, fvr, mhi, vcr):
        self.name = name
        self.cap = cap
        self.reg = reg
        self.seats = seats
        self.pop = pop
        self.ccases = ccases
        self.cdeaths = cdeaths
        self.fvr = fvr
        self.mhi = mhi
        self.vcr = vcr

    def get_name(self):
        return self.name

    def get_cap(self):
        return self.cap

    def get_reg(self):
        return self.reg

    def get_seats(self):
        return self.seats

    def get_pop(self):
        return self.pop

    def get_ccases(self):
        return self.ccases

    def get_cdeaths(self):
        return self.cdeaths

    def get_fvr(self):
        return self.fvr

    def get_mhi(self):
        return self.mhi

    def get_vcr(self):
        return self.vcr

    def set_name(self, name):
        self.name = name

    def set_cap(self, name):
        self.name = name

    def set_reg(self, name):
        self.name = name

    def set_seats(self, name):
        self.name = name

    def set_pop(self, name):
        self.name = name

    def set_ccases(self, name):
        self.name = name

    def set_cdeaths(self, name):
        self.name = name

    def set_fvr(self, name):
        self.name = name

    def set_mhi(self, name):
        self.name = name

    def set_vcr(self, name):
        self.name = name

    def __gt__(self, other):
        return self.get_name() > other.get_name()

    def __str__(self):
        return self.name + "    " + self.cap + "    " + self.reg + "    " + self.seats + "    " + self.pop + "    " + self.ccases + "    " + self. cdeaths + "    " + self.fvr + "    " + self.mhi + "    " + self.vcr

