# app.py
from flask import Flask, render_template
import yaml

app = Flask(__name__)

# Load configuration from YAML file
with open('config.yml', 'r') as yaml_file:
    config = yaml.load(yaml_file, Loader=yaml.FullLoader)

@app.route('/')
def index():
    return render_template('index.html', title=config['title'], message=config['message'])

if __name__ == '__main__':
    app.run(debug=True)
