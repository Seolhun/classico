from db import db


class UserModel(db.Model):
    __tablename__ = 'TB_USER'
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

    created_by = db.Column(db.String(100))
    created_date = db.Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = db.Column(db.String(100))
    modified_date = db.Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return {'username': self.username, 'password': self.password}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
