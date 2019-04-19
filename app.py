from flask import Flask, redirect
import re

app = Flask(__name__)

def get_new_url(old_url):
    #removing the leading  www.
    return   re.sub(r'(https?://)www\.', r'\1', old_url)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all():
    new_url = get_new_url(request.url)
    return redirect(new_url, code=302)
