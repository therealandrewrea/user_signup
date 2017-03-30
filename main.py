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
import re

#CSS for Red Error Messages - apply inline as class
#<style type="text/css">
    #.error {
        #color: red;
    #}
#</style>

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>User Signup</h1>"
        user_req = "<label>   Username</label><input type='text' name='username'>"
        pwd_req = "<label>    Password</label><input type='text' name='password1'>"
        pwd_req2 = "<label>Verify Password</label><input type='text' name='password2'>"
        email_req = "<label>Email(optional)</label><input type='text' name='email'>"
        submit_button = "<input type='submit' name='submit'>"
        user_error = ""
        pwd1_error = ""
        pwd2_error = ""
        email_error = ""
        content = '''<form method="post">''' + user_req + user_error + "<br>" + pwd_req + pwd1_error + "<br>" + pwd_req2 + pwd2_error + "<br>" + email_req + email_error + "<br>" + submit_button + '''</form>'''
            #within the content line, insert relevant errors (user_req + user_error), (pwd_req + pwd1_error), (pwd_req2 + pwd2_error), (email_req + email_error)

    #error = self.request.get("error")
        #if error:
            #error_esc = cgi.escape(error, quote=True)
            #error_element = '<p class="error">' + error_esc + '</p>'
        #else:
            #error_element = ''

        self.response.write(header + content) #for initial load of page, reloads and error messages after a post

    def post(self): #for updating of data from post request
        username = self.request.get("username")
        password1 = self.request.get("password1")
        password2 = self.request.get("password2")
        email = self.request.get("email")

        valid_user = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        valid_pass = re.compile(r"^.{3,20}$")
        valid_email = re.compile(r"^[\S]+@[\S]+.[\S]+$")

        very_valid_user = valid_user.match(username)
        very_valid_pass = valid_pass.match(password1)
        very_valid_email = valid_email.match(email)

        #if password1 != password2 #check if passwords match, return pwd_error2 if they don't
        #if any errors, identify and create error message

        user_error = "That's not a valid username."
        pwd_error = "That wasn't a valid password."
        pwd_error2 = "Your passwords don't match."
        email_error = "That's not a valid email."
        #self.redirect("/?error=" + error)
        #redirect to original page with errors included

        #if all checks clear, print this content
        content = "<h1>Welcome, {0}!".format(username)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
