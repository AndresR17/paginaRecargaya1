from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/aliados')
def aliados():
    return render_template('sitio/aliados.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admi/aliados')
def admin_aliados():
    return render_template('admin/aliados.html')

if __name__ =='__main__':
    app.run(debug=True)