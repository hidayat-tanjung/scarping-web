import pywebcopy
from pywebcopy import save_website

kwargs = {'project_name': 'talalsite'} # it will create a folder in desired folder with name 'talalsite'

save_website(
    url='https://www.abc.com/',
    project_folder='D:/Talal/game',
    **kwargs
)