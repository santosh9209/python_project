from flask import Flask, render_template, request, redirect, url_for
import os
from logistics_system.services import FleetService
from logistics_system.validators import validate_capacity, DuplicateVehicleError
from logistics_system.optimizer import LOCATIONS, optimize_route, generate_map

app = Flask(__name__)
service = FleetService()

# Ensure directories exist
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

@app.route('/')
def index():
    fleet = service.get_all()
    # Read the analytics chart if it exists
    chart_exists = os.path.exists("static/fleet_status_chart.png")
    map_exists = os.path.exists("templates/route_map.html")
    
    # Load Route Summary text if exists
    route_summary = ""
    if os.path.exists("static/route_summary.txt"):
        with open("static/route_summary.txt", "r") as f:
            route_summary = f.read()
    
    # Generate an initial blank map if it doesn't exist
    if not map_exists:
        try:
            generate_map(["HQ (Depot)", "Client A (Downtown)"])
        except:
            pass
            
    return render_template('index.html', fleet=fleet, locations=list(LOCATIONS.keys()), route_summary=route_summary, chart_exists=chart_exists)

@app.route('/add', methods=['POST'])
def add_vehicle():
    v_id = request.form.get('v_id').upper()
    driver = request.form.get('driver').title()
    capacity = request.form.get('capacity')
    
    try:
        cap_val = validate_capacity(capacity)
        service.add_vehicle(v_id, driver, cap_val)
    except Exception as e:
        print(f"Error adding vehicle: {e}")
        
    return redirect(url_for('index'))

@app.route('/optimize', methods=['POST'])
def run_optimization():
    # Get selected locations from form checkboxes
    selected = request.form.getlist('locations')
    if not selected:
        # Default all if none selected
        selected = list(LOCATIONS.keys())
        
    # Run the optimization algorithm (TSP)
    best_route, distance = optimize_route(selected)
    
    # Generate folium Map HTML
    generate_map(best_route)
    
    # Save the route summary to a text file
    with open("static/route_summary.txt", "w") as f:
        f.write(f"Optimized Path: {' -> '.join(best_route)}\n")
        f.write(f"Total Ground Distance: {distance} km\n")
        f.write(f"Est. Travel Time: {round((distance / 40)*60)} mins (with live traffic)")
        
    return redirect(url_for('index'))

@app.route('/analytics', methods=['POST'])
def run_analytics():
    from logistics_system.analytics import generate_fleet_report
    generate_fleet_report(service.get_all())
    if os.path.exists("fleet_status_chart.png"):
        os.replace("fleet_status_chart.png", "static/fleet_status_chart.png")
    return redirect(url_for('index'))

@app.route('/map')
def view_map():
    return render_template('route_map.html')

if __name__ == '__main__':
    print("\n" + "="*70)
    print("Dynamic Route Optimizer running on: http://127.0.0.1:5000")
    print("="*70 + "\n")
    app.run(debug=True, port=5000)
