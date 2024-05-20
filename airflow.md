# I. Setup airflow with pip
## 1. Cài đặt virtualenv nếu chưa có
```
sudo apt install python3
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
```
## 2. Tạo và kích hoạt môi trường ảo
```
python3 -m venv venv
source venv/bin/activate
```
## 3. Cài đặt setuptools và wheel
```
pip install --upgrade pip setuptools wheel
```
## 4. Đặt biến môi trường (tuỳ chọn)
```
export AIRFLOW_HOME=~/my_airflow
```
## 5. Cài đặt Airflow với PostgreSQL
```
pip install apache-airflow[postgres]==2.9.1
```
## 6. Khởi tạo cơ sở dữ liệu
```
airflow db init
```
## 7. Tạo người dùng admin
```
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```
## 8. Khởi động web server và scheduler (mỗi lệnh trong một terminal khác nhau)
```
airflow webserver --port 8080
airflow scheduler
```
## 9. Tạo DAG
```
mkdir -p $AIRFLOW_HOME/dags
touch $AIRFLOW_HOME/dags/example_dag.py
```
# II. Airflow components
## 1. DAG (Directed Acyclic Graph):

Một DAG là một tập hợp các tasks được sắp xếp theo một thứ tự xác định mà không có chu kỳ. DAG xác định mối quan hệ và thứ tự thực thi giữa các tasks

## 2. Task

Một task là một đơn vị công việc cụ thể trong một DAG. Các tasks có thể thực hiện các công việc như chạy một script, gọi một API, hoặc thực thi một lệnh bash

## 3. DAG Run 

Đại diện cho một lần thực thi của toàn bộ DAG tại một thời điểm cụ thể. Mỗi lần DAG được kích hoạt, một DAG Run mới được tạo ra

## 4. Task Instance

Task Instance là một bản ghi cụ thể của việc thực thi một task trong một DAG Run. Nó đại diện cho việc thực thi của một task cụ thể trong một DAG tại một thời điểm thực thi cụ thể

- Thuộc tính của Task Instance
```
Task ID: ID của task
DAG ID: ID của DAG chứa task
Execution Date: Thời điểm thực thi của DAG run
State: Trạng thái hiện tại của task instance, ví dụ như running, success, failed, up_for_retry, skipped, v.v
Try Number: Số lần thử thực thi task này
Start Date: Thời gian bắt đầu thực thi task
End Date: Thời gian kết thúc thực thi task
```
- Các Trạng Thái của Task Instance
```
queued: Task instance đã được xếp hàng để thực thi
running: Task instance đang được thực thi
success: Task instance đã hoàn thành thành công
failed: Task instance đã thất bại
up_for_retry: Task instance đã thất bại và đang chờ để thử lại
skipped: Task instance đã bị bỏ qua
up_for_reschedule: Task instance đang chờ để được lên lịch lại
none: Task instance chưa được thực thi hoặc không có trạng thái xác định
```
# III. Airflow CLI

## 1. Quản lý DAGs

- Trigger DAG: Khởi động một DAG run

```airflow dags trigger <dag_id>```

- Xóa DAG: Xóa một DAG và tất cả các bản ghi liên quan từ cơ sở dữ liệu

```airflow dags delete <dag_id>```

- Danh sách DAGs: Hiển thị danh sách các DAGs

```airflow dags list```

- Dừng DAG: Dừng một DAG (ngăn nó chạy)

```airflow dags pause <dag_id>```

- Tiếp tục DAG: Kích hoạt lại một DAG đã bị dừng

```airflow dags unpause <dag_id>```

## 2. Quản lý task instances
- Danh sách task instances: Hiển thị danh sách các task instances của một DAG

```airflow tasks list <dag_id>```

- Chạy task: Thực thi một task cụ thể bên ngoài lịch trình của DAG

```airflow tasks run <dag_id> <task_id> <execution_date>```

- Xóa task instance: Xóa các task instances theo tiêu chí nhất định

```airflow tasks delete <dag_id> --execution_date <execution_date>```

## 3. Quản lý các lần chạy của DAG (DAG runs)
- Danh sách DAG runs: Hiển thị danh sách các DAG runs của một DAG

```airflow dags list-runs <dag_id>```

- Xóa DAG run: Xóa một DAG run cụ thể

```airflow dags delete-run <dag_id> <execution_date>```

## 4. Quản lý cơ sở dữ liệu
- Khởi tạo cơ sở dữ liệu: Tạo bảng cơ sở dữ liệu ban đầu cho Airflow

```airflow db init```

- Nâng cấp cơ sở dữ liệu: Nâng cấp cơ sở dữ liệu Airflow lên phiên bản mới nhất

```airflow db upgrade```

- Xóa cơ sở dữ liệu: Xóa tất cả các bảng và dữ liệu từ cơ sở dữ liệu

```airflow db reset```

## 5. Quản lý người dùng
- Tạo người dùng: Tạo người dùng mới cho Airflow

```airflow users create --username <username> --firstname <firstname> --lastname <lastname> --role <role> --email <email>```

- Danh sách người dùng: Hiển thị danh sách người dùng

```airflow users list```

## 6. Khác
- Khởi động web server: Khởi động Airflow web server

```airflow webserver```

- Khởi động scheduler: Khởi động Airflow scheduler

```airflow scheduler```

- Kiểm tra trạng thái DAG: Kiểm tra trạng thái của một DAG

```airflow dags state <dag_id> <execution_date>```

- In thông tin cấu hình: Hiển thị thông tin cấu hình hiện tại của Airflow

```airflow config list```

- In thông tin về phiên bản: Hiển thị thông tin phiên bản của Airflow

```airflow version```

## 7. Sử dụng CLI trong Docker
Nếu bạn đang chạy Airflow trong Docker, bạn cần truy cập vào container Docker để sử dụng các lệnh CLI:

- Truy cập vào container:

```docker exec -it <container_name> /bin/bash```

Thay <container_name> bằng tên container của bạn

- Sử dụng các lệnh CLI như bình thường:

```airflow dags list```

Những lệnh này giúp bạn quản lý và điều khiển Airflow một cách hiệu quả, từ việc khởi động và dừng DAGs đến quản lý cơ sở dữ liệu và người dùng

