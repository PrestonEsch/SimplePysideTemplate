import os
import subprocess

ui_dir = "./ui/"

for file in os.listdir(ui_dir):
    if file.endswith(".ui"):
        ui_path = os.path.join(ui_dir, file)
        py_path = os.path.join(ui_dir, f"{os.path.splitext(file)[0]}.py")

        subprocess.run([
            "pyside6-uic",
            ui_path,
            "-o",
            py_path
        ])

print("All UI files converted.")