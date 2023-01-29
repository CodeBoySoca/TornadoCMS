import tornado.web

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', page_title='Log In')