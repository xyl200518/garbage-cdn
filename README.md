# 智能垃圾分类 - OTA 更新仓库

此仓库托管垃圾分类 App 的模型和知识库在线更新文件。

## 文件说明

| 文件 | 说明 |
|------|------|
| `update.json` | 版本清单（App 启动时自动检查） |
| `yolo_nano_garbage.tflite` | YOLOv8n 垃圾分类模型（5类） |
| `knowledge_base.json` | 知识库 JSON |

## 使用方式

将本仓库的 GitHub Raw URL 配置到 App 的 `UpdateManager.updateServerUrl` 即可。
