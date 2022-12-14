import tornado.web as tw
import tornado.ioloop as tio
import asyncio # introduced in python 3.10

class BasicRequestHandler(tw.RequestHandler):
    def get(self):
        self.write(f'This is printed from the inhereted tornado web\'s request handler when the get request is called on port. Yayyy!')
        print(f'get command was executed')

class ListRequestHandler(tw.RequestHandler):
    def get(self):
        self.render("index.html")

class QueryRequestHandler(tw.RequestHandler):
    # http://127.0.0.1:6969/iseven?num=5 returns '5 is odd'
    # http://127.0.0.1:6969/iseven?num=4 returns '4 is even'
    def get(self):
        number = self.get_argument("num")
        if number.isdigit():
            number = int(number)
            self.write(f"{number} is {'odd' if number&1 else 'even'}.")
        else: 
            self.write(f"{number} is not a valid integer.")

class ResourceParamRequestHandler(tw.RequestHandler):
    # the regualr expression becomes the input
    # https://regex101.com/
    #
    # http://127.0.0.1:6969/students/weeee/5464
    # Welcome Weeee! The course you are viewing is 5464.
    def get(self, studentName, courseID):
        self.write(f"Welcome {studentName}! The course you are viewing is {courseID}.")
        


if __name__ == '__main__':
    app =  tw.Application([
        (r"/", BasicRequestHandler),
        (r"/animals", ListRequestHandler),
        (r"/iseven", QueryRequestHandler),
        (r"/students/([a-zA-Z]+)/([0-9]+)", ResourceParamRequestHandler)
    ])


    # recall ports below 1000 is reserved for the system
    port0 = 6969
    port1 = 9999

    app.listen(port0)
    app.listen(port1)
    print(f'App is running on ports {port0} and {port1}')
    tio.IOLoop.current().start() # starts the async IO event loop on the tornado server

    


