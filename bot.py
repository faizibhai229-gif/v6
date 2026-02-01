import os
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
import requests
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_bot', methods=['POST'])
def create_bot():
    bot_name = request.form.get('bot_name')
    bot_description = request.form.get('bot_description')
    # Generate bot files
    generate_bot_files(bot_name, bot_description)
    return jsonify({'status': 'success', 'message': 'Bot created successfully'})

def generate_bot_files(bot_name, bot_description):
    slugified_name = bot_name.lower().replace(' ', '-')
    os.makedirs(slugified_name, exist_ok=True)
    # Generate bot.py
    with open(f'{slugified_name}/bot.py', 'w') as f:
        f.write(f'# {bot_name}\n\nprint("Hello, World!")\n')
    # Generate config.py
    with open(f'{slugified_name}/config.py', 'w') as f:
        f.write(f'# Configuration for {bot_name}\n\nBOT_NAME = "{bot_name}"\n')
    # Generate README.md
    with open(f'{slugified_name}/README.md', 'w') as f:
        f.write(f'# {bot_name}\n\n{bot_description}\n')
    # Generate requirements.txt
    with open(f'{slugified_name}/requirements.txt', 'w') as f:
        f.write('flask\ndotenv\nrequests\n')
    # Generate .env.example
    with open(f'{slugified_name}/.env.example', 'w') as f:
        f.write('# Environment Variables\n\nGITHUB_TOKEN=your_token_here\n')

if __name__ == '__main__':
    app.run(debug=True)
