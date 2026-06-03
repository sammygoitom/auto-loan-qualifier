class CarApproval:
    def __init__(self, final_customer_score, budget, down_payment, payment_method):
        self.final_customer_score = final_customer_score
        self.budget = budget
        self.down_payment = down_payment
        self.payment_method = payment_method

    def get_approval_limit(self, cars):
        final_customer_score = self.final_customer_score
        down_payment = self.down_payment
        approved = []
        manual_approval = []

        # For those paying in full, it returns the cars under their budget

        if self.payment_method == 'pay_in_full':
            for car in cars:
                if car.price <= self.budget:
                    approved.append(car)
            return approved, manual_approval

        # Candidates with strong profiles will be shown cars slightly over their budget too (little upsell)
        elif final_customer_score >= 80:
            for car in cars:
                if car.price <= self.budget + 2000:
                    approved.append(car)
            return approved, manual_approval
            # Manual_approval empty: Strong candidates qualify for anything > budget + a bit more

        # Sets max guaranteed approval limits based off customer scores
        elif 80 > final_customer_score >= 75:
            limit = int(down_payment * 6)
        elif 75 > final_customer_score >= 70:
            limit = int(down_payment * 5)
        elif 70 > final_customer_score >= 65:
            limit = int(down_payment * 4)
        elif 65 > final_customer_score >= 60:
            limit = int(down_payment * 3)
        else:
            limit = int(down_payment * 2)

        # Safe_limit takes whichever number is lower: Their budget or approved amount
        safe_limit = min(limit, self.budget)

        # Loops through cars: If budget is > than approved amount, car gets added to manual approval list
        for car in cars:
            price = car.price
            if price <= safe_limit:
                approved.append(car)
            elif price <= self.budget:
                manual_approval.append(car)
            else:
                pass
        return approved, manual_approval
