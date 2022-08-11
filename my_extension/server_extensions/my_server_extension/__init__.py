import json
import os

from notebook.base.handlers import IPythonHandler
from notebook.utils import url_path_join as ujoin
from tornado import web
from traitlets.config import LoggingConfigurable


class UserNameHandler(IPythonHandler):
    def get(self):
        user = os.getenv("JUPYTERHUB_USER")
        if user is None:
            user = os.getenv("USER")
        self.write(json.dumps(dict(user=user)))


class MyServerExtension(LoggingConfigurable):

    static_path = os.path.join(os.path.dirname(__file__), "static")

    def __init__(self, nbapp):
        self.webapp = nbapp.web_app

    def get_handlers(self):
        return [
            (
                r"/myextension/static/(.*)",  # Where is the handler exposed?
                web.StaticFileHandler,  # The handler class
                {"path": self.static_path},  # Additional arguments
            ),
            (r"/myextension/api/user", UserNameHandler),
        ]

    def load(self):
        def rewrite(x):
            pat = ujoin(self.webapp.settings["base_url"], x[0].lstrip("/"))
            return (pat,) + x[1:]

        self.webapp.add_handlers(".*$", [rewrite(x) for x in self.get_handlers()])


def load_jupyter_server_extension(nbapp):
    nbapp.log.info("Loading my server extension!")
    myextension = MyServerExtension(nbapp)
    myextension.load()
