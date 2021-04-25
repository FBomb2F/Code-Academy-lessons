weight = 41.5
cost_ground_premium = 125.00
# Ground Shipping

if weight <= 2:
  price_per_pound = 1.50
elif weight <= 6:
  price_per_pound = 3.00
elif weight <= 10:
  price_per_pound = 4.00
else:
  price_per_pound = 4.75

  
print("Your Shipping Cost is: $", 20 + price_per_pound * weight)
print("Ground Shipping Premium: $",cost_ground_premium)

# Drone Shipping


if weight <= 2:
  drone_price_per_pound = 4.5
elif weight <= 6:
  drone_price_per_pound = 9.00
elif weight <= 10:
  drone_price_per_pound = 12.00
else:
  drone_price_per_pound = 14.25

print("Your Drone Shipping Cost is: $", drone_price_per_pound * weight)
