
from google.appengine.api import users

from handlers.base import BaseHandler
from models.topic import Topic


class TopicAddHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You're not logged in.")
        title = self.request.get("title")
        text = self.request.get("text")

        new_topic = Topic(title=title, content=text, author_email=user.email())
        new_topic.put()

        return self.redirect_to("topic-details", topic_id = new_topic.key.id())


class TopicDetailsHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        params = {"topic": topic}
        return self.render_template("topic_details.html", params)