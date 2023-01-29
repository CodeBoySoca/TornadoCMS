import tornado.web
from datetime import datetime

class DashboardHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        projects = [
            {'name' : 'TravelBot', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'Chiquis', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'production'},
            {'name' : 'Jukebox', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'Guard Dog', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'Bookstash', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'Uniq', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'MyPassport', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'Cookies and Cream', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'},
            {'name' : 'FightPub', 'date' : datetime.now().date(), 'project_url' : '', 'status' : 'development'}
        ]
        self.render('dashboard.html', page_title='Dashboard', username=username, projects=projects)
