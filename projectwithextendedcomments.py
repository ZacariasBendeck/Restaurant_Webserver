from flask import Flask
app = Flask(__name__)  #  __name__  is the name of the running application
			#everytime we run an application with python a special variable called name gets defined
			# for the application and all of the imports it uses


@app.route('/')    #DECORATOR This decorator will call the function that follows it
@app.route('/hello')  

def HelloWorld():      #THIS is the function that will be executed when the route is /, or /hello
	return'Hello World'

if __name__ == '__main__':  # this IF statement ensure this part is only runs if the script is executed directly
						# from the python interpreter, NOT if it is imported as a module
	app.debug= True		# with this line we dont need to reload the server everytime we change the code
	app.run (host = '0.0.0.0', port = 5000) # 
