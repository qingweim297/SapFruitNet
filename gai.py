import os

# 指定要处理的文件夹路径
folder_path = 'images'

# 获取文件夹中的所有文件名
file_list = os.listdir(folder_path)

# 遍历文件夹中的每个文件
for filename in file_list:
    # 检查文件是否是图片文件（这里假设只处理以 .jpg 结尾的文件）
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
        # 构建新的文件名，将后缀名改为小写
        new_filename = os.path.splitext(filename)[0] + '.jpg'

        # 构建完整的文件路径
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(old_filepath, new_filepath)
        print(f'Renamed: {filename} -> {new_filename}')