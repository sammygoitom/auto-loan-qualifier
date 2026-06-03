class DownPayment:
    def __init__(self, down_payment, budget):   # Pulling values user entered + storing them as an object
        self.down_payment = down_payment
        self.budget = budget

    # Down payment score, is based off their percent down
    def down_payment_score(self):
        percent_down = self.down_payment/self.budget * 100
        if percent_down < 10:
            return 0.2
        elif 10 <= percent_down < 15:
            return 0.4
        elif 15 <= percent_down < 20:
            return 0.6
        elif 20 <= percent_down < 25:
            return 0.8
        else:
            return 1.0

