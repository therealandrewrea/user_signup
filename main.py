#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>User Signup</h1>"
        user_req = "<label>   Username</label><input type='text' name='username'>"
        pwd_req = "<label>    Password</label><input type='text' name='password1'>"
        pwd_req2 = "<label>Verify Password</label><input type='text' name='password2'>"
        email_req = "<label>Email(optional)</label><input type='text' name='email'>"
        submit_button = "<input type='submit' name='submit'>"
        content = '''<form method="post">''' + user_req + "<br>" + pwd_req + "<br>" + pwd_req2 + "<br>" + email_req + "<br>" + submit_button + '''</form>'''

        self.response.write(header + content) #for initial load of page, reloads and error messages after a post

    #def post(self): #for updating of data from post request

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
