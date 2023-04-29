import tornado.web
from datetime import datetime
from database import db


class DashboardHandler(tornado.web.RequestHandler):
    async def post(self):
        pass


    async def get(self):
        username = 'Rocky'
        password = 'password'
        sorted_projects = db.projects.find({})
        projects = []
        async for document in sorted_projects:
            projects.append(document)
        self.render('dashboard.html', page_title='Dashboard', username=username, projects=projects)
