from flask import Flask, render_template,request,redirect

app=Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>hellow world</h1>'
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/doLogin',methods=['POST'])
def doLogin():
    username=request.form['username']
    psw=request.form['psw']
    if username == "sujan" and psw == "sujan123":
        print(username)
        print(psw)
        return redirect('/')
    else:
        return redirect('/login')

if __name__=='__main__':
    app.run(debug=True)
