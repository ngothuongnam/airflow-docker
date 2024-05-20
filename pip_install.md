# Cài đặt virtualenv nếu chưa có
```
sudo apt install python3
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
```
# Tạo và kích hoạt môi trường ảo
```
python3 -m venv venv
source venv/bin/activate
```
# Cài đặt setuptools và wheel
```
pip install --upgrade pip setuptools wheel
```
# Đặt biến môi trường (tuỳ chọn)
```
export AIRFLOW_HOME=~/my_airflow
```
# Cài đặt Airflow với PostgreSQL
```
pip install apache-airflow[postgres]==2.9.1
```
# Khởi tạo cơ sở dữ liệu
```
airflow db init
```
# Tạo người dùng admin
```
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```
# Khởi động web server và scheduler (mỗi lệnh trong một terminal khác nhau)
```
airflow webserver --port 8080
airflow scheduler
```
# Tạo DAG
```
mkdir -p $AIRFLOW_HOME/dags
touch $AIRFLOW_HOME/dags/example_dag.py
```