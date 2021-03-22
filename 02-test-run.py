""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
#from instapy import smart_run
#from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# login credentials
insta_username = 'johnjohnmanjohn'
insta_password = 'MQgbyFRfnb8Ar29'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  geckodriver_path='/home/naser/work-area/selanium/geckodriver')

with smart_run(session):
  """ Activity flow """	
   
