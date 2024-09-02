import tkinter as tk
import subprocess
import os
import tempfile

class LegendaryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Legendary GUI")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        
        self.auth_button = tk.Button(self.button_frame, text="Authenticate", command=self.authenticate)
        self.auth_button.grid(row=0, column=0, padx=5)

        self.delete_login_button = tk.Button(self.button_frame, text="Delete Saved Login", command=self.delete_saved_login)
        self.delete_login_button.grid(row=0, column=1, padx=5)

        self.download_saves_button = tk.Button(self.button_frame, text="Download Saves", command=self.download_saves)
        self.download_saves_button.grid(row=0, column=2, padx=5)

        self.game_manager_button = tk.Button(self.button_frame, text="Game Manager", command=self.open_game_manager)
        self.game_manager_button.grid(row=0, column=3, padx=5)

        self.install_eos_overlay_button = tk.Button(self.button_frame, text="Install and enable EOS Overlay (Admin required)", command=self.install_eos_overlay)
        self.install_eos_overlay_button.grid(row=0, column=4, padx=5)

        self.list_saves_button = tk.Button(root, text="List Saves", command=self.list_saves)
        self.list_saves_button.pack(pady=(10, 5))

        self.egl_sync_button = tk.Button(root, text="EGL Sync", command=self.egl_sync)
        self.egl_sync_button.pack(pady=(10, 5))

        self.other_commands_label = tk.Label(root, text="Other legendary commands")
        self.other_commands_label.pack(pady=(10, 0))

        self.custom_command_entry = tk.Entry(root, width=50)
        self.custom_command_entry.pack(pady=10)

        self.execute_command_button = tk.Button(root, text="Execute Command", command=self.execute_custom_command)
        self.execute_command_button.pack(pady=10)

        self.help_button = tk.Button(root, text="?", command=self.show_help, width=2)
        self.help_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    def run_command(self, command):
        userprofile = os.environ['USERPROFILE']
        command_path = os.path.join(userprofile, 'legendary.exe')

    
        with tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode='w') as bat_file:
            bat_file.write(f'@echo off\n"{command_path}" {" ".join(command)}\npause\nexit\n')
            bat_file_path = bat_file.name

        subprocess.run(['cmd', '/c', bat_file_path])

        os.remove(bat_file_path)


    def authenticate(self):
        self.run_command(['auth'])

    def list_games(self):
        self.run_command(['list-games'])

    def delete_saved_login(self):
        self.run_command(['auth', '--delete'])

    def execute_custom_command(self):
        custom_command = self.custom_command_entry.get().split()
        if custom_command:
            self.run_command(custom_command)

    def install_game(self):
        app_name = self.install_command_entry.get()
        if app_name:
            self.run_command(['install', app_name])

    def launch_game(self):
        app_name = self.launch_command_entry.get()
        if app_name:
            self.run_command(['launch', app_name])

    def download_saves(self):
        self.run_command(['download-saves'])

    def egl_sync(self):
        self.run_command(['egl-sync'])

    def install_eos_overlay(self):
        self.run_command(['eos-overlay', 'install'])

    def list_saves(self):
        self.run_command(['list-saves'])

    def show_help(self):
        help_text = (
            "Help Information:\n\n"
            "WIP\n"
        )
        messagebox.showinfo("Help", help_text)

    def open_game_manager(self):
        game_manager_window = tk.Toplevel(self.root)
        game_manager_window.title("Game Manager")
        
        list_installed_games_button = tk.Button(game_manager_window, text="List Installed Games", command=self.list_installed_games)
        list_installed_games_button.pack(pady=(10, 0))

        list_games_button = tk.Button(game_manager_window, text="List Games", command=self.list_games)
        list_games_button.pack(pady=10)

        install_commands_label = tk.Label(game_manager_window, text="Install game with app name")
        install_commands_label.pack(pady=(10, 0))

        self.install_command_entry = tk.Entry(game_manager_window, width=50)
        self.install_command_entry.pack(pady=10)

        install_command_button = tk.Button(game_manager_window, text="Install Game", command=self.install_game)
        install_command_button.pack(pady=10)

        launch_commands_label = tk.Label(game_manager_window, text="Launch game with app name")
        launch_commands_label.pack(pady=(10, 0))

        self.launch_command_entry = tk.Entry(game_manager_window, width=50)
        self.launch_command_entry.pack(pady=10)

        launch_command_button = tk.Button(game_manager_window, text="Launch Game", command=self.launch_game)
        launch_command_button.pack(pady=10)

        note_label = tk.Label(game_manager_window, text="NOTE: APP NAME REFERS TO THE APP NAME SHOWN WHEN YOU CLICK 'LIST GAMES.' NOT THE ACTUAL GAME NAME IN MOST CASES")
        note_label.pack(pady=(10, 10), padx=10, anchor='w')

    def list_installed_games(self):
        self.run_command(['list-installed'])

root = tk.Tk()

app = LegendaryGUI(root)

root.mainloop()
