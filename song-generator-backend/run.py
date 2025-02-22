import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use the PORT environment variable or default to 10000
    app.run(host='0.0.0.0', port=port)  # Set host to '0.0.0.0' to allow external access
