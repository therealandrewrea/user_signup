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
page_header = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
'''

page_footer = '''
</body>
</html>
'''

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email and EMAIL_RE.match(email)

error_messages = ["That's not a valid username",
"That's not a valid password",
"Passwords don't match",
"That's not a valid email"
]


def write_form(username, email, user_error, pwd1_error, pwd2_error, email_error):
    signup_header = "<h1>Signup</h1>"

    signup_form = '''
    <form method='post'>
    <table>
        <tr>
        <td><label>Username</label></td>
        <td><input name='username' type='text' value="'''+username+'''" required/></td>
        <td><span class='error'>'''+user_error+'''</span></td>
        </tr>
        <tr>
        <td><label>Password</label></td>
        <td><input name='password1' type='password' required/></td>
        <td><span class='error'>'''+pwd1_error+'''</span></td>
        </tr>
        <tr>
        <td><label>Verify Password</label></td>
        <td><input name='password2' type='password' required/></td>
        <td><span class='error'>'''+pwd2_error+'''</span></td>
        </tr>
        <tr>
        <td><label>Email (optional)</label></td>
        <td><input name='email' type='email' value="'''+email+'''"/></td>
        <td><span class='error'>'''+email_error+'''</span></td>
        </tr>
    </table>
    <input type='submit'>
    '''

    return page_header + signup_header + signup_form + page_footer


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_error = ""
        pwd1_error = ""
        pwd2_error = ""
        email_error = ""

        blank = write_form("","","","","","")
        self.response.write(blank)    #within the content line, insert relevant errors (user_req + user_error), (pwd_req + pwd1_error), (pwd_req2 + pwd2_error), (email_req + email_error)

    def post(self): #for updating of data from post request
        username = self.request.get("username")
        password1 = self.request.get("password1")
        password2 = self.request.get("password2")
        email = self.request.get("email")

        errors = False
        user_error = ""
        pwd1_error = ""
        pwd2_error = ""
        email_error = ""
        #regular expressions for verifying inputs
        if not valid_username(username):
            user_error += error_messages[0]
            errors = True

        if not valid_password(password1):
            pwd1_error += error_messages[1]
            errors = True

        if password1 != password2:
            pwd2_error += error_messages[2]
            errors = True

        if len(email) > 0:
            if not valid_email(email):
                email_error += error_messages[3]
                errors = True

        if errors == False:
            self.redirect('/welcome?username=' + username)
        if errors == True:
            error_codes = write_form(username,email,user_error,pwd1_error,pwd2_error,email_error)
            self.response.write(error_codes)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        greeting = "Welcome, " + username + "!"
        content = page_header + "<h1>"+greeting+"</h1>" + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
