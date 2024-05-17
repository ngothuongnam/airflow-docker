from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import dag, task

# Định nghĩa các tham số mặc định cho DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Sử dụng decorator để định nghĩa DAG
@dag(default_args=default_args, schedule_interval='@daily', start_date=datetime(2023, 1, 1), catchup=False)
def example_decorator_dag():

    # Sử dụng decorator để định nghĩa task
    @task
    def start_task():
        print("Starting task")

    @task
    def process_task():
        print("Processing task")

    @task
    def end_task():
        print("Ending task")

    # Định nghĩa luồng thực hiện các task
    start = start_task()
    process = process_task()
    end = end_task()

    # Thiết lập thứ tự thực hiện
    start >> process >> end

# Gán hàm DAG cho biến để Airflow nhận diện
dag = example_decorator_dag()