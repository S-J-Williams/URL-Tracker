from flask import Flask, redirect, url_for
app = Flask(__name__)

def validLink(token):
    tokens = []
    users = []
    with open('tokens.txt', 'r') as file:
        for line in file:
            tokens.append(line[:-1])
    with open('users.txt', 'r') as file:
        for line in file:
            users.append(line[:-1])
    
    for x in tokens:
        if(x == token):
            print('HIT!')
            print(x)
 #Open file of tokens
 #check if valid token
 #Mark opened is found
 #else nothing



@app.route('/<token>/')
def webServer(token):
    validLink(token)
    print('URL Hit, Token: %s' % token)
    return 'URL Hit, Token: %s' % token

if __name__ == '__main__':
    app.run(debug = True)