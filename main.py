from bottle import run, TEMPLATE_PATH, get, static_file, jinja2_view


TEMPLATE_PATH[:] = ["static/templates"]


@get("/")
@jinja2_view('index.html')
def index():
    return {}


@get("/static/<filename>")
def static(filename):
    return static_file(filename, root="./static")


run(host="0.0.0.0", port=8080)
