from flask import Flask, render_template, jsonify
import threading
import time

app = Flask(__name__)

# Possible status cycles
statuses = ["fa-check text-success", "fa-exclamation text-warning", "fa-question"]
status_data = ["fa-check text-success"] * 15  # Adjust number based on how many icons exist

def update_status():
    """Background thread to update statuses every 5 seconds"""
    global status_data
    index = 0
    while True:
        for i in range(len(status_data)):
            status_data[i] = statuses[(index + (i // 5)) % len(statuses)]
        index = (index + 1) % len(statuses)
        time.sleep(5)

@app.route('/')
def serve_dashboard():
    """Render the main HTML page"""
    return render_template('Pubmon_Dashboard.html')

@app.route('/status')
def get_status():
    """API endpoint to fetch current status values"""
    return jsonify(status_data)

# Start the background thread when Flask starts
threading.Thread(target=update_status, daemon=True).start()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')