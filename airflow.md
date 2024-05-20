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
## 1. DAG (Directed Acyclic Graph)
Mô tả: DAG là cấu trúc định nghĩa thứ tự thực thi của các tasks. Nó bao gồm các tasks và xác định mối quan hệ giữa chúng.
Vai trò: DAG xác định các workflows, mô tả công việc nào cần được thực hiện và khi nào.
## 2. Tasks
Mô tả: Task là đơn vị công việc nhỏ nhất trong Airflow. Mỗi task thực hiện một công việc cụ thể như chạy một script, gọi một API, hoặc thực thi một lệnh bash.
Vai trò: Task thực hiện các công việc đơn lẻ trong một DAG.
## 3. DAG Run
Mô tả: DAG Run đại diện cho một lần thực thi của toàn bộ DAG tại một thời điểm cụ thể.
Vai trò: Giữ thông tin về trạng thái và tiến trình của việc thực thi DAG.
## 4. Task Instance
Mô tả: Task Instance là một phiên bản cụ thể của một task tại một thời điểm thực thi cụ thể.
Vai trò: Cho phép theo dõi chi tiết việc thực thi của từng task trong một DAG.
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
## 5. Scheduler
Mô tả: Scheduler là thành phần chịu trách nhiệm lên lịch và gửi các tasks đến các workers để thực thi.
Vai trò: Đảm bảo rằng các tasks được thực thi đúng theo lịch trình đã định trong DAG.
## 6. Executor
Mô tả: Executor xác định cách các tasks được thực thi. Có nhiều loại Executors khác nhau như LocalExecutor, CeleryExecutor, KubernetesExecutor, v.v.
Vai trò: Quản lý việc thực thi tasks, phân phối chúng tới các workers.
## 7. Workers
Mô tả: Workers là các thực thể thực thi các tasks đã được lên lịch bởi Scheduler.
Vai trò: Thực thi các công việc cụ thể được định nghĩa trong tasks.
## 8. Web Interface
Mô tả: Giao diện web cho phép người dùng tương tác với hệ thống Airflow, bao gồm việc xem DAGs, giám sát DAG Runs và Task Instances, và quản lý hệ thống.
Vai trò: Cung cấp giao diện người dùng để quản lý và giám sát các workflows.
## 9. Metadata Database
Mô tả: Cơ sở dữ liệu lưu trữ thông tin về DAGs, DAG Runs, Task Instances, và các thông tin cấu hình khác.
Vai trò: Lưu trữ trạng thái và tiến trình của tất cả các workflows.
## 10. CLI (Command Line Interface)
Mô tả: Công cụ dòng lệnh cho phép người dùng tương tác với Airflow để quản lý DAGs, chạy tasks, và thực hiện nhiều tác vụ quản trị khác.
Vai trò: Cung cấp một cách tương tác để quản lý Airflow từ dòng lệnh.

## Tương Tác Giữa Các Thành Phần
### Lập Lịch và Thực Thi:

Scheduler đọc DAGs và lên lịch các tasks cần thực thi.
Executor nhận các tasks từ Scheduler và phân phối chúng đến các Workers.

### Lưu Trữ và Giám Sát:

Metadata Database lưu trữ trạng thái và tiến trình của các DAGs và tasks.
Web Interface cho phép người dùng xem trạng thái, lịch sử thực thi và nhật ký của các tasks và DAGs.

### Tương Tác Người Dùng:

Người dùng có thể sử dụng CLI để quản lý Airflow và thực thi các lệnh.
Giao diện web cho phép giám sát và quản lý các workflows một cách trực quan.

- Ví dụ Minh Họa

DAG: Định nghĩa một workflow hàng ngày để tải dữ liệu từ một API, xử lý dữ liệu, và lưu vào cơ sở dữ liệu.

Tasks: Bao gồm các bước như tải dữ liệu (fetch_data), xử lý dữ liệu (process_data), và lưu trữ dữ liệu (store_data).

DAG Run: Mỗi ngày, một DAG Run mới được tạo để thực thi workflow hàng ngày này.

Task Instances: Tạo ra các phiên bản thực thi cụ thể cho mỗi task trong DAG vào mỗi DAG Run.
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

