# 模型更新脚本
# 使用方法: python update_model.py <新模型文件路径> <版本号> <发布说明>

import sys, os, json, hashlib

def update(new_model_path, new_version, release_notes):
    cdn_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. 计算新模型的 SHA256 和大小
    with open(new_model_path, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    size = os.path.getsize(new_model_path)

    # 2. 替换模型文件
    dest = os.path.join(cdn_dir, 'yolo_nano_garbage.tflite')
    import shutil
    shutil.copy(new_model_path, dest)

    # 3. 更新 update.json
    json_path = os.path.join(cdn_dir, 'update.json')
    with open(json_path) as f:
        data = json.load(f)
    data['model']['version'] = int(new_version)
    data['model']['size'] = size
    data['model']['checksum'] = f'sha256:{sha}'
    data['model']['releaseNotes'] = release_notes
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'✅ 模型已更新 → version={new_version}, size={size/1024/1024:.1f}MB')
    print(f'✅ SHA256: {sha}')
    print()
    print('接下来运行:')
    print('  git add -A')
    print(f'  git commit -m "模型更新 v{new_version}: {release_notes}"')
    print('  git push')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('用法: python update_model.py <模型.tflite> <版本号> <更新说明>')
        print('示例: python update_model.py new_model.tflite 2 "新增10种物品识别"')
        sys.exit(1)
    update(sys.argv[1], sys.argv[2], sys.argv[3])
