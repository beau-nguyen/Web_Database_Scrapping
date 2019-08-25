from flask import Flask, render_template
# Import scrape_mars
import scrape_mars

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
#conn = 'mongodb://localhost:27017/mission_to_mars'

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
client = PyMongo(app)

# Set route
@app.route("/")
def index():
    mars = client.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Scrape 
@app.route("/scrape")
def scrape():
    mars = client.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data)
    return "Scraped!"

if __name__ == "__main__":
    app.run(debug=True)