from db import mongo as db


# Field(required=True, default=UNSET, default_f=None, db_field=None, allow_none=False, on_update='$set', validator=None, unwrap_validator=None, wrap_validator=None, _id=False, proxy=None, iproxy=None, ignore_missing=False)¶

class NewsData(db.Document):
    _id = db.StringField()
    NEWS_IDX = db.IntField()
    news_title = db.StringField()
    news_content = db.StringField()
    news_tags = db.ListField(db.StringField())

    news_from_source = db.StringField()
    news_header_image = db.StringField()

    news_del_check = db.IntField()
    news_created_by = db.StringField()

    def __init__(self, NEWS_IDX):
        self.NEWS_IDX = NEWS_IDX

    def __str__(self):
        return {'email': self.email, 'nickname': self.nickname, 'password': self.password}

    def json(self):
        return {
            'news_idx': self.NEWS_IDX,
            'news_title': self.news_title,
            'news_content': self.news_content
        }


        # class Business(db.Document):
        #     name = db.StringField(required=True)
        #     address = db.StringField()
        #     location = db.GeoPointField()
        #     tags = db.ListField()
        #     area = db.ReferenceField(Area, dbref=True)
        #     contact = db.EmbeddedDocumentField(Contact)
        #     details = db.EmbeddedDocumentField(details)
