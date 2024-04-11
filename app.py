from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import secrets
import string
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['temple_bookings']
collection = db['bookings']

app = Flask(__name__, template_folder="template", static_url_path='/static')

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/kanaka_durgamma')
def kanaka_durgamma():
    return render_template("kanaka_durgamma.html")

@app.route('/tirupathi_deva')
def tirupathi_deva():
    return render_template("tirupathi_deva.html")

@app.route('/srilakshmitirupathiamma')
def srilakshmitirupathiamma():
    return render_template("srilakshmitirupathiamma.html")

@app.route('/save_booking', methods=['POST'])
def save_booking():
    booking_details = request.json
    result = collection.insert_one(booking_details)
    if result.inserted_id:
        return jsonify({'message': 'Booking details saved successfully!'}), 200
    else:
        return jsonify({'error': 'Failed to save booking details.'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
