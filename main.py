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

def write_form(username, email, user_error, pwd1_error, pwd2_error, email_error):
    header = "<h1>User Signup</h1>"
    user_req = "<label>   Username</label><input type='text' name='username' value=''>"
    pwd_req = "<label>    Password</label><input type='password' name='password1' value=''>"
    pwd_req2 = "<label>Verify Password</label><input type='password' name='password2' value=''>"
    email_req = "<label>Email(optional)</label><input type='text' name='email' value=''>"
    submit_button = "<input type='submit' name='submit'>"
    form = header + '''<form method="post">''' + user_req + user_error + "<br>" + pwd_req + pwd1_error + "<br>" + pwd_req2 + pwd2_error + "<br>" + email_req + email_error + "<br>" + submit_button + '''</form>'''
    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        blank = write_form("","","","","","")
        self.response.write(blank)    #within the content line, insert relevant errors (user_req + user_error), (pwd_req + pwd1_error), (pwd_req2 + pwd2_error), (email_req + email_error)

    def post(self): #for updating of data from post request
        username = self.request.get("username")
        password1 = self.request.get("password1")
        password2 = self.request.get("password2")
        email = self.request.get("email")

        have_error = False
        user_error = ""
        pwd1_error = ""
        pwd2_error = ""
        email_error = ""
        #regular expressions for verifying inputs
        user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        pass_re = re.compile(r"^.{3,20}$")
        email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

        def valid_username(username):
            return username and user_re.match(username)
        def valid_password(password1):
            return password1 and pass_re.match(password1)
        def valid_email(email):
            return not email or email_re.match(email)

        if not valid_username(username):
            user_error += "That's not a valid username."
            have_error = True
        if not valid_email(email):
            email_error += "That's not a valid email."
            have_error = True
        if not valid_password(password1):
            pwd1_error += "That wasn't a valid password."
            have_error = True
        if password2 != password1:
            pwd2_error += "Your passwords don't match."
            have_error = True

        content = "<h1>Welcome, {0}!".format(username)

        if have_error == True:
            error_page = write_form(username, email, user_error, pwd1_error, pwd2_error, email_error)
            self.response.write(error_page) #placeholder, displays snarky message when have_error is True
        elif have_error == False:
            self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
