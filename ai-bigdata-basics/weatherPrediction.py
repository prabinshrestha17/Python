# import libraries 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
import os 
import numpy as np

# option: check if file exist and provide helpful error message

data = r"C:\Users\SAU\Downloads\korea_weather.xlsx"
print(data)

# create sample weather data

dates = pd.date_range(start='2023-01-01', periods=365,freq='D')
temps = 15+10*np.sin(2*np.arange(365)/365)+np.random.normal(0,2,365)

data = pd.DataFrame({
    'datetime':dates,
    'temp':temps
})
print("Sample data creates sucessfully")


data['datetime'] = pd.to_datetime(data['datetime'])

# create numeric days 

data['day_number'] = range(len(data))
# features 
x = data[['day_number']]
y = data['temp']
model = LinearRegression()
model.fit(x, y)

future_days = [[len(data) + i] for i in range(1, 8)]

predictions = model.predict(future_days)

print("Future Temperature predictions:\n" )

for i, temp in enumerate(predictions, start=1):
    print(f"Day +{i}: {temp:.2f}C")


# plot graph 


plt.figure(figsize=(10, 5))
plt.plot(data['day_number'], y, label="Acutal Temperature")
plt.plot(
    future_days, 
    predictions, 
    marker = 0,
    label = "Predicted Temperature"
)
plt.xlabel("Day Number")
plt.ylabel("Temperature (C)")
plt.title("Seoul weather prediction ")