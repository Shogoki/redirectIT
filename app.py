from flask import Flask, redirect
import re

app = Flask(__name__)

def get_new_url(old_url):
    #adding a leading www.
    match = re.search(r'(https?://)(.+)', old_url)
    if(not (match.group(2).startswith('www'))):
        new_url = match.group(1) + 'www.' + match.group(2) 
    return   new_url 

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all():
    new_url = get_new_url(request.url)
    if(new_url != request.url):
        return redirect(new_url, code=302)
    else:
        return "nothing to redirect"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)