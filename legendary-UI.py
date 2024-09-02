import tkinter as tk
import subprocess
import os
import tempfile

class LegendaryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Legendary GUI")

        # Create a frame to hold the top buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Create and place the top buttons in the frame
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

        # Create and place the List Saves button in a new row
        self.list_saves_button = tk.Button(root, text="List Saves", command=self.list_saves)
        self.list_saves_button.pack(pady=(10, 5))

        # Create and place the EGL sync button in a new row
        self.egl_sync_button = tk.Button(root, text="EGL Sync", command=self.egl_sync)
        self.egl_sync_button.pack(pady=(10, 5))

        # Create and place the label for other commands in the main window
        self.other_commands_label = tk.Label(root, text="Other legendary commands")
        self.other_commands_label.pack(pady=(10, 0))

        # Create and place the entry box for custom commands in the main window
        self.custom_command_entry = tk.Entry(root, width=50)
        self.custom_command_entry.pack(pady=10)

        # Create and place the button to execute custom commands in the main window
        self.execute_command_button = tk.Button(root, text="Execute Command", command=self.execute_custom_command)
        self.execute_command_button.pack(pady=10)

        # Create and place the help button in the corner
        self.help_button = tk.Button(root, text="?", command=self.show_help, width=2)
        self.help_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    def run_command(self, command):
        """Run a command using a temporary batch script and delete it after execution."""
        userprofile = os.environ['USERPROFILE']
        command_path = os.path.join(userprofile, 'legendary.exe')
    
        # Create a temporary batch file with the command and a pause
        with tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode='w') as bat_file:
            bat_file.write(f'@echo off\n"{command_path}" {" ".join(command)}\npause\nexit\n')
            bat_file_path = bat_file.name
    
        # Run the batch file
        subprocess.run(['cmd', '/c', bat_file_path])
    
        # Delete the batch file after execution
        os.remove(bat_file_path)


    def authenticate(self):
        """Run the legendary auth command."""
        self.run_command(['auth'])

    def list_games(self):
        """Run the legendary list-games command."""
        self.run_command(['list-games'])

    def delete_saved_login(self):
        """Run the legendary auth --delete command."""
        self.run_command(['auth', '--delete'])

    def execute_custom_command(self):
        """Execute a custom legendary command typed by the user."""
        custom_command = self.custom_command_entry.get().split()
        if custom_command:
            self.run_command(custom_command)

    def install_game(self):
        """Execute an install command with the app name."""
        app_name = self.install_command_entry.get()
        if app_name:
            self.run_command(['install', app_name])

    def launch_game(self):
        """Execute a launch command with the app name."""
        app_name = self.launch_command_entry.get()
        if app_name:
            self.run_command(['launch', app_name])

    def download_saves(self):
        """Run the legendary download-saves command."""
        self.run_command(['download-saves'])

    def egl_sync(self):
        """Run the legendary egl-sync command."""
        self.run_command(['egl-sync'])

    def install_eos_overlay(self):
        """Run the legendary eos-overlay command."""
        self.run_command(['eos-overlay', 'install'])

    def list_saves(self):
        """Run the legendary list-saves command."""
        self.run_command(['list-saves'])

    def show_help(self):
        """Display help information."""
        help_text = (
            "Help Information:\n\n"
            "1. Authenticate: Runs the legendary auth command to log in.\n"
            "2. List Games: Displays a list of available games.\n"
            "3. Delete Saved Login: Deletes saved login credentials.\n\n"
            "4. Execute Command: Runs any custom legendary command you type.\n"
            "5. Install Game: Installs a game using the name you provide. Use names from the list shown by 'List Games'.\n"
            "6. Launch Game: Launches a game using the name you provide. Use names from the list shown by 'List Games'.\n"
            "7. Download Saves: Downloads game saves from the cloud.\n"
            "8. EGL Sync: Syncs your legendary games to the Epic Games Launcher or vice versa.\n"
            "9. Install EOS Overlay: Installs the EOS Overlay.\n"
            "10. List Saves: Lists available cloud saves.\n\n"
            "App names should match those displayed by the 'List Games' button."
        )
        messagebox.showinfo("Help", help_text)

    def open_game_manager(self):
        """Open a new window with game management options."""
        game_manager_window = tk.Toplevel(self.root)
        game_manager_window.title("Game Manager")
        
        # Create and place the button to list installed games in the new window
        list_installed_games_button = tk.Button(game_manager_window, text="List Installed Games", command=self.list_installed_games)
        list_installed_games_button.pack(pady=(10, 0))

        # Create and place the button to list games in the new window
        list_games_button = tk.Button(game_manager_window, text="List Games", command=self.list_games)
        list_games_button.pack(pady=10)

        # Create and place the label for install commands in the new window
        install_commands_label = tk.Label(game_manager_window, text="Install game with app name")
        install_commands_label.pack(pady=(10, 0))

        # Create and place the entry box for install commands in the new window
        self.install_command_entry = tk.Entry(game_manager_window, width=50)
        self.install_command_entry.pack(pady=10)

        # Create and place the button to execute install commands in the new window
        install_command_button = tk.Button(game_manager_window, text="Install Game", command=self.install_game)
        install_command_button.pack(pady=10)

        # Create and place the label for launch commands in the new window
        launch_commands_label = tk.Label(game_manager_window, text="Launch game with app name")
        launch_commands_label.pack(pady=(10, 0))

        # Create and place the entry box for launch commands in the new window
        self.launch_command_entry = tk.Entry(game_manager_window, width=50)
        self.launch_command_entry.pack(pady=10)

        # Create and place the button to execute launch commands in the new window
        launch_command_button = tk.Button(game_manager_window, text="Launch Game", command=self.launch_game)
        launch_command_button.pack(pady=10)

        # Create and place the note at the bottom of the new window
        note_label = tk.Label(game_manager_window, text="NOTE: APP NAME REFERS TO THE APP NAME SHOWN WHEN YOU CLICK 'LIST GAMES.' NOT THE ACTUAL GAME NAME IN MOST CASES")
        note_label.pack(pady=(10, 10), padx=10, anchor='w')

    def list_installed_games(self):
        """Run the legendary installed-games command."""
        self.run_command(['list-installed'])

# Create the main window
root = tk.Tk()

# Initialize the LegendaryGUI
app = LegendaryGUI(root)

# Start the GUI event loop
root.mainloop()
