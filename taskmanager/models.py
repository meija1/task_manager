from taskmanager import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25))

    def __repr__(self):
        return self


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
