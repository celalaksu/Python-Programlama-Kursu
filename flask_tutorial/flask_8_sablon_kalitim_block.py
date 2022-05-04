from flask import Flask,render_template
 
 
app = Flask(__name__)
 
@app.route("/")
def index():
 
    #return  render_template("sablon_index.html")
    #return  render_template("kalitim_index.html")
    return  render_template("block_kalitim_index.html")

@app.route("/hakkimizda")
def hakkimizda():
    return render_template("block_kalitim_hakkimizda.html")
    
 
if __name__ =="__main__":
    app.run(debug =True)