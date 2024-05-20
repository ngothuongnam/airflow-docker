# Airflow CLI cung cấp nhiều lệnh hữu ích để quản lý và vận hành các workflows trong Airflow. Dưới đây là danh sách các lệnh phổ biến của Airflow CLI và cách sử dụng chúng

## Quản lý DAGs

1. Trigger DAG: Khởi động một DAG run

```airflow dags trigger <dag_id>```

2. Xóa DAG: Xóa một DAG và tất cả các bản ghi liên quan từ cơ sở dữ liệu

```airflow dags delete <dag_id>```

3. Danh sách DAGs: Hiển thị danh sách các DAGs

```airflow dags list```

4. Dừng DAG: Dừng một DAG (ngăn nó chạy)

```airflow dags pause <dag_id>```

5. Tiếp tục DAG: Kích hoạt lại một DAG đã bị dừng

```airflow dags unpause <dag_id>```

## Quản lý task instances
1. Danh sách task instances: Hiển thị danh sách các task instances của một DAG

```airflow tasks list <dag_id>```

2. Chạy task: Thực thi một task cụ thể bên ngoài lịch trình của DAG.

```airflow tasks run <dag_id> <task_id> <execution_date>```

3. Xóa task instance: Xóa các task instances theo tiêu chí nhất định.

```airflow tasks delete <dag_id> --execution_date <execution_date>```

### Quản lý các lần chạy của DAG (DAG runs)
1. Danh sách DAG runs: Hiển thị danh sách các DAG runs của một DAG.

```airflow dags list-runs <dag_id>```

2. Xóa DAG run: Xóa một DAG run cụ thể

```airflow dags delete-run <dag_id> <execution_date>```

## Quản lý cơ sở dữ liệu
1. Khởi tạo cơ sở dữ liệu: Tạo bảng cơ sở dữ liệu ban đầu cho Airflow.

```airflow db init```

2. Nâng cấp cơ sở dữ liệu: Nâng cấp cơ sở dữ liệu Airflow lên phiên bản mới nhất.

```airflow db upgrade```

3. Xóa cơ sở dữ liệu: Xóa tất cả các bảng và dữ liệu từ cơ sở dữ liệu.

```airflow db reset```

## Quản lý người dùng
1. Tạo người dùng: Tạo người dùng mới cho Airflow.

```airflow users create --username <username> --firstname <firstname> --lastname <lastname> --role <role> --email <email>```

2. Danh sách người dùng: Hiển thị danh sách người dùng.

```airflow users list```

## Khác
1. Khởi động web server: Khởi động Airflow web server.

```airflow webserver```

2. Khởi động scheduler: Khởi động Airflow scheduler.

```airflow scheduler```

3. Kiểm tra trạng thái DAG: Kiểm tra trạng thái của một DAG.

```airflow dags state <dag_id> <execution_date>```

4. In thông tin cấu hình: Hiển thị thông tin cấu hình hiện tại của Airflow.

```airflow config list```

5. In thông tin về phiên bản: Hiển thị thông tin phiên bản của Airflow.

```airflow version```

## Sử dụng CLI trong Docker
Nếu bạn đang chạy Airflow trong Docker, bạn cần truy cập vào container Docker để sử dụng các lệnh CLI:

1. Truy cập vào container:

```docker exec -it <container_name> /bin/bash```

Thay <container_name> bằng tên container của bạn.

2. Sử dụng các lệnh CLI như bình thường:

```airflow dags list```

Những lệnh này giúp bạn quản lý và điều khiển Airflow một cách hiệu quả, từ việc khởi động và dừng DAGs đến quản lý cơ sở dữ liệu và người dùng.