
"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

import argparse, os, re, random, logging, json, pathlib
from pathlib import Path, PurePath
from string import Template


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


def component(args):
    componen_name  = args[0]
    component_path = args[1]
    component_type = args[2]
    text = args[3]
    path = os.path.join( component_path, "view.py" )
    write_file(path, text)
    path = os.path.join( component_path, "logic.py" )
    write_file(path, "'''code'''")


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
    root_component_path = os.path.abspath(os.path.join(APP_PATH, "core") )
    file_routing = open_file( os.path.join( root_component_path, "routing.py" ) )
    Path( component_path).mkdir(parents=True, exist_ok=True)
    _code_views = '''
"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

from flask import Blueprint, session, request, g, jsonify, current_app
from core.service.interface import MessageProtocol


${name}_bp = Blueprint('${name}_bp', __name__, url_prefix="/${name}")

class ${title_name}:
    def __init__(self, message: MessageProtocol):
        self.message = message

    def main(self) -> dict:
        return {"route": "${name}"}


@${name}_bp.route('/route', methods=["GET"])
def example():
    message = MessageProtocol(action="", status_code=200, message="", payload={})
    result = ${title_name}(message).main()
    response = MessageProtocol(
        message="Успешно", status_code=200, payload=result, action="")
    return jsonify(response.to_dict()), response.status_code
'''.strip()

    code_views = Template(_code_views).substitute(    
        name=component_name,
        title_name=component_name.title()
    )


    _code_routing = "from .${name}.view import ${name}_bp"

    code_routing = Template(_code_routing).substitute(    
        name=component_name,
        title_name=component_name.title()
    )


    def create_component():
        _files = [("view.py", code_views)]

        files = [ (component_name, component_path, x[0], x[1]) for x in _files ]
        list( map( lambda x: component(x) , files ) )

        routing_replace(file_routing, code_routing, component_name)


    create_component()
    log.info("Component %s was created", component_name)