#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import app, render_template, Flask
from config import datapath
import os
import re

app = Flask(__name__)

@app.route("/")
@app.route("/<path:s>")
def index(s=""):
    if re.match(r'^[0-9a-f]{64}$', s):
        try:
            datafile = os.path.join(datapath, s)
            with open(datafile, encoding="UTF-8") as f:
                contents = f.read()
            os.system("shred -u %s" % datafile)
            return render_template("something.html", contents=contents)
        except OSError:
            pass
    return render_template("nothing.html")

if __name__ == '__main__':
    app.run()
