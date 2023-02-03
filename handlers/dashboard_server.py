import tornado.web
from datetime import datetime

class DashboardHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        projects = [
            {'name' : 'TravelBot', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Bottle', 'id' : 1},
            {'name' : 'Chiquis', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'production', 'tech_stack' : 'Bottle', 'id' : 2},
            {'name' : 'Jukebox', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'FastAPI', 'id' : 3},
            {'name' : 'Guard Dog', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Flask', 'id' : 4},
            {'name' : 'Bookstash', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'PHP', 'id' : 5},
            {'name' : 'Uniq', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Sinatra', 'id' : 6},
            {'name' : 'MyPassport', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Tornado', 'id' : 7},
            {'name' : 'Cookies and Cream', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Django', 'id' : 8},
            {'name' : 'FightPub', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Ruby on Rails', 'id' :10}
        ]
        self.render('dashboard.html', page_title='Dashboard', username=username, projects=projects)
