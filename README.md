# AIU2 · YOLO11n 本地实验

项目实际位于 D:\aiu2；桌面“aiu2”是打开此目录的快捷方式。代码、虚拟环境、缓存、模型、数据集和训练结果均放在 D 盘。Git 已在项目根目录初始化，分支为 main；尚未配置 GitHub 远程仓库。

YOLO（You Only Look Once）用于识别图片中的物体并给出位置框与类别。本项目使用 YOLO11n：它是 YOLO11 的小型目标检测模型。当前使用 Ultralytics 8.4.173、PyTorch 2.14.1+cu130，在 NVIDIA GeForce RTX 5070 Laptop GPU 上运行。

## 已跑通的流程

- 从官方来源取得预训练 YOLO11n 权重和 COCO8 小样本数据集。
- 以 640 像素输入、批量 2、GPU 模式进行 3 轮微调；权重位于 runs\coco8_train\weights\best.pt。
- 使用训练权重对 COCO8 验证图片检测，识别出 person 与 umbrella；带框结果位于 runs\predict\000000000036.jpg。
- 此为环境与流程演示，不等同于完成飞书任务二可能要求的特定数据集、训练轮数或精度目标。

## 安装（当前机器的实际命令）

在 PowerShell 中执行：

    cd D:\aiu2
    $env:UV_CACHE_DIR = 'D:\aiu2\.uv-cache'
    uv venv --python 'C:\Users\shao\Desktop\test\.uv-python\cpython-3.12-windows-x86_64-none\python.exe' .venv
    uv pip install --python .venv\Scripts\python.exe 'torch==2.14.1+cu130' 'torchvision==0.29.1+cu130' --index-url https://download.pytorch.org/whl/cu130
    uv pip install --python .venv\Scripts\python.exe 'ultralytics==8.4.173'

当前已安装完毕，日常使用无需重复安装。

## 启动

在 PowerShell 中执行：

    cd D:\aiu2
    .\.venv\Scripts\python.exe -m yolo_demo train
    .\.venv\Scripts\python.exe -m yolo_demo predict

也可以检测自己的图片：

    .\.venv\Scripts\python.exe -m yolo_demo predict --source "D:\照片\示例.jpg"

训练结果保存在 runs\coco8_train；带框图片保存在 runs\predict。models、datasets、runs、.venv、.uv-cache 等目录均由 .gitignore 排除，不会提交到 Git。
