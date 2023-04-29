import tornado.web
from database import db

class FilterHandler(tornado.web.RequestHandler):
    async def get(self):
        sort_result = db.projects.find({}).sort(self.get_arguments('dropdown_filter')[0])
        projects = []
        async for document in sort_result:
            projects.append(document)
        print(self.request.path)
        self.render('partials/projects.html', projects=projects, page_title='dashboard')
        
        





