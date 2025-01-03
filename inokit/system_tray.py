"""
Copyright (c) 2024 Omar Moutabir
InoKit System Tray Application
Author: Omar Moutabir
Contact: omar.moutabir@gmail.com
"""

import os
import sys
import webbrowser
import subprocess
import psutil
from PIL import Image
import pystray
from pystray import MenuItem as item

class DjangoTrayApp:
    def __init__(self):
        self.server_process = None
        self.icon = None
        self.url = "http://127.0.0.1:8000"
        
        # Get the directory where the script is located
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create the icon
        icon_path = os.path.join(self.base_dir, "static", "images", "logos", "logo.jpg")
        image = Image.open(icon_path)
        self.icon = pystray.Icon(
            "InoKit",
            image,
            "InoKit Server (Stopped)",
            menu=self.create_menu()
        )

    def create_menu(self):
        return (
            item('Toggle Server', self.toggle_server),
            item('Open Website', self.open_website),
            item('Quit', self.quit_application)
        )

    def is_server_running(self):
        if self.server_process:
            return self.server_process.poll() is None
        return False

    def toggle_server(self):
        if self.is_server_running():
            self.stop_server()
        else:
            self.start_server()

    def start_server(self):
        if not self.is_server_running():
            try:
                # Change to the project directory
                os.chdir(self.base_dir)
                
                # Start the Django server
                self.server_process = subprocess.Popen(
                    [sys.executable, "manage.py", "runserver"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                
                self.icon.title = "InoKit Server (Running)"
                self.notify("Server Started", "Django server is running at " + self.url)
                self.open_website()
            except Exception as e:
                self.notify("Error", f"Failed to start server: {str(e)}")

    def stop_server(self):
        if self.server_process:
            try:
                # Get the process and all its children
                parent = psutil.Process(self.server_process.pid)
                children = parent.children(recursive=True)
                
                # Terminate children first
                for child in children:
                    child.terminate()
                
                # Terminate parent
                parent.terminate()
                
                self.server_process = None
                self.icon.title = "InoKit Server (Stopped)"
                self.notify("Server Stopped", "Django server has been stopped")
            except Exception as e:
                self.notify("Error", f"Failed to stop server: {str(e)}")

    def open_website(self):
        if self.is_server_running():
            webbrowser.open(self.url)
        else:
            self.notify("Server Not Running", "Please start the server first")

    def notify(self, title, message):
        self.icon.notify(message, title)

    def quit_application(self):
        self.stop_server()
        self.icon.stop()

    def run(self):
        self.icon.run()

if __name__ == "__main__":
    app = DjangoTrayApp()
    app.run() 