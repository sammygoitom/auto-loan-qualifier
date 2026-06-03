class CreditScore:
    def __init__(self, credit_score):
        self.credit_score = credit_score

    def credit_rating(self):
        if self.credit_score <= 450:
            return 0.1
        elif 450 < self.credit_score <= 550:
            return 0.2
        elif 550 < self.credit_score < 650:
            return 0.5
        elif 650 <= self.credit_score < 750:
            return 0.8
        else:
            return 1.0
