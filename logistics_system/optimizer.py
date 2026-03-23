import math
import folium

# Simulated Coordinates (New York) for Route Optimization
LOCATIONS = {
    "HQ (Depot)": (40.7128, -74.0060),
    "Client A (Downtown)": (40.7061, -74.0092),
    "Client B (Midtown)": (40.7580, -73.9855),
    "Client C (Uptown)": (40.7829, -73.9654),
    "Client D (East Side)": (40.7306, -73.9866),
}

def haversine(coord1, coord2):
    """Calculates distance between two lat/lon points in km"""
    R = 6371  # Earth radius in km
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def optimize_route(selected_locations):
    """Greedy Nearest Neighbor Approach for Route Optimization (TSP heuristic)"""
    if "HQ (Depot)" not in selected_locations:
        selected_locations.insert(0, "HQ (Depot)")
        
    unvisited = selected_locations.copy()
    current = "HQ (Depot)"
    unvisited.remove(current)
    
    optimized_path = [current]
    total_distance = 0.0
    
    while unvisited:
        # Find nearest neighbor
        nearest = min(unvisited, key=lambda loc: haversine(LOCATIONS[current], LOCATIONS[loc]))
        total_distance += haversine(LOCATIONS[current], LOCATIONS[nearest])
        optimized_path.append(nearest)
        unvisited.remove(nearest)
        current = nearest
        
    # Return to HQ
    total_distance += haversine(LOCATIONS[current], LOCATIONS["HQ (Depot)"])
    optimized_path.append("HQ (Depot)")
    
    return optimized_path, round(total_distance, 2)

def generate_map(optimized_path):
    """Generates a Folium map showing the optimized route"""
    start_coord = LOCATIONS["HQ (Depot)"]
    m = folium.Map(location=start_coord, zoom_start=13)
    
    # Add Markers for each stop
    for i, loc in enumerate(optimized_path[:-1]):
        coord = LOCATIONS[loc]
        color = 'red' if loc == "HQ (Depot)" else 'blue'
        icon = 'home' if loc == "HQ (Depot)" else 'info-sign'
        
        folium.Marker(
            location=coord,
            popup=f"Stop {i}: {loc}",
            tooltip=f"{loc}",
            icon=folium.Icon(color=color, icon=icon)
        ).add_to(m)
        
    # Draw Lines connecting the path (Simulated Route/GPS Trajectory)
    path_coords = [LOCATIONS[loc] for loc in optimized_path]
    
    # A dashed line to show real-time GPS pathing
    folium.PolyLine(
        path_coords, 
        color="#2ecc71", 
        weight=5, 
        opacity=0.8,
        dash_array='10'
    ).add_to(m)
    
    # Return HTML string for Vercel Serverless (read-only filesystem)
    return m.get_root().render()
