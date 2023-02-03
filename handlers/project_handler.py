import tornado.web
from database import db


class ProjectHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('project.html', page_title='Add Project')

    async def post(self):
        project_values = self.request.arguments
        data = dict()
        for key, value in project_values.items():
            data[key] = value[0].decode('utf-8')
        await db.projects.insert_one(data)

    async def delete(self, project_id):
        delete_item = await db.projects.delete_one({'_id' : project_id}) 
        return f'removed item with id: {project_id}'


