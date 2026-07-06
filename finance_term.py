class FinanceTerm:
    def __init__(self, finance_term):
        self.finance_term = finance_term

    def finance_term_score(self):
        if self.finance_term == 0:
            return 1.0
        elif self.finance_term == 12:
            return 0.9
        elif self.finance_term == 24:
            return 0.8
        elif self.finance_term == 36:
            return 0.6
        elif self.finance_term == 48:
            return 0.5
        elif self.finance_term == 60:
            return 0.3
        else:  # 72 months just gets a 0.1
            return 0.1
