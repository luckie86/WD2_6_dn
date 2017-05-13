#!/usr/bin/env python
import os
import jinja2
import webapp2

from handlers.topics import TopicAddHandler, TopicDetailsHandler

from handlers.base import BaseHandler, MainHandler, CookieAlertHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
    webapp2.Route('/topic/add', TopicAddHandler),
    webapp2.Route('/topic-details/<topic_id:\d+>', TopicDetailsHandler, name="topic-details"),
], debug=True)
