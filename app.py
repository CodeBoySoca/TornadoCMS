import os.path
import tornado.ioloop
import tornado.web
from handlers import user_handler, dashboard_server, server_handler, project_handler, production_handler



settings = {
    "debug" : True,
    "cookie_secret" : "SECRET KEY HERE",
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    "xsrf_cookies" : False,
}

urls = [
    (r'/', user_handler.UserHandler),
    (r'/dashboard', dashboard_server.DashboardHandler),
    (r'/manage/server', server_handler.ServerHandler),
    (r'/manage/project', project_handler.ProjectHandler),
    (r'/manage/production', production_handler.ProductionHandler)

]

class TornadoApp(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)


if __name__ == '__main__':
    app = TornadoApp()
    app.listen(8811)
    tornado.ioloop.IOLoop.current().start()