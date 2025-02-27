from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Serve the main dashboard
@app.route('/')
def serve_dashboard():
    return render_template('Pubmon_Dashboard.html')

# Serve static files (CSS, JS, etc.)
@app.route('/static/<path:filename>')
def serve_assets(filename):
    assets_folder = os.path.join(app.root_path, 'static')
    return send_from_directory(assets_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)