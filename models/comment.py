from google.appengine.ext import ndb


class Comment(ndb.Model):
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    topic_id = ndb.IntegerProperty()
    topic_title = ndb.StringProperty()
    created = ndb.DateProperty(auto_now_add=True)
    updated = ndb.DateProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)