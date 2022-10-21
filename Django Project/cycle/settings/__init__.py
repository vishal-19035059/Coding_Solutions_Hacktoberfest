import os 
from dotenv import load_dotenv

load_dotenv()



if os.environ.get('WEBSITE_MODE') == 'prod':
    from .prod import *
else:
    from .dev import *