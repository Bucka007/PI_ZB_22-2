import os

# Путь к файлу
file_path = "input3.txt"

# Удаление файла
try:
  os.remove(file_path)
  print(f"Файл {file_path} успешно удален.")
except FileNotFoundError:
  print(f"Файл {file_path} не найден.")