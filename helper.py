
"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

import argparse, os, re, random, logging, json, pathlib
from pathlib import Path, PurePath
from string import Template
import os
import random
from datetime import datetime

license = f'''
"""
Copyright {datetime.now().year} Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
'''.strip()

# Enable logging
logging.basicConfig(format='[ %(asctime)s ]  %(name)s - %(levelname)s : %(message)s',
                    level=logging.INFO)

log = logging.getLogger(__name__)


PATH = os.getcwd()
APP_PATH = os.path.join( PATH, "app" )


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    description='Автоматизация различных задач для приложения:\n - создать отображение'
)

parser.add_argument('-c','--component', dest='component', type=str, 
    help='Создать отображение:\npython3 helper.py --component test')

args = parser.parse_args()
root_component_path = os.path.abspath(os.path.join(APP_PATH, "core") )

def write_file(path, content=""):
    if isinstance(content, bytes):
        with open(path, "wb") as f:
            f.write(content)
    else:
        with open(path, "w", encoding="utf8") as f:
            f.write(content)

def open_file(path):
    with open(path, "r", encoding="utf8") as f:
        data = f.read()
    return data


def routing_replace(_file_routing, _code_routing, _component_name):
    _c_name = "{}_bp".format(_component_name)

    if not len(_file_routing) or _file_routing[0] == "R":
        _file_routing = _code_routing + "\n\n\nRoutes = [{}]".format(_c_name)
    else:
        rows = _file_routing.split("\n")
        rows.insert(rows.index(""), _code_routing)
        rows[-1] = rows[-1].replace("]", ", {}]".format(_c_name))
        _file_routing = "\n".join(rows)
    path = os.path.join( root_component_path, "routing.py" )
    write_file( path, _file_routing )

if args.component:
    args.component = args.component.replace("-","_")
    component_name = os.path.split(args.component)[-1]
    component_path = os.path.join( APP_PATH, "core", args.component)
    templates_path = os.path.join(component_path, "templates")
    static_path    = os.path.join(component_path, "static")
    file_routing = open_file( os.path.join( root_component_path, "routing.py" ) )
    random_color = "%06x" % random.randint(0, 0xFFFFFF)
    Path(component_path).mkdir(parents=True, exist_ok=True)
    Path(templates_path).mkdir(parents=True, exist_ok=True)
    Path(static_path).mkdir(parents=True, exist_ok=True)
    _code_views = '''
${license}

from flask import Blueprint, session, request, g, jsonify, current_app, render_template
from core.service.interface import MessageProtocol


${name}_bp = Blueprint('${name}', __name__, 
    url_prefix="/${name}",
    template_folder="templates",
    static_folder="static",
)

@${name}_bp.route('/')
def index():
    return render_template("${name}.html")
'''.strip()

    _index_html = r'''
{% extends "base.html" %}


{% block head %}
  <link rel="stylesheet" href="{{ url_for('${name}.static', filename='style.css')}}">
{% endblock %}

{% block body %}

    <p class="text-bg">${name} page</p>

{% endblock %}


{% block script %}
  <script src="{{ url_for('${name}.static', filename='main.js')}}"></script>
{% endblock %}
'''.strip()
    
    _main_js = r'''
console.log("Script ${name}/static/main.js loaded for page ${name}.html");
'''.strip()
    
    _style = '''
.text-bg {
    background-color: #${color};
}
'''.strip()

    _logic = """
${license}

'''your code'''
""".strip()


    logic = Template(_logic).substitute(license=license)
    code_views = Template(_code_views).substitute(name=component_name, license=license)
    index_html = Template(_index_html).substitute(name=component_name)
    main_js = Template(_main_js).substitute(name=component_name)
    style = Template(_style).substitute(color=random_color)


    _code_routing = "from .${name}.view import ${name}_bp"
    code_routing = Template(_code_routing).substitute(name=component_name)

    items = [
        (os.path.join(component_path, "view.py"), code_views), 
        (os.path.join(component_path, "logic.py"), logic), 
        (os.path.join( templates_path, component_name + ".html" ), index_html),
        (os.path.join( static_path, "main.js" ), main_js),
        (os.path.join( static_path, "style.css" ), style),
    ]

    for item in items:
        path = item[0]
        data = item[1]
        write_file(path, data)


    routing_replace(file_routing, code_routing, component_name)
    log.info("Component %s was created", component_name)