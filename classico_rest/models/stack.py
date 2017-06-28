from databases import db

stack_similar = db.Table('TB_STACK_SIMILAR_REFER',
                         db.Column('stack_id', db.BigInteger, db.ForeignKey('TB_STACK.id'), nullable=False),
                         db.Column('stack_similar_id', db.BigInteger, db.ForeignKey('TB_SIMILAR_STACK.id'), nullable=False))


class StackModel(db.Model):
    __tablename__ = 'TB_STACK'
    id = db.Column(db.BigInteger, primary_key=True)
    stack_name = db.Column(db.String(80), unique=True, nullable=False)

    stack_home_url = db.Column(db.String(200))
    similars = db.relationship('SimilarStackModel', secondary=stack_similar, back_populates='stacks', lazy='dynamic')

    stack_depth = db.Column(db.Integer, default=0, server_default=db.text('0'))
    comment_depth = db.Column(db.Integer, default=0, server_default=db.text('0'))
    company_depth = db.Column(db.Integer, default=0, server_default=db.text('0'))
    hits = db.Column(db.Integer, default=0, server_default=db.text('0'))
    likes = db.Column(db.Integer, default=0, server_default=db.text('0'))
    hates = db.Column(db.Integer, default=0, server_default=db.text('0'))

    modified_by = db.Column(db.String(100))
    modified_date = db.Column(db.TIMESTAMP(True),
                              server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, stack_name):
        self.stack_name = stack_name

    def json(self):
        return {
            'stack_name': self.stack_name,
            'stack_home_url': self.stack_home_url,

            'stack_depth': self.stack_depth,
            'comment_depth': self.comment_depth,
            'hits': self.hits,
            'likes': self.likes,
            'hates': self.hates,

            'similars': [similars.json() for similars in self.similars]}

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
    def find_by_stack_name(cls, stack_name):
        # stack = SimilarStackModel.query.filter(SimilarStackModel.stacks.any(stack_name=stack_name)).all()
        stack = cls.query.filter_by(stack_name=stack_name).first()
        return stack

    @classmethod
    def find_list(cls):
        return cls.query.filter_by()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class SimilarStackModel(db.Model):
    __tablename__ = 'TB_SIMILAR_STACK'
    id = db.Column(db.BigInteger, primary_key=True)
    stack_name = db.Column(db.String(80), nullable=False)
    stacks = db.relationship("StackModel", secondary=stack_similar, back_populates="similars", lazy='dynamic')

    modified_by = db.Column(db.String(100))
    modified_date = db.Column(db.TIMESTAMP(True),
                              server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, stack_name):
        self.stack_name = stack_name

    def json(self):
        return {
            'stack_name': self.stack_name,
            # 'stacks': [stacks.json() for stacks in self.stacks.all()],
            'modified_by': self.modified_by,
            'modified_date': self.modified_date.__str__()
        }

    @classmethod
    def find_by_stack_name(cls, stack_name):
        return cls.query.filter_by(stack_name=stack_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

# class Parent(db.Model):
#     __tablename__ = 'left'
#     id = db.Column(db.Integer, primary_key=True)
#     children = db.relationship("Child",
#                                secondary=association_table)
#
# class Child(db.Model):
#     __tablename__ = 'right'
#     id = db.Column(db.Integer, primary_key=True)
#
#
# p = Parent()
# c = Child()
# p.children.append(c)
# db.session.add(p)
# db.session.commit()
