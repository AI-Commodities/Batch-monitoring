Sample 1: Database Connection Timeout
text
150045: sd-7122-9f3b: BATCH INST PE2 JOBFAILURE #JOB NAME: 150045_CRM_User_Sync_sd-7122-9f3b

Traceback (most recent call last):
  File "D:\Enterprise\Apps\crm-sync\Main.py", line 27, in <module>
    syncUserProfiles()
  File "D:\Enterprise\Apps\crm-sync\Main.py", line 18, in syncUserProfiles
    conn = connectToDatabase(credentials)
  File "D:\Enterprise\Apps\crm-sync\DBConnector.py", line 56, in connectToDatabase
    return mysql.connector.connect(**config)
  File "C:\Python39\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python39\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python39\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python39\lib\site-packages\mysql\connector\connection.py", line 208, in _open_connection
    self._socket.open_connection()
mysql.connector.errors.InterfaceError: 2003: Can't connect to MySQL server on 'dbprod.internal.company.com:3306' (10060: A connection attempt failed because the connected party did not properly respond after 30000ms)

ERROR: Database timeout - retry exhausted (3 attempts)
JOB STATUS: FAILED - RESOLVE NETWORK ROUTING TO DB CLUSTER
Sample 2: Disk Full / Storage Exhaustion
text
150102: sd-8301-4c22: BATCH INST PE2 JOBFAILURE #JOB NAME: 150102_ETL_Log_Processor_sd-8301-4c22

Traceback (most recent call last):
  File "/opt/data-pipeline/etl_runner.py", line 43, in <module>
    processDailyLogs()
  File "/opt/data-pipeline/etl_runner.py", line 38, in processDailyLogs
    writeToParquet(df, output_path)
  File "/opt/data-pipeline/writers.py", line 112, in writeToParquet
    pq.write_table(table, output_file)
  File "/usr/local/lib/python3.9/site-packages/pyarrow/parquet.py", line 242, in write_table
    writer.write_table(table)
OSError: [Errno 28] No space left on device while writing chunk to '/data/warehouse/logs/2026-06-08/part-00001.parquet'

Additional Context:
  - Available disk: 0 bytes
  - Required space: 4.2GB
  - Partition: /data (97% → 100% during job run)
  - Temporary files not cleaned from previous failed runs: 184 files (23GB)

JOB STATUS: FAILED - CLEAR STORAGE OR EXTEND VOLUME
Sample 3: Authentication / Token Expired
text
150178: sd-9456-7a11: BATCH INST PE2 JOBFAILURE #JOB NAME: 150178_API_Data_Fetcher_sd-9456-7a11

Traceback (most recent call last):
  File "/app/fetchers/salesforce_sync.py", line 31, in <module>
    fetchNewRecords(since_last_run)
  File "/app/fetchers/salesforce_sync.py", line 22, in fetchNewRecords
    response = session.get(api_url, headers=auth_headers)
  File "/app/common/auth.py", line 89, in refresh_token_if_expired
    raise AuthExpiredException()
__main__.AuthExpiredException: OAuth2 token expired at 2026-06-08 14:23:17 UTC (current time: 2026-06-08 15:01:44 UTC)

Token Details:
  - Token issued: 2026-06-08 12:00:00 UTC
  - Expiry configured: 7200 seconds (2 hours)
  - Refresh token: INVALID (revoked)
  - Service account: svc_data_pipeline@company.com (locked after 10 failed attempts)

JOB STATUS: FAILED - ROTATE CREDENTIALS AND UNLOCK SERVICE ACCOUNT
Sample 4: Missing Dependencies / Import Error
text
150199: sd-10234-8d77: BATCH INST PE2 JOBFAILURE #JOB NAME: 150199_ML_Feature_Engine_sd-10234-8d77

Traceback (most recent call last):
  File "E:\MLPlatform\feature_pipeline\run.py", line 8, in <module>
    from transformers import AutoTokenizer, AutoModel
ModuleNotFoundError: No module named 'transformers'

During handling of above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\MLPlatform\feature_pipeline\run.py", line 12, in <module>
    from tokenizers import ByteLevelBPETokenizer
ModuleNotFoundError: No module named 'tokenizers'

Environment Details:
  - Python version: 3.8.10
  - Virtual environment: /opt/venvs/ml_pipeline (activated)
  - Requirements file: requirements.txt (last updated 2026-05-15)
  - Missing packages: transformers>=4.30.0, tokenizers>=0.13.3, torch>=2.0.0
  - pip freeze shows only 12 packages (expected 48)

JOB STATUS: FAILED - RUN 'pip install -r requirements.txt' IN TARGET ENVIRONMENT
Sample 5: Memory Exhaustion (OOM Killer)
text
150245: sd-11987-f2e4: BATCH INST PE2 JOBFAILURE #JOB NAME: 150245_Report_Aggregator_sd-11987-f2e4

Traceback (most recent call last):
  File "/app/reporting/aggregator.py", line 67, in <module>
    consolidated = pd.merge(df_sales, df_inventory, on=['product_id', 'region'])
  File "/usr/local/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 120, in merge
    op = _MergeOperation(
  File "/usr/local/lib/python3.9/site-packages/pandas/core/reshape/merge.py", line 711, in __init__
    self._maybe_coerce_numbers()
MemoryError: Unable to allocate 8.23 GiB for an array with shape (110876542,) and data type float64

System Metrics at Failure:
  - RAM total: 16GB
  - RAM used before operation: 11.2GB
  - RAM requested: 8.23GB (exceeds available 4.8GB)
  - OOM killer invoked: YES (PID 19283 terminated)
  - Input data size: sales(8.4M rows), inventory(12.1M rows)
  - Expected output: 95M rows (cartesian join detected - possible missing join condition)

JOB STATUS: FAILED - REVIEW JOIN LOGIC AND ADD PARTITIONING
📊 Quick Reference Table for Model Training
Sample	Error Category	Root Cause	Key Pattern to Learn
#1	Network	DB timeout	Can't connect, 10060, properly respond
#2	Storage	Disk full	No space left on device, OSError 28
#3	Auth	Token expired	AuthExpiredException, OAuth2 token expired
#4	Environment	Missing module	ModuleNotFoundError, No module named
#5	Memory	OOM	MemoryError, Unable to allocate, cartesian join