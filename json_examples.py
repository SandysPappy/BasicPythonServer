import tornado.web as tw
import tornado.ioloop as tio
import asyncio # introduced in python 3.10
import json

class listRequestHandler(tw.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()

        # json.dumps() function will convert a subset of Python objects into a json string. Not all objects are convertible and you may need
        # to create a dictionary of data you wish to expose before serializing to JSON.
        self.write(json.dumps(fruits)) 


if __name__ == "__main__":
    app = tw.Application([
        (r"/list", listRequestHandler)
    ])

    port1 = 6969
    port2 = 8888

    app.listen(port1)
    app.listen(port2)

    print(f'Application started and is running on port {port1} and {port2}')
    tio.IOLoop.current().start() # creates the listener