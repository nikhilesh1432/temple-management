from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

client = MongoClient('mongodb+srv://santhoshpodili874:SANTHU@7981@cluster0.rz2dqev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['temple_bookings']
collection = db['bookings']

app = Flask(__name__, template_folder="template", static_url_path='/static')

@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/confirmation')
def confirmation():
    booking_details = collection.find_one() 
    return render_template('confirmation.html', booking_details=booking_details)
    
@app.route('/paid_payment')
def paid_payment():
    return render_template('paidpayment.html')
    
@app.route('/kanaka_durgamma')
def kanaka_durgamma():
    return render_template("kanaka_durgamma.html")

@app.route('/tirupathi_deva')
def tirupathi_deva():
    return render_template("tirupathi_deva.html")

@app.route('/srilakshmitirupathiamma')
def srilakshmitirupathiamma():
    return render_template("srilakshmitirupathiamma.html")

@app.route('/paiddarshan')
def paid_darshan():
    return render_template("paiddarshan.html")

@app.route('/free_darshan')
def free_darshan():
    return render_template("free_darshan.html")

@app.route('/vehicle')
def vehicle_parking():
    return render_template("vehicle.html")

@app.route('/roombooking')
def room_booking():
    return render_template("roombooking.html")

@app.route('/prasadbooking')
def prasad_booking():
    return render_template("prasadbooking.html")

@app.route('/vip_darshan')
def vip_darshan():
    return render_template("vip_darshan.html")

@app.route('/foodbooking')
def food_booking():
    return render_template("foodbooking.html")

@app.route('/taxibooking')
def taxi_booking():
    return render_template("taxibooking.html")

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
