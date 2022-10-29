import tornado.web as tw
import tornado.ioloop as tio
import asyncio # introduced in python 3.10

class BasicRequestHandler(tw.RequestHandler):
    def get(self):
        self.write(f'Call Number: This is printed from the inhereted tornado web\'s request handler when the get request is called on port. Yayyy!')
        print(f'get command was executed')

class ListRequestHandler(tw.RequestHandler):
    def get(self):
        self.render("index.html")

class QueryRequestHandler(tw.RequestHandler):
    def get(self):
        number = self.get_argument("num")
        self.write(f"{number} is {'odd' if number & 1 else 'even'}.") if number.isdigit() else self.write(f"{number} is not a valid integer.")


if __name__ == '__main__':
    app =  tw.Application([
        (r"/", BasicRequestHandler),
        (r"/animals", ListRequestHandler),
        (r"/isEven", QueryRequestHandler)
    ])


    # recall ports below 1000 is reserved for the system
    port0 = 6969
    port1 = 9999

    app.listen(port0)
    app.listen(port1)
    print(f'App is running on ports {port0} and {port1}')
    tio.IOLoop.current().start() # starts the async IO event loop on the tornado server

    

