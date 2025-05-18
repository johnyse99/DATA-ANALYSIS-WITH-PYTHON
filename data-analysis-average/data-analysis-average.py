import pandas as pd

# 1. Cargar los datos desde el archivo CSV
df = pd.read_csv("Copy your path of file")

# 2. Eliminar registros con valores faltantes
df.dropna(inplace=True)

# 3. Calcular el Salary Increase
df['Salary Increase'] = ((df['Average Experienced Salary'] - df['Average Entry-Level Salary']) / df['Average Entry-Level Salary']) * 100

# 4. Encontrar la carrera con mayor Salary Increase
index_max = df['Salary Increase'].idxmax()
career_highest_increase = df.loc[index_max, 'Career']
highest_increase_value = df.loc[index_max, 'Salary Increase']

# 5. Imprimir resultados
print(f"The career with the highest salary increase is: {career_highest_increase}")
print(f"Salary Increase: {highest_increase_value:.2f}%")