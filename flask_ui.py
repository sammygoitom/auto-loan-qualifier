from flask import Flask, request, render_template
from credit_score import CreditScore
from cars import cars
from down_payment import DownPayment
from employment import Employment
from finance_term import FinanceTerm
from customer_score import CustomerScore
from car_approval import CarApproval

app = Flask(__name__)


@app.route("/", methods=["GET"])
def form():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        budget = int(request.form['budget'])
        credit_score = int(request.form['credit_score'])
        down_payment = int(request.form.get('down_payment') or 0)  # Was throwing an error so switched from , 0 to or 0
        monthly_income = int(request.form['monthly_income'])
        employment_status = int(request.form['employment_status'])
        payment_method = request.form['payment_method']
        finance_term = int(request.form['finance_term']) if payment_method == 'finance' else 0

        # Run Scoring logic
        credit_rating = CreditScore(credit_score).credit_rating()
        down_payment_score = DownPayment(down_payment, budget).down_payment_score()
        employment = Employment(employment_status, monthly_income)
        employment_score = employment.employment_status_score()
        income_score = employment.monthly_income_score()
        finance_score = FinanceTerm(finance_term).finance_term_score()

        final_score = CustomerScore(down_payment_score, credit_rating, employment_score,
                                    income_score, finance_score).final_customer_score()

        approval = CarApproval(final_score, budget, down_payment, payment_method)
        approved, manual = approval.get_approval_limit(cars)

        return render_template("results.html", final_score=final_score, manual=manual, approved=approved)


if __name__ == "__main__":
    app.run(debug=False)
application = app

