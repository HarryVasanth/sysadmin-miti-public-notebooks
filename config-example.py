# Ip and port on which flask is gonna listen.
IP = '127.0.0.1'
PORT = 5000

# Base folder of the users' home directory. It's usually /home on linux and
# /Users on OSX.
HOME_FOLDER = "/Users"

# Folder where the jupyter notebook files are stored. It can be an empty string if you
# want to look for those files in the top level of the user home folder.
NB_FOLDER = "/public_notebooks"

# Considering the notebooks url as
# https://jupyterhub.example.org/public_notebooks/<username>
# the BASE_URL is /public_notebooks
BASE_URL="/public_notebooks"

# File extension used to filter jupyter notebook files
NB_EXT = '.ipynb'
