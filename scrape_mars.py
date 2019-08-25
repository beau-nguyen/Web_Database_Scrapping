# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup

   # Windows user initializing Splinter here...
def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    # Run the function below:
    first_title, first_paragraph = mars_news(browser)
    
    # Run the functions below and store into a dictionary
    results = {
        "title": first_title,
        "paragraph": first_paragraph,
        "image_URL": jpl_image(browser),
        "weather": mars_weather_tweet(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemis(browser),
    }

    # Quit the browser and return the scraped results
    browser.quit()
    return results

def mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

    # Scrape the first article title and teaser paragraph text; return them
    first_title = mars_news_soup.find('div', class_='content_title').text
    first_paragraph = mars_news_soup.find('div', class_='article_teaser_body').text
    return first_title, first_paragraph


def mars_weather_tweet(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')
    
    # Scrape the tweet info and return
    first_tweet = tweet_soup.find('p', class_='TweetTextSize').text
    return first_tweet
    
def mars_facts():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Property', 'Value']
    # Set index to property in preparation for import into MongoDB
    df.set_index('Property', inplace=True)
    
    # Convert to HTML table string and return
    return df.to_html()
    