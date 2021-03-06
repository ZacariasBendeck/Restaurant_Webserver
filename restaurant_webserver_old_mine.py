# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 03:22:53 2015

@author: Z
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, MenuItem, Restaurant

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()


                output = ''
                output += '<html><body>'
                output += "<form method= 'POST' enctype='multipart/form-data' \
                    action ='new'><h2>Make a New Restaurant</h2><input\
                    name='message' type='text' ><input type='submit' value=\
                    'Create'> </form>"
                output += '<br><a href= "http://localhost:8080/restaurants">'
                output += ' Back to Restaurants Home</a><br><br><br>'

                output += '</body></html>'
                self.wfile.write(output)
                print output
                return



            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                engine = create_engine('sqlite:///restaurantmenu.db')
                Base.metadata.bind = engine
                DBSession = sessionmaker(bind=engine)
                session = DBSession()

                restaurants = session.query(Restaurant).all()

                output = ''
                output += '<html><body>'
                output += '<a href= "http://localhost:8080/restaurants/new">'
                output += ' Create a new Restaurant here</a><br><br><br>'

                for item in restaurants:
                    output += item.name
                    output += '<br>'
                    output += '<a href= "http://localhost:8080/' + item.id + '/edit"> Edit</a><br>'
                    output += '<a href= "http://localhost:8080/delete"> Delete</a>'
                    output += '<br><br>'


                output += '</body></html>'
                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += 'Hello!'
                output += "<form method= 'POST' enctype='multipart/form-data' \
                    action ='hello'><h2>What would you like to say?</h2><input\
                     name='message' type='text' ><input type='submit' value=\
                     'Submit'> </form>"
                output += '</body></html>'
                self.wfile.write(output)
                print output
                return


            if self.path.endswith('/hola'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += "<html><body>"
                output += "&#161Hola!   <a href = '/hello' >Back to Hello<a>"
                output += "<form method= 'POST' enctype='multipart/form-data' \
                    action ='hello'><h2>What would you like to say?</h2><input\
                     name='message' type='text' ><input type='submit' value=\
                     'Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return


        except IOError:
            self.send_error(404, 'File Not Found %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

                engine = create_engine('sqlite:///restaurantmenu.db')
                Base.metadata.bind = engine
                DBSession = sessionmaker(bind=engine)
                session = DBSession()
                print messagecontent
                new_restaurant = Restaurant(name = messagecontent[0])

                session.add(new_restaurant)
                
                output = ''
                output += "<html><body>"
                output += "<h2> You have added the following new Restaurant </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]

                output += "<form method= 'POST' enctype='multipart/form-data' \
                    action ='hello'><h2>Would you like to add another?</h2><input\
                     name='message' type='text' ><input type='submit' value=\
                     'Submit'> </form>"
                output += '<br><a href= "http://localhost:8080/restaurants">'
                output += ' Back to Restaurants Home</a><br><br><br>'
                output += "</body></html>"
                
                self.wfile.write(output)

                print output
                
                session.commit()

                

        except:
            pass


# functiion that handles hello
'''

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

                output = ''
                output += "<html><body>"
                output += "<h2> Okay, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]

                output += "<form method= 'POST' enctype='multipart/form-data' \
                    action ='hello'><h2>What would you like to say?</h2><input\
                     name='message' type='text' ><input type='submit' value=\
                     'Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output


        except:
            pass
'''

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print 'Web server running on port %s' % port
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C entered, stopping web server...'
        server.socket.close()

if __name__ == '__main__':
    main()
