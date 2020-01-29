#IMPLEMENTATION of the Web-based user interface (UI). 
#Such a UI provides a list of choices, where each choice enables an analytical objective (cf. Part 2). 
#However, the interaction between the UI and the analytical objectives is always mediated by the software Part 1. 
#The list of choices can be represented as a list of hyperlinks. 
#Each hyperlink is associated with a dedicated view (i.e. a Web page) that shows the outcomes of the analytical 
#operation requested by the user. Again the dedicated view provided by the Web page does not communicate directly with the Part 2, 
#but it communicates with the Part 1. Accordingly the Part 1 is responsible for (i) forwarding the request to the 
#appropriate class/method of Part 2 and (ii) returning the result to the view.

from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')  
def index(): 
	return render_template('page1.html')
	
#@app.route('/slides')  
#def slides():
#	return render_template('slides.html')
	
	
if __name__ == '__main__':    
	app.run(debug=True) 