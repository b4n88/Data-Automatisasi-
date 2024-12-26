import pandas as pd

# 1. Baca File CSV dengan Header Otomatis
def proses_file_csv(input_file, output_file):
    # Membaca file dan mengatur header secara otomatis
    df = pd.read_csv(input_file, skiprows=6, sep='|')
    
    # 2. Memperbarui kolom 'Cabang' dengan 4 karakter pertama dari kolom 'TOKO'
    df['Cabang'] = df['TOKO'].astype(str).str[:4]
    
    # 3. Menyimpan file yang sudah diperbarui
    df.to_csv(output_file, index=False)
    print(f"File berhasil diperbarui dan disimpan sebagai {output_file}")

# Contoh penggunaan
input_file = 'data_input.csv'  # Ganti dengan path file input Anda
output_file = 'data_output.csv'  # Ganti dengan path file output yang diinginkan
proses_file_csv(input_file, output_file)
