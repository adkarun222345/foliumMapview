from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def show_map():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    return render_template('map.html', latitude=latitude, longitude=longitude)

if __name__ == '__main__':
    app.run(debug=True)
