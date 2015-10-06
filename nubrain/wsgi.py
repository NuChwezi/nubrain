import os, sys

base = os.path.dirname(os.path.dirname(__file__))
base_parent = os.path.dirname(base)


# Remember original sys.path.
prev_sys_path = list(sys.path)

#new path...
sys.path.append(base)
sys.path.append(base_parent)

env_path = os.path.join(base, 'env/lib/python2.7/site-packages')

import site
site.addsitedir(env_path)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'nubrain.settings'


# Activate your virtual env
activate_env=os.path.join(base, 'env/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
