import pandas as pd
import dask.dataframe as dd
import time

start = time.time()
chunksize = 100_000
total_chunk = 0

for chunk in pd.read_csv('UrbanSound8K.csv', chunksize=chunksize):
    total_chunk += chunk['value'].sum()

chunking_time = time.time() - start
print(" Chunking Result:", total_chunk)
print(" Chunking Time:", f"{chunking_time:.2f} seconds\n")


start = time.time()
dask_df = dd.read_csv('UrbanSound8K.csv')
total_dask = dask_df['value'].sum().compute()

dask_time = time.time() - start
print(" Dask Result:", total_dask)
print(" Dask Time:", f"{dask_time:.2f} seconds\n")

start = time.time()
compressed_df = pd.read_csv('C:/Users/LAPTA/Desktop/big data/TP2_chunk/UrbanSound8K.csv.gz', compression='gzip')
total_compressed = compressed_df['value'].sum()

compression_time = time.time() - start
print(" Compressed File Result:", total_compressed)
print(" Compression Time:", f"{compression_time:.2f} seconds\n")

print(" Performance Comparison:")
print(f"Chunking Time     : {chunking_time:.2f} sec")
print(f"Dask Time         : {dask_time:.2f} sec")
print(f"Compression Time  : {compression_time:.2f} sec")
