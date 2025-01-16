# 人脸检测

## 创建环境（建议）
```python
conda create -n face python==3.8
```

```python
conda activate face
```

## 安装 cmake 工具
```python
sudo apt update  # 更新软件包索引
```

```python
sudo apt install cmake  # cmake 是一个跨平台的构建系统，常用于编译和安装软件。
```


## 安装依赖包
```python
pip install -r requirements.txt
```

## 运行
```python
nohup python face_flask.py & tail -f nohup.out
```
