#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os
import voting

class VoteWrite(webapp.RequestHandler):
    def post(self):
##
## 書き込み処理
        bd = voting.votingdata(
            name = self.request.get('name'),
            serialno = self.request.get('serialno'))
        bd.put()
        self.redirect("/")

application = webapp.WSGIApplication([('/write', VoteWrite)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
