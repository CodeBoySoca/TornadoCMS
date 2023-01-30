import tornado.web
from datetime import datetime

class DashboardHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        projects = [
            {'name' : 'TravelBot', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Bottle'},
            {'name' : 'Chiquis', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'production', 'tech_stack' : 'Bottle'},
            {'name' : 'Jukebox', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'FastAPI'},
            {'name' : 'Guard Dog', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Flask'},
            {'name' : 'Bookstash', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'PHP'},
            {'name' : 'Uniq', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Sinatra'},
            {'name' : 'MyPassport', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Tornado'},
            {'name' : 'Cookies and Cream', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Django'},
            {'name' : 'FightPub', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development', 'tech_stack' : 'Ruby on Rails'}
        ]
        self.render('dashboard.html', page_title='Dashboard', username=username, projects=projects)
