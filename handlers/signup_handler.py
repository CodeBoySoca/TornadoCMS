import tornado.web

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
       self.render('signup.html', page_title='Sign up')