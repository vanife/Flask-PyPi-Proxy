import os

os.environ["PYPI_PROXY_BASE_FOLDER_PATH"] = "./packages"
os.environ["PYPI_PROXY_LOGGING_PATH"] = "./_debug.log"
# os.environ['FLASK_PYPI_PROXY_CONFIG'] = 'config.json'
# os.environ['PYPI_PROXY_BASE_FOLDER_PATH'] = '/mnt/eggs/'
# os.environ['PYPI_PROXY_LOGGING_PATH'] = '/mnt/eggs/proxy.logs'

# if installed inside a virtualenv, then do this:
# activate_this = 'VIRTUALENENV_PATH/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))

from flask_pypi_proxy import app as application
application.run()