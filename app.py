from flask import Flask, request, jsonify, redirect, render_template
from selenium import webdriver
import time

app = Flask(__name__)

@app.route('/run_selenium', methods=['POST'])
def run_selenium():
    # Define the Selenoid capabilities with video recording enabled
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "117.0",
        "selenoid:options": {
            "enableVideo": True
    }
}


    try:
        # Create a remote WebDriver instance using Selenoid
        driver = webdriver.Remote(
            command_executor="http://34.29.17.54:4444/wd/hub",  # Replace with your Selenoid URL
            desired_capabilities=capabilities
        )

        # Navigate to a website, e.g., YouTube
        driver.get("https://www.youtube.com/watch?v=v5fZkAo-PpM")

        # Wait for a few seconds (e.g., 20 seconds)
        time.sleep(20)

        # Ensure that the WebDriver session is closed gracefully
        driver.quit()

        # Provide a success response
        return jsonify({'message': 'Selenium process completed successfully'})
    except Exception as e:
        # Provide an error response in case of any issues
        return jsonify({'error': str(e)})

@app.route('/selenoid_ui', methods=['GET'])
def selenoid_ui():
    # Redirect to the Selenoid UI URL
    selenoid_ui_url = "http://34.29.17.54:8080"  # Replace with your Selenoid UI URL
    return redirect(selenoid_ui_url)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
