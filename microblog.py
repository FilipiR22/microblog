from app import app
import os

if __name__ =='main':
    port = int(os.getenv('PORT'))
    app.run(host='0.0.0.0', port = port)