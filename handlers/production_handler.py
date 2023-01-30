import tornado.web

class ProductionHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('production.html', page_title='Production')