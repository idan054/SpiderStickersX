from flask import Flask, render_template, request, redirect, url_for, flash
from Gadgets.beeper import beep
from Gadgets.multi_usage.bcolors import bcolors
from Scripts.A1_wooGetAPI import woocomarce_api, woo_api_get_processing
from Scripts.B1_complete_and_notifications import wooApi_mail_complete, complete_and_notifications
from mainApi import main_api
from popupDesign import locker_popupDesign

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session and flash messages

# Initialize global variables
global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output
processing_num_api = woo_api_get_processing()

@app.route('/')
def index():
    return render_template('index.html', processing_num_api=processing_num_api)

@app.route('/process_order', methods=['POST'])
def process_order():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

    order_number = request.form.get('orderLinkField')
    pack_number = request.form.get('packNum', 1)

    beep(2000, 300)
    beep(1000, 100)

    try:
        print("Closing old browser window, if any.")
        if browser:
            browser.quit()
            flash("Old browser window closed.", "success")
    except:
        flash("No old browser window to close.", "warning")

    api_output = main_api(numOrder=order_number, numOfPacks=pack_number)

    if len(api_output) == 2:  # Handle pickup scenario
        buyer_phone, locker_name = api_output
        flash(f"Local Pickup: Phone {buyer_phone}, Locker {locker_name}", "info")
        locker_popupDesign(root=None, buyer_phone=buyer_phone, locker_name=locker_name, order_number=order_number)
        wooApi_mail_complete(numOrder=order_number, buyer_name="", butikTrackNumber="", sendMailNeeded=False)
    else:  # Normal processing
        browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone = api_output
        flash("Order processed. Check details.", "success")

    return redirect(url_for('index'))

@app.route('/complete_order', methods=['POST'])
def complete_order():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

    try:
        complete_and_notifications(
            browser=browser,
            numOrder=request.form.get('orderLinkField'),
            buyer_name=buyer_name,
            butikTrackNumber=butikTrackNumber,
            buyer_phone=buyer_phone,
            butikBarCode=butikBarCode
        )
        flash("Order marked as complete and notifications sent.", "success")
    except Exception as e:
        flash(f"Error completing order: {str(e)}", "danger")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
