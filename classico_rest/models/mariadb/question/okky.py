from databases import db

stack_similar = db.Table('TB_STACK_SIMILAR_REFER',
                         db.Column('stack_id', db.BigInteger, db.ForeignKey('TB_STACK.id'), nullable=False),
                         db.Column('stack_similar_id', db.BigInteger, db.ForeignKey('TB_SIMILAR_STACK.id'), nullable=False))


class OkkyModel(db.Model):
    __tablename__ = 'TB_OKKY'
    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.String(80), unique=True, nullable=False)

    title = db.Column(db.String(200))
    content = db.Column(db.Text())

    comment_depth = db.Column(db.Integer, default=0, server_default=db.text('0'))
    hits = db.Column(db.Integer, default=0, server_default=db.text('0'))
    likes = db.Column(db.Integer, default=0, server_default=db.text('0'))
    scraps = db.Column(db.Integer, default=0, server_default=db.text('0'))

    modified_by = db.Column(db.String(100))
    modified_date = db.Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_by = db.Column(db.String(100))
    created_date = db.Column(db.TIMESTAMP(True), server_default=db.text('CURRENT_TIMESTAMP'))

    def __init__(self, id):
        self.id = id

    def json(self):
        return {
            'id': self.id,
            'type': self.type,

            'title': self.title,
            'content': self.content,
            'comment_depth': self.comment_depth,
            'hits': self.hits,
            'likes': self.likes,
            'scraps': self.scraps,

            'modified_by': self.modified_by,
            'modified_date': self.modified_date,
            'created_by': self.created_by,
            'created_date': self.created_date,
        }

    # @classmethod
    # def find_by_stack_name_with_similars(cls, stack_name):
    #     # stack = SimilarStackModel.query.filter(SimilarStackModel.stacks.any(stack_name=stack_name)).all()
    #     stack = cls.query.filter_by(stack_name=stack_name).first()
    #     similars = SimilarStackModel.query.filter(SimilarStackModel.stacks.any(stack_name=stack_name)).all()
    #     stack.similars = similars
    #     for s in stack.similars:
    #         print("-------dasdsa------", s.stack_name)
    #     return stack

    @classmethod
    def find_by_id(cls, id):
        # stack = SimilarStackModel.query.filter(SimilarStackModel.stacks.any(stack_name=stack_name)).all()
        okky = cls.query.filter_by(id=id).first()
        return okky

    @classmethod
    def find_list(cls):
        return cls.query.filter_by()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()