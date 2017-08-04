from setting.databases import mongo as db


class NewsData(db.Document):
    idx = db.StringField()
    title = db.StringField()
    content = db.StringField()
    tags = db.ListField(db.StringField())

    source = db.StringField()
    header_image = db.StringField()

    del_check = db.IntField()
    created_by = db.StringField()

    def __init__(self, idx):
        self.idx = idx

    def json(self):
        return {
            'idx': self.idx,
            'title': self.title,
            'content': self.content
        }


        # class Business(db.Document):
        #     name = db.StringField(required=True)
        #     address = db.StringField()
        #     location = db.GeoPointField()
        #     tags = db.ListField()
        #     area = db.ReferenceField(Area, dbref=True)
        #     contact = db.EmbeddedDocumentField(Contact)
        #     details = db.EmbeddedDocumentField(details)
