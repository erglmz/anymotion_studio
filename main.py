import tkinter as tk
from src.splash import SplashScreen
from src.launcher import Launcher
from src.drawing_app import PaintApp

class AppManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw() # Hide root initially
        self.root.title("Anymotion Studio")
        
        # Start Splash
        SplashScreen(self.root, self.on_splash_complete)
        
    def on_splash_complete(self):
        # Start Launcher
        Launcher(self.root, self.on_launcher_complete)
        
    def on_launcher_complete(self, w, h, fps):
        # Start Main App
        self.root.deiconify()
        # Pass callback to restart launcher
        try:
            self.app = PaintApp(self.root, w, h, fps, on_return_to_launcher=self.show_launcher)
        except Exception as e:
            tk.messagebox.showerror("Critical Error", f"Launcher -> App Transition Failed:\n{e}")
            self.root.quit()

    def show_launcher(self):
        # Hide main root again
        self.root.withdraw()
        # Re-open Launcher (Pass callback again)
        Launcher(self.root, self.on_launcher_complete)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    manager = AppManager()
    manager.run()
