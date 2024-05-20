from airflow.decorators import dag, task
from datetime import datetime
import pymssql
import requests

@dag(schedule_interval=None, start_date=datetime(2024, 5, 20), description='A simple DAG', catchup=False)
def etl_dag():

    @task
    def call_api():
        api_endpoint = "http://10.10.10.1:8080/data"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "doi_tuong": "so_ho_so",
            "linh_vuc": "L01",
            "ky_du_lieu": "2011",
            "don_vi_bao_cao": "Bộ Tài chính",
            "don_vi_nhan_bao_cao": "Cục Văn thư và Lưu trữ nhà nước",
            "data": "1"
        }
        requests.post(api_endpoint, headers=headers, json=payload)
    
    @task
    def transfer_data():
        try:
            # Connection information for SQL Server
            source_connection_info = {
                'host': '10.10.10.1',
                'user': 'sa',
                'password': '@ANHpro12345',
                'database': 'source'
            }

            destination_connection_info = {
                'host': '10.10.10.1',
                'user': 'sa',
                'password': '@ANHpro12345',
                'database': 'destination'
            }

            # Connect to source database
            source_conn = pymssql.connect(**source_connection_info)
            source_cursor = source_conn.cursor()

            # Fetch data from source
            source_cursor.execute("SELECT * FROM dbo.data")
            rows = source_cursor.fetchall()

            # Connect to destination database
            destination_conn = pymssql.connect(**destination_connection_info)
            destination_cursor = destination_conn.cursor()

            # Insert data into destination
            for row in rows:
                destination_cursor.execute("INSERT INTO dbo.data VALUES (%s, %s, %s, %s, %s, %s)", row)
            
            # Commit changes
            destination_conn.commit()
        finally:
            # Close connections
            source_cursor.close()
            source_conn.close()
            destination_cursor.close()
            destination_conn.close()
    
    call_api_task = call_api()
    transfer_data_task = transfer_data()

    call_api_task >> transfer_data_task

etl_dag = etl_dag()
