"""
Script to modify CC_GENERAL.csv dataset
This simulates receiving updated data with new customers
"""
import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_csv('data/CC_GENERAL.csv')

print(f"Original dataset shape: {df.shape}")
print(f"Original number of customers: {len(df)}")

# Create 5 new synthetic customer records
new_customers = pd.DataFrame({
    'CUST_ID': ['C99998', 'C99997', 'C99996', 'C99995', 'C99994'],
    'BALANCE': [5000.50, 3500.75, 4200.00, 2800.25, 6100.90],
    'BALANCE_FREQUENCY': [0.9, 0.85, 0.95, 0.80, 1.0],
    'PURCHASES': [1200.75, 950.50, 1500.00, 800.25, 2000.50],
    'ONEOFF_PURCHASES': [500.00, 400.00, 600.00, 300.00, 800.00],
    'INSTALLMENTS_PURCHASES': [700.75, 550.50, 900.00, 500.25, 1200.50],
    'CASH_ADVANCE': [150.25, 200.00, 100.50, 250.75, 0.00],
    'PURCHASES_FREQUENCY': [0.8, 0.75, 0.9, 0.7, 0.95],
    'ONEOFF_PURCHASES_FREQUENCY': [0.5, 0.45, 0.6, 0.4, 0.7],
    'PURCHASES_INSTALLMENTS_FREQUENCY': [0.6, 0.55, 0.7, 0.5, 0.8],
    'CASH_ADVANCE_FREQUENCY': [0.1, 0.15, 0.05, 0.2, 0.0],
    'CASH_ADVANCE_TRX': [2, 3, 1, 4, 0],
    'PURCHASES_TRX': [15, 12, 18, 10, 20],
    'CREDIT_LIMIT': [10000, 8500, 12000, 7000, 15000],
    'PAYMENTS': [1500.50, 1200.00, 1800.75, 900.50, 2200.00],
    'MINIMUM_PAYMENTS': [800.25, 650.00, 900.50, 550.25, 1000.00],
    'PRC_FULL_PAYMENT': [0.3, 0.25, 0.35, 0.2, 0.4],
    'TENURE': [12, 12, 12, 12, 12]
})

# Append new customers to the dataset
df_updated = pd.concat([df, new_customers], ignore_index=True)

print(f"\nUpdated dataset shape: {df_updated.shape}")
print(f"Updated number of customers: {len(df_updated)}")
print(f"New customers added: {len(new_customers)}")

# Save the updated dataset
df_updated.to_csv('data/CC_GENERAL.csv', index=False)

print("\n✅ Dataset updated successfully!")
print("🔹 Added 5 new customer records")
print("🔹 Ready to track as Version 2 with DVC")

