from flask_frozen import Freezer
from your_flask_app import app  # Import your Flask app

freezer = Freezer(app)

@freezer.register_generator
def my_view():
    # Example: return the URLs you want to freeze
    yield 'index'  # Replace with your view name
    # Add more views as needed

if __name__ == '__main__':
    freezer.freeze()
