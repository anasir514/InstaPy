""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# login credentials
insta_username = ''
insta_password = ''

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  geckodriver_path='/home/naser/work-area/selanium/geckodriver')

with smart_run(session):
  """ Activity flow """		
  # general settings		
#  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # set up all the settings
 # session.set_relationship_bounds(enabled=True,
#				 potency_ratio=-1.21,
#				  delimit_by_numbers=True,
#				   max_followers=4590,
#				    max_following=5555,
#				     min_followers=45,
#				      min_following=77)
  
  #session.set_do_comment(True, percentage=10)
  session.set_do_follow(enabled=True, percentage=100)

  session.set_do_comment(enabled=True, percentage=100)
  session.set_do_like(True, percentage=100)
  session.interact_by_users([''], amount=100, randomize=True)
  #session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
#  session.set_dont_include(['friend1', 'friend2', 'friend3'])
#  session.set_dont_like(['pizza', 'girl'])

# do the actual liking
#  session.like_by_tags(['natgeo', 'world'], amount=50)

# default enabled=False, ~ every 4th image will be commented on

#  session.set_do_comment(enabled=True, percentage=25)
  #session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])

# you can also set comments for specific media types (Photo / Video)

#  session.set_comments(['Nice shot!'], media='Photo')
#  session.set_comments(['Great Video!'], media='Video')

# and you can add the username of the poster to the comment by using

#  session.set_comments(['Nice shot! @{}'], media='Photo')

#  session.set_user_interact(amount=4,
#				 percentage=50,
#                  randomize=True,
#                   media='Photo')
  
  #session.follow_by_list(followlist=['samantha3', 'larry_ok'], times=2, sleep_delay=600, interact=True)

# default sleep_delay=600 (10min) for every 10 user following, in this case
# sleep for 60 seconds

#  session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, sleep_delay=60)


# default sleep_delay=600 (10min) for every 10 user following, in this case
# sleep for 60 seconds

#  session.follow_user_following(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, sleep_delay=60)



# For 50% of the 30 newly followed, move to their profile
# and randomly choose 5 pictures to be liked.
# Take into account the other set options like the comment rate
# and the filtering for inappropriate words or users

#  session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
#  session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, interact=True)

# Follow user based on hashtags (without liking the image)

#  session.follow_by_tags(['goal', 'gains'], amount=10)

# This will follow the people those liked photos of given list of users

#  session.follow_likers (['@{}'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)

  # Joining Engagement Pods
#  session.set_do_comment(enabled=True, percentage=35)
#  session.set_comments(comments)
#  session.join_pods(topic='sports', engagement_mode='no_comments')
