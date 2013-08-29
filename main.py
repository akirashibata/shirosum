#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from google.appengine.api import users
import urllib2
import urllib
import json
from HtmlContents import HtmlContents

#from google.appengine.api import urlfetch
#urlfetch.set_default_fetch_deadline(60) 

class MainHandler(webapp2.RequestHandler):
    def get(self):
        doc=HtmlContents()
        self.response.write(doc.top_page("テキストを自動で要約します"))

class Guestbook(webapp2.RequestHandler):
      def post(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        checkbox=None
        
        doc=HtmlContents()

        if cgi.escape(self.request.get('evaluation')): checkbox=int(cgi.escape(self.request.get('evaluation')))

        api_url=u'http://mixtape.jp/'
        if checkbox:
          data={}
          data['id']='shirosum_evaluate'
          data['checkbox']=checkbox

          req = urllib2.Request(api_url, headers=headers, data=json.dumps(data))
          response=urllib2.urlopen(req, timeout=15)
          html = response.read()
          self.response.write(doc.thanks_page())

        else:
          title=cgi.escape(self.request.get('title'))
          body=cgi.escape(self.request.get('body'))
          url=cgi.escape(self.request.get('url'))

          data={}
          data['id']='shirosum_post'
          data['title']=title.encode("utf-8")
          data['body']=body.encode("utf-8")
          data['url']=url.encode("utf-8")

          req = urllib2.Request(api_url, headers=headers, data=json.dumps(data))
          response=urllib2.urlopen(req, timeout=15)
          html = response.read()
          jres=json.loads(html)

          if jres.has_key('status'):
            status='<font color="red">'+jres['status'].encode('utf-8')+'</font>'
            self.response.write(doc.top_page(status))
          else:
            self.response.write(doc.summary_done_page(jres))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', Guestbook),
    ], debug=True)


