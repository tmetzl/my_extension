# my_extension
Example of a combined Jupyter nbextension and Jupyter server extension


# Install

First clone the repository or download it:

`git clone https://github.com/tmetzl/my_extension`

Open the main directory:

`cd my_extension`

Install the Python package:

`pip install .`

Activate the extensions:

```
jupyter serverextension enable --py my_extension --sys-prefix
jupyter nbextension install --py my_extension --sys-prefix
jupyter nbextension enable --py my_extension --sys-prefix
```