from flask import Flask, request, jsonify
from Email import send_email

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    # Handle sending message logic here
    data = request.json
    # Initialize Selenium WebDriver (assuming you have installed the appropriate WebDriver for your browser)
    # driver = webdriver.Chrome()  # Example: using Chrome WebDriver
    # driver.get("https://example.com")
    # driver.quit()
    #execute()  # Call your other function
    send_email()
    return jsonify({"message": "Message sent successfully"})

@app.route('/')
@app.route('/home')
def home():
    return "Hope you like my web app"

if __name__ == '__main__':
    app.run(port=5005)