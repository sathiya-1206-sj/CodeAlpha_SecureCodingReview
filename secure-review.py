from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.secret_key = "hardcoded_secret"

@app.route("/", methods=["GET"])
def home():
    return '''
    <h2>Login Page</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>    '''

@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerable code
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        return "Login Success"
    else:
        return "Login Failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True)