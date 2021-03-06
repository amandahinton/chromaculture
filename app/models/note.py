from .db import db

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey("articles.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_details = db.relationship("User", back_populates="note_details")
    article_details = db.relationship("Article", back_populates="note_details")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'article_id': self.article_id,
            'content': self.content,
        }
