import os
class path:
    baseDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config = os.path.join(baseDir, 'config.yml')
    log = os.path.join(baseDir, 'logs')
    modules = os.path.join(baseDir, 'modules')