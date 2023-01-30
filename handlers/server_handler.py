import tornado.web

class ServerHandler(tornado.web.RequestHandler):
    def post(self):
        pass

    def get(self):
        self.render('server.html', page_title='Add Server')