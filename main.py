from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True  




@app.route("/")
def index():  
    username_error = request.args.get("usernameerror")
    password_error = request.args.get("passworderror")
    verify_error = request.args.get("verifyerror")
    email_error = request.args.get("emailerror")
    username_giveback = request.args.get("usernameinput")
    email_giveback = request.args.get("emailinput")
    
    
    if not username_giveback:
        username_giveback = ""

    if not email_giveback:
        email_giveback = ""

    return render_template('home.html',
                            usernameerror=username_error and cgi.escape(username_error, quote=True),
                            passworderror=password_error and cgi.escape(password_error, quote=True),
                            verifyerror=verify_error and cgi.escape(verify_error, quote=True),
                            emailerror=email_error and cgi.escape(email_error, quote=True),
                            usernameinput=username_giveback and cgi.escape(username_giveback, quote=True),
                            emailinput=email_giveback and cgi.escape(email_giveback, quote=True))


@app.route("/welcome", methods=['POST'])
def welcome():   
    username_input = request.form['username']
    password_input = request.form['password']
    verify_input = request.form['verify']   
    email_input = request.form['email']

    usernameerror = ""
    passworderror  = ""
    verifyerror = ""
    emailerror = ""

    # validations to do
    if (not username_input) or (username_input.strip() == "" or (len(username_input) < 3) or (len(username_input) > 20)):
        usernameerror = "That's not a valid username"
    
    if (not password_input) or (password_input.strip() == "" or (len(password_input) < 3) or (len(password_input) > 20)):
        passworderror = "That's not a valid password"

    if (not verify_input) or (verify_input.strip() == ""):
        verifyerror = "That's not a valid verify"

    if (password_input != verify_input):
        verifyerror = "Passwords dont match"

    if (len(email_input) > 0):
        # validations  
        if (email_input.find("@") < 0):
            emailerror = "not a valid email"

        if (email_input.find(".") < 0):
            emailerror = "not a valid email"
        
    

    if(not usernameerror) and (not passworderror) and (not verifyerror) and (not emailerror):     
        return render_template('welcome.html', username=username_input and cgi.escape(username_input, quote=True))
    else:
        return redirect("/?usernameerror=" + usernameerror + "&passworderror=" + passworderror + "&verifyerror=" + verifyerror + "&emailerror=" + emailerror + "&usernameinput=" + username_input + "&emailinput=" + email_input)


app.run()