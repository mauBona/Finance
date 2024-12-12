import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
import os

# Calcola il range temporale
end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=1*365)).strftime("%Y-%m-%d")

# Definizione dei simboli
vix_symbol = "^VIX"
sp500_symbol = "^GSPC"

# Scarica i dati per VIX e S&P500
vix_data = yf.download(vix_symbol, start=start_date, end=end_date)
sp500_data = yf.download(sp500_symbol, start=start_date, end=end_date)

# Calcolo dello z-score per entrambi gli indici:  (valore - media)/dev_standard
vix_zscore = (vix_data['Close'] - vix_data['Close'].mean()) / vix_data['Close'].std()
sp500_zscore = (sp500_data['Close'] - sp500_data['Close'].mean()) / sp500_data['Close'].std()

# Creazione del grafico
plt.figure(figsize=(14, 7))
plt.plot(vix_data.index, vix_zscore, label="VIX (z-score)", color="red", alpha=0.7)
plt.plot(sp500_data.index, sp500_zscore, label="S&P500 (z-score)", color="blue", alpha=0.7)

# Personalizzazione del grafico
plt.title("Confronto tra indice VIX e S&P500 (z-score)", fontsize=16)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Z-Score", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Salvataggio del grafico come PNG con la data attuale nel nome
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"Confronto_VIX_SP500_{current_date}.png"
plt.savefig(file_name)

plt.show()

print(f"Grafico salvato come: {file_name}")
