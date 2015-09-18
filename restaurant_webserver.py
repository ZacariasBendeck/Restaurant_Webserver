<<<<<<< HEAD
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
                    output += '<a href= "http://localhost:8080/edit"> Edit</a><br>'
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

                new_restaurant = Restaurant(name = messagecontent)

                engine = create_engine('sqlite:///restaurantmenu.db')
                Base.metadata.bind = engine
                DBSession = sessionmaker(bind=engine)
                session = DBSession()
                session.add(new_restaurant)
                session.commit

                print output
=======
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Objective 3 Step 2 - Create /restarants/new page
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></html></body>"
                self.wfile.write(output)
                return
            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += myRestaurantQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/restaurants/%s/edit' >" % restaurantIDPath
                    output += "<input name = 'newRestaurantName' type='text' placeholder = '%s' >" % myRestaurantQuery.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += 'Are you sure you want to delete ' + myRestaurantQuery.name + '?'
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/restaurants/%s/delete' >" % restaurantIDPath                    
                    output += "<input type = 'submit' value = 'Delete'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                # Objective 3 Step 1 - Create a Link to create a new menu item
                output += "<a href = '/restaurants/new' > Make a New Restaurant Here </a></br></br>"

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    # Objective 2 -- Add Edit and Delete Links
                    # Objective 4 -- Replace Edit href
                    output += "<a href ='/restaurants/%s/edit' >Edit </a> " % restaurant.id
                    output += "</br>"
                    output += "<a href ='/restaurants/%s/delete'> Delete </a>" % restaurant.id
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    # Objective 3 Step 3- Make POST method
    def do_POST(self):
        try:
            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)

                    restaurantIDPath = self.path.split("/")[2]

                    myRestaurantQuery = session.query(Restaurant).filter_by(
                        id=restaurantIDPath).one()
                    if myRestaurantQuery != []:
                        session.delete(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()
>>>>>>> c97d9f6f4cef1201a1b36f37831f18da3e7f313a

        except:
            pass


<<<<<<< HEAD
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
=======
def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()
>>>>>>> c97d9f6f4cef1201a1b36f37831f18da3e7f313a
