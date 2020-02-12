import os

def downloadFile(app):
    record = os.path.join(app.root_path, app.config['records'])
    return record