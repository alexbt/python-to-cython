import os

from flask import Flask

from abt import other

flask_app = Flask(__name__)


def start(source: str):
    @flask_app.route('/')
    def index():
        files_root = [f for f in os.listdir('.') if os.path.isfile(f)]
        files_abt = [f for f in os.listdir('./abt') if os.path.isfile(f"./abt/{f}")]
        return {
            "files_on_disk":{
                "./": files_root,
                "./abt": files_abt,
            },
            "filenames_programmatically": {
                "app": source,
                "other": other.get_filename(),
                "my_flask": __file__
            }
        }

    flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    flask_app.run(host="0.0.0.0", port=8090)
