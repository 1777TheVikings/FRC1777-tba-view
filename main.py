from bottle import run, TEMPLATE_PATH, get, static_file, jinja2_view

import configuration as c


TEMPLATE_PATH[:] = ["static/templates"]


@get("/")
@jinja2_view('index.html')
def index():
    return {"team_logo_file": c.TEAM_LOGO_FILE}


@get("/static/<filename>")
def static(filename):
    return static_file(filename, root="./static")


run(host="0.0.0.0", port=8080)
