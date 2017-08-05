from setting.databases import mongo


class NewsModel(mongo.Document):
    mongo.config_collection_name = 'NewsData'

    _id = mongo.StringField()
    NEW_IDX = mongo.IntField()

    NEWS_TITLE = mongo.StringField()
    NEWS_CONTENT = mongo.StringField()
    NEWS_TAGS = mongo.ListField(mongo.StringField())

    NEWS_FROM_SOURCE = mongo.StringField()

    # header_image = mongo.StringField()
    # content_images = mongo.ListField(mongo.StringField())

    # del_check = mongo.IntField()
    # modified_by = mongo.StringField()
    # modified_date = mongo.DateTimeField()
    # created_by = mongo.StringField()
    # created_date = mongo.DateTimeField()

    def __init__(self, idx):
        self.idx = idx

    def json(self):
        return {
            '_id': self._id,
            'index': self.NEW_IDX,

            'title': self.NEWS_TITLE,
            'content': self.NEWS_CONTENT,
            'tags': [tag.json() for tag in self.NEWS_TAGS],
            'source': self.NEWS_FROM_SOURCE,

            # 'header_image': self.header_image,
            # 'content_images': [content_image.json() for content_image in self.content_images],

            # 'del_check': self.del_check,
            # 'modified_by': self.modified_by,
            # 'modified_date': self.modified_date,
            # 'created_by': self.created_by,
            # 'created_date': self.created_date,
        }

    @classmethod
    def find_by_index(cls, index):
        return mongo.session.query(NewsModel).filter_by(NEW_IDX=index).all()

    @classmethod
    def find_by_id(cls, index):
        # cls.query.filter(NewsModel.id == _id).first()
        return mongo.session.query(NewsModel).filter_by(_id=index).in_(NewsModel.NEWS_FROM_SOURCE, 'service').all()

    @classmethod
    def find_all(cls):
        # cls.query.filter(NewsModel.id == _id).first()
        return mongo.session.query(NewsModel).all()

    def __eq__(self, other):
        return self.index == other.index

    def __repr__(self):
        return 'News(index="%s")' % self.index

# class Business(mongo.Document):
#     name = mongo.StringField(required=True)
#     address = mongo.StringField()
#     location = mongo.GeoPointField()
#     tags = mongo.ListField()
#     area = mongo.ReferenceField(Area, mongoref=True)
#     contact = mongo.EmbeddedDocumentField(Contact)
#     details = mongo.EmbeddedDocumentField(details)
#     gender = EnumField(StringField(), 'male', 'female')
#     blood_type = EnumField(StringField(), 'O+', 'A+', 'B+', 'AB+', 'O-', 'A-', 'B-', 'AB-')
