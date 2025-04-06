from src import db

class Candidate(db.Model):
    __tablename__ = 'candidate'
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented by default
    fullName = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    yearOfGraduation  = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    ExperienceYear = db.Column(db.String(20),nullable=False)
    currentEmployer = db.Column(db.String(100),nullable=False)
    currentCTC = db.Column(db.String(100),nullable=False)
    expectedCTC = db.Column(db.String(100),nullable=False)
    noticePeriod = db.Column(db.String(100),nullable=False)
    filename = db.Column(db.String(120), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)
    upload_time = db.Column(db.DateTime, default=db.func.current_timestamp())
