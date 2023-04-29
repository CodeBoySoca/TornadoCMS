import tornado.web

class PasscodeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('otp.html', page_title='OTP')