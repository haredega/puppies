from puppies import app
import os

#Starts Server
if __name__ == '__main__':
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    app.secret_key = 'super_secret_key'
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
