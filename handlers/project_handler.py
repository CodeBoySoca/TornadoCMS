import tornado.web

class ProjectHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('project.html', page_title='Add Project')

    def post(self):
        pass