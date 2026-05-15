import tkinter as tk
import threading

from app.services.camera_service import (
    start_camera,
    stop_camera
)

def create_dashboard():

    root = tk.Tk()

    root.title("Driver Monitoring Dashboard")
    root.geometry("300x220")

    title = tk.Label(
        root,
        text="Driver Monitoring System",
        font=("Arial", 16, "bold")
    )

    title.pack(pady=20)

    start_btn = tk.Button(
        root,
        text="Start Monitoring",
        width=20,
        height=2,
        command=lambda: threading.Thread(
            target=start_camera,
            daemon=True
        ).start()
    )

    start_btn.pack(pady=10)

    stop_btn = tk.Button(
        root,
        text="Stop Monitoring",
        width=20,
        height=2,
        command=stop_camera
    )

    stop_btn.pack(pady=10)

    exit_btn = tk.Button(
        root,
        text="Exit",
        width=20,
        height=2,
        command=root.destroy
    )

    exit_btn.pack(pady=10)

    root.mainloop()