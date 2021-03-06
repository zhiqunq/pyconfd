import os
import sys
from jinja2 import Environment, FileSystemLoader

class EnvBackend(object):
    def get_values(self, env_vars, var):
        for env in env_vars:
            try:
                env_var = os.environ.get(env.values()[0])
                value = Environment().from_string(env_var).render(var)
                var[env.keys()[0]] = {'key': env_var, 'value': value }
            except AttributeError, e:
                raise RuntimeError("Missing environment variable %s" % (env.values()[0]))
            except:
                raise