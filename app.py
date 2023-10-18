from flask import Flask, render_template
import time
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_process():
    # Your Selenium script here
    driver = webdriver.Chrome()
    driver.get("https://www.indeed.com")
    time.sleep(5)  # Add a delay
    driver.quit()
    return 'Process Started'

if __name__ == '__main__':
    app.run(debug=True)
