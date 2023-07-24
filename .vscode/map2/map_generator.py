import folium
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def generate_map():
    lat = float(request.form['latitude'])
    lon = float(request.form['longitude'])
    
    # Create a map centered at the given coordinates
    map_obj = folium.Map(location=[lat, lon], zoom_start=10)
    
    # Add a marker to the map
    folium.Marker([lat, lon], popup='Coordinates').add_to(map_obj)
    
    # Save the map as an HTML file
    map_obj.save('templates/map.html')
    
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
