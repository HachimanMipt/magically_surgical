# основной файл "программы"

import os
from utils import helpers

# база с данными о видео
VIDEOS = "data/videos.txt"

def uplod_vdeo(video_name, size):
    # типа добовляет видео в базу данных
    f = open(VIDEOS, "a")
    f.write(video_name + " " + str(size) + "\n") # не проверяем вообще типы
    f.close()
    print("Added video:", video_name, size, "mb")

def list_vedos():
    # выводим список всех сохраненных видосов.
    with open(VIDEOS, "r") as f:
        print("VIDEOS:")
        print(f.read())

if __name__ == "__main__":
    print("Запускаем тест программы!")
    uplod_vdeo("cat.mp4", "200")
    list_vedos()
    helpers.calc_vdeo_size("cat.mp4")