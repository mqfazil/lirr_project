import pandas as pd
import matplotlib.pyplot as plt

#loads CSV
data = pd.read_csv('lirr_otp.csv')

#peek at data
print("First 5 rows:")
print(data.head())
print("Columns:", data.columns.tolist())

#delay % = (1 - OTP) * 100
data['Delay %'] = (1 - data['OTP']) * 100

#average delays by branch
delay_by_branch = data.groupby('Branch / Line')['Delay %'].mean()

#bar chart
bars = plt.bar(delay_by_branch.index, delay_by_branch.values, color='skyblue')
plt.title('Average LIRR Delays by Branch (2015-2025)')
plt.xlabel('Branch')
plt.ylabel('Average Delay %')
plt.xticks(rotation=45)
plt.tight_layout()

#adds bold black text on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.1f}', 
             ha='center', va='bottom', color='black', weight='bold')

plt.show()

#worst branch
worst_branch = delay_by_branch.idxmax()
worst_value = delay_by_branch.max()
print(f"Worst branch: {worst_branch} with {worst_value:.1f}% avg delay")