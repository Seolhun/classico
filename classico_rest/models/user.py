from db import db


class UserModel(db.Model):
    __tablename__ = 'TB_USER'
    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    created_by = db.Column(db.String(100))
    created_date = db.Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = db.Column(db.String(100))
    modified_date = db.Column(db.TIMESTAMP(True),
                              server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname

    def __str__(self):
        return {'email': self.email, 'nickname': self.nickname, 'password': self.password}

    def json(self):
        return {
            'email': self.email,
            'nickname': self.nickname,
            'created_date': self.created_date.__str__(),
            'modified_date': self.modified_date.__str__(),
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_nickname(cls, nickname):
        return cls.query.filter_by(nickname=nickname).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()