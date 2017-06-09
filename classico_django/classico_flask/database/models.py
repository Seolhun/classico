from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Board(db.Model):
    __tablename__ = 'TB_BOARD'
    id = Column(db.BigInteger, primary_key=True)
    title = Column(db.String(100), nullable=False)
    text = Column(db.TEXT, nullable=False)
    hits = Column(db.Integer, default=0)
    commentDepth = Column(db.Integer, default=0)
    fileDepth = Column(db.Integer, default=0)
    likes = Column(db.Integer, default=0)
    hates = Column(db.Integer, default=0)
    comments = db.relationship('Comment', backref='board', lazy=True)
    files = db.relationship('Comment', backref='board', lazy=True)

    created_by = Column(db.String(100))
    created_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = Column(db.String(100))
    modified_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, title, text, created_by):
        self.title = title
        self.text = text
        self.created_by = created_by

    def publish(self):
        self.created_date = db.TIMESTAMP

    def __repr__(self):
        return '<Board %r>' % self.title

    def __str__(self):
        return self.title


class Comment(db.Model):
    __tablename__ = 'TB_COMMENT'
    id = Column(db.BigInteger, primary_key=True)
    board_id = db.Column(db.BigInteger, db.ForeignKey('TB_BOARD.id'), nullable=False)

    text = Column(db.String(300), nullable=False)
    likes = Column(db.Integer, default=0)
    hates = Column(db.Integer, default=0)

    created_by = Column(db.String(100))
    created_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = Column(db.String(100))
    modified_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, title, text, created_by):
        self.title = title
        self.text = text
        self.created_by = created_by

    def publish(self):
        self.created_date = db.TIMESTAMP

    def __repr__(self):
        return '<Comment %r>' % self.text

    def __str__(self):
        return self.title


class File(db.Model):
    __tablename__ = 'TB_FILE'
    id = Column(db.BigInteger, primary_key=True)
    board_id = db.Column(db.BigInteger, db.ForeignKey('TB_BOARD.id'), nullable=False)

    origin_name = Column(db.String(200), nullable=False)
    saved_name = Column(db.String(200), nullable=False)
    path = Column(db.String(200), nullable=False)
    size = Column(db.Integer(10))

    created_by = Column(db.String(100))
    created_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = Column(db.String(100))
    modified_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, origin_name):
        self.origin_name = origin_name

    def publish(self):
        self.created_date = db.TIMESTAMP

    def __repr__(self):
        return '<File %r>' % self.originName

    def __str__(self):
        return self.origin_name


class Stack(db.Model):
    __tablename__ = 'TB_STACK'
    id = Column(db.BigInteger, primary_key=True)
    name = Column(db.String(100), nullable=False)
    hits = Column(db.Integer, default=0)
    comment_depth = Column(db.Integer, default=0)
    stack_depth = Column(db.Integer, default=0)
    company_depth = Column(db.Integer, default=0)
    company_depth = Column(db.Integer, default=0)
    likes = Column(db.Integer, default=0)
    hates = Column(db.Integer, default=0)

    comments = db.relationship('Comment', backref='stack', lazy=True)

    created_by = Column(db.String(100))
    created_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = Column(db.String(100))
    modified_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, name):
        self.name = name

    def publish(self):
        self.created_date = db.TIMESTAMP

    def __repr__(self):
        return '<Stack %r>' % self.name

    def __str__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'TB_USER'
    id = Column(db.BigInteger, primary_key=True)
    name = Column(db.String(100), nullable=False)
    email = Column(db.String(100), default=0, nullable=False)
    password = Column(db.String(128), nullable=False)

    fail_count = Column(db.Integer, default=0)
    token = Column(db.String(200))

    created_by = Column(db.String(100))
    created_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))
    modified_by = Column(db.String(100))
    modified_date = Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, name):
        self.name = name

    def publish(self):
        self.created_date = db.TIMESTAMP

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return self.name
