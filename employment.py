class Employment:
    def __init__(self, employment_status, monthly_income):
        self.employment_status = employment_status
        self.monthly_income = monthly_income

    def employment_status_score(self):
        if self.employment_status == 1:  # 1 represents employed full time
            return 1.0
        elif self.employment_status == 2:  # Employed Part Time
            return 0.5
        elif self.employment_status == 3:  # Student
            return 0.2
        else:
            return 0.1  # Unemployed

    # I could have separated the two, but for their relation and simplicity, decided to combine it
    def monthly_income_score(self):
        if self.monthly_income >= 15000:
            return 1.0
        elif self.monthly_income >= 10000:
            return 0.8
        elif self.monthly_income >= 7000:
            return 0.7
        elif self.monthly_income >= 4000:
            return 0.55
        else:
            return 0.1
