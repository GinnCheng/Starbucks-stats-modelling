class bayes_engine:
    def __init__(self, p_c, sensitivity, specitivity):
        self.p_c = p_c
        self.p_nc = 1 - p_c
        self.sensitivity = sensitivity
        self.specitivity = specitivity

    def calculate(self):
        self.p_c_pos = self.p_c * self.sensitivity
        self.p_nc_pos = self.p_nc * (1-self.specitivity)
        self.p_c_neg = self.p_c * (1-self.sensitivity)
        self.p_nc_neg = self.p_nc * self.specitivity

        self.pos_c = self.p_c_pos/(self.p_c_pos + self.p_nc_pos)
        self.pos_nc = 1 - self.pos_c

        self.neg_c = self.p_c_neg/(self.p_c_neg + self.p_nc_neg)
        self.neg_nc = 1 - self.neg_c
        return self

    def result(self):
        print(f'When positive, the probably that the result is true is {self.pos_c}')
        print(f'When positive, the probably that the result is false is {self.pos_nc}')
        print(f'When negative, the probably that the result is true is {self.neg_c}')
        print(f'When negative, the probably that the result is false is {self.neg_nc}')

if __name__ == '__main__':
    case1 = bayes_engine(p_c=0.01, sensitivity=0.9, specitivity=0.9)
    case1.calculate()
    case1.result()

