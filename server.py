import webbrowser
import os
from flask import Flask, request
app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))
@app.route('/linkedin_api', methods=['GET'] )
def linkedin_api():
    input_string = request.args.get('input_string', default="material")
    url = "https://www.linkedin.com"
    webbrowser.open(url)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)