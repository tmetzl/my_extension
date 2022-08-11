import os
from typing import Dict, List


def _jupyter_nbextension_paths() -> List[Dict[str, str]]:
    """Hook for telling Jupyter where our nbextensions are located

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing information about the nbextensions
    """
    here = os.path.dirname(__file__)
    return [
        dict(
            section="notebook",  # Where the extension is supposed to run (tree or notebook)
            src=os.path.join(
                here, "nbextensions", "notebook", "my_notebook_extension"
            ),  # Where the files of the extension are located
            dest="my_notebook_extension",  # How the extension should be called once it is installed
            require=os.path.join(
                "my_notebook_extension", "main"
            ),  # Relative path to the entry script (here main.js)
        ),
        dict(
            section="tree",
            src=os.path.join(here, "nbextensions", "tree", "my_tree_extension"),
            dest="my_tree_extension",
            require=os.path.join("my_tree_extension", "main"),
        ),
    ]


def _jupyter_server_extension_paths() -> List[Dict[str, str]]:
    """Hook for telling Jupyter where our server extensions are located

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing information about the server extensions
    """
    return [dict(module="my_extension.server_extensions.my_server_extension")]
