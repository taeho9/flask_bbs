
from blogger import db

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    posting_date = db.Column(db.DateTime(), nullable=False)

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'))
    post = db.relationship('Post', backref=db.backref('reply_set'))
    content = db.Column(db.Text(), nullable=False)
    reply_date = db.Column(db.DateTime(), nullable=False)

