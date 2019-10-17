from os import path
from split_settings.tools import optional, include

if path.isfile('/home/vagrant/capelco-membership/envars/local'):
    env = 'local'
elif path.isfile('/home/vagrant/capelco-membership/envars/onprem'):
    env = 'onprem'
elif path.isfile('/home/vagrant/capelco-membership/envars/staging'):
    env = 'staging'
else:
    env ='prod'

include('apps.py')
include(f'environments/{env}.py')