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

        #Didn't want strong customers with 0 down or long finance term to have their scores tanked so wrote
        #this to over-ride the scoring logic
        if self.credit_rating >= 0.8 and self.monthly_income_score >= 0.8:
            final_customer_score = max(final_customer_score, 85)

        #pay in cash gets automatic 100
        if self.finance_term_score == 1:
            final_customer_score = 100

        return round(final_customer_score, 1)

