from project import db , app
import re

# Loan model
class Loan(db.Model):
    __tablename__ = 'Loans'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64), nullable=False)
    book_name = db.Column(db.String(64), nullable=False)
    loan_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    original_author = db.Column(db.String(64), nullable=False)
    original_year_published = db.Column(db.Integer, nullable=False)
    original_book_type = db.Column(db.String(64), nullable=False)

    def __init__(self, customer_name, book_name, loan_date, return_date, original_author, original_year_published, original_book_type):
    
        if not re.match(r'^[a-zA-Z-]+$', customer_name) or not (1 <= len(customer_name) <= 64):
            raise ValueError(400, "Niepoprawna nazwa klienta. Dozwolone są znaki alfabetyczne i myślnik.")

        if not re.match(r'^[a-zA-Z0-9]+$', book_name) or not (1 <= len(book_name) <= 64):
            raise ValueError(400, "Niepoprawna nazwa książki. Dozwolone są znaki alfabetyczne i cyfry.")
    
        self.customer_name = customer_name
        self.book_name = book_name
        self.loan_date = loan_date
        self.return_date = return_date
        self.original_author = original_author
        self.original_year_published = original_year_published
        self.original_book_type = original_book_type

    def __repr__(self):
        return f"Customer: {self.customer_name}, Book: {self.book_name}, Loan Date: {self.loan_date}, Return Date: {self.return_date}"


with app.app_context():
    db.create_all()