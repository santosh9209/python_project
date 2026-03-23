# Week 12: Analytics (NumPy, Pandas, Matplotlib)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def generate_fleet_report(fleet_dict):
    if not fleet_dict:
        print("No fleet data available for analytics.")
        return

    # Convert dictionary of objects to Pandas DataFrame
    data = []
    for v_id, vehicle in fleet_dict.items():
        data.append({
            "Vehicle_ID": v_id,
            "Driver": vehicle.driver_name,
            "Capacity": vehicle.capacity_tons,
            "Status": vehicle.status
        })
    
    df = pd.DataFrame(data)
    
    print("\n--- Fleet Analytics Summary ---")
    print(f"Total Vehicles: {len(df)}")
    print(f"Total Fleet Capacity: {np.sum(df['Capacity'])} tons")
    print(f"Average Capacity: {np.mean(df['Capacity']):.2f} tons")
    
    # Generate a Matplotlib Chart
    try:
        status_counts = df['Status'].value_counts()
        plt.figure(figsize=(6, 4))
        status_counts.plot(kind='bar', color=['blue', 'orange', 'green'])
        plt.title('Fleet Status Distribution')
        plt.xlabel('Status')
        plt.ylabel('Number of Vehicles')
        plt.tight_layout()
        
        # Save chart to /tmp/ for Vercel serverless
        chart_path = "/tmp/fleet_status_chart.png"
        plt.savefig(chart_path)
        print(f"Analytics chart saved to {chart_path}")
    except Exception as e:
        print(f"Failed to generate chart: {e}")
