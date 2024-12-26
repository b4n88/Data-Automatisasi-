import pandas as pd

# Fungsi untuk memproses file CSV
def proses_file_csv(input_file, output_file, output_tunai, output_type_trx):
    # 1. Membaca file dengan header otomatis
    df = pd.read_csv(input_file, skiprows=6, sep='|')
    
    # 2. Memperbarui kolom 'Cabang' dengan 4 karakter pertama dari kolom 'TOKO'
    df['Cabang'] = df['TOKO'].astype(str).str[:4]
    
    # 3. Filter Dataset 1: TUNAI_AMOUNT > 0 dan kelipatan 50.000
    df['TUNAI_AMOUNT'] = pd.to_numeric(df['TUNAI_AMOUNT'], errors='coerce')
    df_tunai = df[(df['TUNAI_AMOUNT'] > 0) & (df['TUNAI_AMOUNT'] % 50000 == 0)]
    
    # 4. Filter Dataset 2: TYPE_TRX adalah 'TCH' atau 'GRB'
    df_type_trx = df[df['TYPE_TRX'].isin(['TCH', 'GRB'])]
    
    # 5. Menyimpan hasil ke file terpisah
    df.to_csv(output_file, index=False)
    df_tunai.to_csv(output_tunai, index=False)
    df_type_trx.to_csv(output_type_trx, index=False)
    
    print(f"File utama disimpan sebagai: {output_file}")
    print(f"Dataset TUNAI_AMOUNT disimpan sebagai: {output_tunai}")
    print(f"Dataset TYPE_TRX disimpan sebagai: {output_type_trx}")


