import os
from ultralytics import YOLO
from PIL import Image
from PIL import ImageTk
import tkinter as tk
import imutils
import cv2

MODEL_PATH = os.path.abspath('./RDD.pt')
model = YOLO(MODEL_PATH)

if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.option_add('*tearOff', False)

    file_menu = tk.Menu()
    file_menu.add_command(label=f'Открыть')
    file_menu.add_command(label=f'Сохранить как...')

    main_menu = tk.Menu(main_window)
    main_menu.add_cascade(label=f'Файл', menu=file_menu)

    main_window.config(menu=main_menu)
    main_window.mainloop()
