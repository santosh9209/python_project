from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import json
from logistics_system.services import FleetService
from logistics_system.validators import validate_capacity, DuplicateVehicleError
from logistics_system.optimizer import LOCATIONS, optimize_route, generate_map

app = Flask(__name__)
service = FleetService()

TMP_DIR = "/tmp"
CHART_PATH = os.path.join(TMP_DIR, "fleet_status_chart.png")
ROUTE_SUMMARY_PATH = os.path.join(TMP_DIR, "route_summary.txt")
ROUTE_DATA_PATH = os.path.join(TMP_DIR, "current_route.json")

# Ensure /tmp exists (mostly for local testing, Vercel has it natively mounted)
os.makedirs(TMP_DIR, exist_ok=True)
# Ensure templates directory exists for Vercel build mapping
os.makedirs('templates', exist_ok=True)

@app.route('/')
def index():
    fleet = service.get_all()
    chart_exists = os.path.exists(CHART_PATH)
    
    route_summary = ""
    if os.path.exists(ROUTE_SUMMARY_PATH):
        with open(ROUTE_SUMMARY_PATH, "r") as f:
            route_summary = f.read()
            
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
    selected = request.form.getlist('locations')
    if not selected:
        selected = list(LOCATIONS.keys())
        
    best_route, distance = optimize_route(selected)
    
    with open(ROUTE_DATA_PATH, "w") as f:
        json.dump(best_route, f)
    
    with open(ROUTE_SUMMARY_PATH, "w") as f:
        f.write(f"Optimized Path: {' -> '.join(best_route)}\n")
        f.write(f"Total Ground Distance: {distance} km\n")
        f.write(f"Est. Travel Time: {round((distance / 40)*60)} mins (with live traffic)")
        
    return redirect(url_for('index'))

@app.route('/analytics', methods=['POST'])
def run_analytics():
    from logistics_system.analytics import generate_fleet_report
    generate_fleet_report(service.get_all())
    return redirect(url_for('index'))

@app.route('/map')
def view_map():
    if os.path.exists(ROUTE_DATA_PATH):
        try:
            with open(ROUTE_DATA_PATH, "r") as f:
                best_route = json.load(f)
        except:
            best_route = ["HQ (Depot)", "Client A (Downtown)"]
    else:
        best_route = ["HQ (Depot)", "Client A (Downtown)"]
        
    # generate_map now returns HTML string thanks to previous refactoring
    html_output = generate_map(best_route)
    return html_output

@app.route('/chart.png')
def view_chart():
    if os.path.exists(CHART_PATH):
        return send_file(CHART_PATH, mimetype='image/png')
    return "", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
