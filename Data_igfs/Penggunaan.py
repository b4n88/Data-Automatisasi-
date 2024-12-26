input_file = 'data_input.csv'        # Ganti dengan path file input Anda
output_file = 'data_output.csv'      # File dengan kolom 'Cabang' yang diperbarui
output_tunai = 'dataset_tunai.csv'   # File untuk dataset TUNAI_AMOUNT
output_type_trx = 'dataset_type_trx.csv'  # File untuk dataset TYPE_TRX

proses_file_csv(input_file, output_file, output_tunai, output_type_trx)
