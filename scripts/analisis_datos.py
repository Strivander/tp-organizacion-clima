import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
ruta_datos = os.path.normpath(os.path.join(base_dir, '../datos/dataset.csv'))
ruta_grafico = os.path.normpath(os.path.join(base_dir, '../resultados/grafico_resultados.png'))

df = pd.read_csv(ruta_datos)
df.columns = [col.lower() for col in df.columns]

columna_fecha = 'date' if 'date' in df.columns else ('year' if 'year' in df.columns else df.columns[0])
columna_valor = 'mean' if 'mean' in df.columns else ('value' if 'value' in df.columns else df.columns[1])

df[columna_fecha] = pd.to_datetime(df[columna_fecha])

temp_promedio = df[columna_valor].mean()
temp_maxima = df[columna_valor].max()
temp_minima = df[columna_valor].min()

print("--- INDICADORES CLIMÁTICOS CALCULADOS ---")
print(f"Temperatura promedio historica (anomalia): {temp_promedio:.4f}")
print(f"Temperatura maxima registrada: {temp_maxima:.4f}")
print(f"Temperatura minima registrada: {temp_minima:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(df[columna_fecha], df[columna_valor], color='orange', label='Anomalia de Temperatura')
plt.title('Evolucion de la Temperatura Global')
plt.xlabel('Fecha')
plt.ylabel('Media de Anomalia de Temperatura')
plt.grid(True)
plt.legend()

plt.savefig(ruta_grafico)
print(f"El grafico se ha generado y guardado en: {ruta_grafico}!")