from flask import Flask,render_template 
from flask_bootstrap import Bootstrap
print("Test de modification pour Jenkins")
print("wa finallyyyyyyyy aaayyyy7")
print("waa lakhdmat")
print("lemail wslllty 3afakkhk")
app=Flask(__name__)
Bootstrap(app)
@app.route('/')
def home():
    return render_template("index.html")
if __name__ =='__main__':
    app.run(debug=True)

