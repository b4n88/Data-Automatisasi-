import pandas as pd
import os  # Untuk manipulasi path dan folder

# Fungsi untuk memproses file CSV
def proses_file_csv(input_file, output_folder, output_file, output_tunai, output_type_trx):
    # Pastikan folder output ada, jika tidak, buat foldernya
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Gabungkan folder dengan nama file output
    output_file = os.path.join(output_folder, output_file)
    output_tunai = os.path.join(output_folder, output_tunai)
    output_type_trx = os.path.join(output_folder, output_type_trx)
    
    # 1. Membaca file dengan header otomatis
    df = pd.read_csv(input_file, skiprows=6, sep='|')
    
    # 2. Memperbarui kolom 'Cabang' dengan 4 karakter pertama dari kolom 'TOKO'
    df['Cabang'] = df['TOKO'].astype(str).str[:4]
    
    # 3. Filter Dataset 1: TUNAI_AMOUNT > 0 dan kelipatan 50.000
    df['TUNAI_AMOUNT'] = pd.to_numeric(df['TUNAI_AMOUNT'], errors='coerce')
    df_tunai = df[(df['TUNAI_AMOUNT'] > 0) & (df['TUNAI_AMOUNT'] % 50000 == 0)]
    
    # 4. Filter Dataset 2: TYPE_TRX adalah 'TCH' atau 'GRB'
    df_type_trx = df[df['TYPE_TRX'].isin(['TCH', 'GRB'])]
    
    # 5. Menyimpan hasil ke file terpisah di folder yang ditentukan
    df.to_csv(output_file, index=False)
    df_tunai.to_csv(output_tunai, index=False)
    df_type_trx.to_csv(output_type_trx, index=False)
    
    print(f"✅ File utama disimpan sebagai: {output_file}")
    print(f"✅ Dataset TUNAI_AMOUNT disimpan sebagai: {output_tunai}")
    print(f"✅ Dataset TYPE_TRX disimpan sebagai: {output_type_trx}")


# Program Utama
if __name__ == "__main__":
    # Path File Input dan Folder Output
    input_file = 'D:/R/DATA FOR KPI/IGFS.csv'  # Path file input
    output_folder = 'D:/R/DATA FOR KPI/Hasil/'  # Folder tujuan untuk output
    output_file = 'data_output.csv'  # File output utama
    output_tunai = 'dataset_tunai.csv'  # File dataset TUNAI_AMOUNT
    output_type_trx = 'dataset_type_trx.csv'  # File dataset TYPE_TRX
    
    # Menjalankan Fungsi
    proses_file_csv(input_file, output_folder, output_file, output_tunai, output_type_trx)
