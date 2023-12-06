import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані з CSV-файлу
df = pd.read_csv("HN.csv", encoding = "latin1")

# Фільтруємо дані для України та Німеччини
ukraine_data = df[df['Country Name'] == 'Ukraine']
germany_data = df[df['Country Name'] == 'Germany']

# Створюємо графіки
plt.figure(figsize=(15, 5))

# 2.1 Графіки для динаміки показників для України та Німеччини
plt.plot(list(ukraine_data.columns[5:]), list(ukraine_data.iloc[0][5:]), label='Ukraine')
plt.plot(list(germany_data.columns[5:]), list(germany_data.iloc[0][5:]), label='Germany')

plt.xlabel('Year')
plt.ylabel('HIV Adults (15+)')
plt.title('HIV Adults (15+) Dynamics: Ukraine vs Germany')
plt.legend()
plt.show()

# 2.2 Стовпчасті діаграми для значень показника для обраної країни
selected_country = input('Enter the country name (Ukraine or Germany): ')

if selected_country.lower() == 'ukraine':
    plt.figure(figsize=(8, 5))
    plt.bar(list(ukraine_data.columns[5:]), [int(x) for x in list(ukraine_data.iloc[0][5:])], color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('HIV Adults (15+)')
    plt.title(f'HIV Adults (15+) in Ukraine')
    plt.show()
elif selected_country.lower() == 'germany':
    plt.figure(figsize=(8, 5))
    plt.bar(list(germany_data.columns[5:]), [int(x) for x in list(germany_data.iloc[0][5:])], color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('HIV Adults (15+)')
    plt.title(f'HIV Adults (15+) in Germany')
    plt.show()
else:
    print('Invalid country name. Please enter either "Ukraine" or "Germany".')
