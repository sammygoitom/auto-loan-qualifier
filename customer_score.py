class CustomerScore:
    def __init__(self, down_payment_score, credit_rating, employment_status_score, monthly_income_score,
                 finance_term_score):
        self.down_payment_score = down_payment_score
        self.credit_rating = credit_rating
        self.employment_status_score = employment_status_score
        self.monthly_income_score = monthly_income_score
        self.finance_term_score = finance_term_score

    # Assigns each category a weight based off importance, then calculates score out of 100 rounded to first decimal
    def final_customer_score(self):
        final_customer_score = ((0.35 * self.credit_rating) + (0.25 * self.down_payment_score) +
                                (0.20 * self.monthly_income_score) + (0.12 * self.employment_status_score) +
                                (0.08 * self.finance_term_score)) * 100
        return round(final_customer_score, 1)

