from flask import Flask
import os
app = Flask(__name__)

import puppies.views

#Starts Server
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
