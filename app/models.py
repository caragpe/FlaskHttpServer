from app import db


class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banner_message = db.Column(db.String(100))

    def __repr__(self):
        return '<Banner => [ id: {}, message: "{}" ]>'.format(self.id, self.banner_message)
