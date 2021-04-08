# Include our application
from app import app

# Define the port the application is running on
port = 8000

# When this script is run directly, start the flask application
if __name__ == "__main__":
    app.run(port=port)
