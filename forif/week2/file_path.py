#file_path.py

file_path = input().split("\\")

count = 0
for i in file_path[:-1]:
    count += 1
    i = i.strip(':')
    print(f"<{count}> {i}")
print(f"최종 파일 : {file_path[-1]}")


    
