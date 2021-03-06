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
from part2 import*

app = Flask(__name__)

@app.route('/')  
def index(): 
	return render_template('part3.html')	#before the @app.route, define value (value= result of the functions), then add ex. values={}, then on html insert {{value[?]}}
	
@app.route('/result1')  
def result1():
	a=Number()
	result1=a.record()
	return render_template('result1.html', value={'rc': result1})

@app.route('/result2')  
def result2():
	a=Semantics()
	result2=a.record()
	return render_template('result2.html', value={'sm': result2})

@app.route('/result3')  
def result3():
	a=Genes()
	result3=a.record()
	return render_template('result3.html', value={'gn': result3})

@app.route('/result14')  
def result4():
	a=AssociatedGenes()
	result4=a.record()
	return render_template('result4.html', value={'ag': result4})
		
@app.route('/result5')  
def result5():
	a=Chromosomes()
	result5=a.record()
	return render_template('result5.html', value={'ch': result5})

@app.route('/result6')  
def result6():
	a=NumberOfGenes()
	result6=a.record()
	return render_template('result6.html', value={'ng': result6})

@app.route('/result7')  
def result7():
	a=PlusStrand()
	result7=a.record()
	return render_template('result7.html', value={'ps': result7})

@app.route('/result8')  
def result8():
	a=MinusStrand()
	result8=a.record()
	return render_template('result8.html', value={'ms': result8})	


#a=Number()
#b=Chromosomes()
#classes[a,b]

#for i in classes.size() :
#	@app.route('/result'+i)
#	def result(i):
#		result=classes[i].record()
#		return render_template('result'+i+'.html', value={classes[i].split(0,2) : result})

	
if __name__ == '__main__':    
	app.run(debug=True) 
