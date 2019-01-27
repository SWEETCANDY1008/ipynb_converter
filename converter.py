import os
import sys

# 폴더 내에 파일들을 불러와서 순서대로 실행

print("폴더 내 파일 변환을 수행합니다.\n")
print("변환을 원하는 파일은 note폴더에, 변환이 완료되면 docs 폴더에 저장이 됩니다.\n")

path_dir = './note'
file_list = os.listdir(path_dir)
file_list.sort()
path_dir2 = './docs'
category = input("카테고리를 입력해 주세요.\n")


for i in file_list:
    file_name = i.split(".")[0]

    inputs = file_name + ".ipynb"
    outputs = file_name + ".md"

    os.system("jupyter nbconvert --output-dir='./docs' --to markdown " + path_dir + "/" + inputs)
    os.system("python ./change_src_and_Plus_YAML.py " + path_dir2 + "/" + outputs + " " + file_name + " " + category)
