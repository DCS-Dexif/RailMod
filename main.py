import customtkinter
import customtkinter as ctk
from tkinter import PhotoImage, Text

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue") # Define the main application window

class RailMod(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("RailMod")
        self.geometry("1200x700")
        self.iconbitmap("images/railmod500x.ico")

        # Create the main frames
        # Create the main frames
        self.left_frame = ctk.CTkFrame(self)
        self.middle_frame = ctk.CTkFrame(self)
        self.right_frame = ctk.CTkFrame(self, width=384)  # Set the width of the right frame here

        # Pack the frames
        self.left_frame.pack(side='left', fill='y')
        self.middle_frame.pack(side='left', fill='both', expand=True)
        self.right_frame.pack(side='left', fill='y')  # No need to set width here

        # Add buttons to the left frame
        self.settings_button = ctk.CTkButton(self.left_frame, text="Settings")
        self.add_mod_button = ctk.CTkButton(self.left_frame, text="Add Mod")
        self.backup_button = ctk.CTkButton(self.left_frame, text="Backup")

        # Pack the buttons
        self.settings_button.pack(side='top', fill='x', pady=5)
        self.add_mod_button.pack(side='top', fill='x', pady=5)
        self.backup_button.pack(side='top', fill='x', pady=5)

        # Create a small frame above the middle frame for additional elements
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(side='top', fill='x')

        # Create a scrollable canvas for the middle frame
        self.middle_canvas = ctk.CTkCanvas(self.middle_frame)
        self.middle_scrollbar = ctk.CTkScrollbar(self.middle_frame, command=self.middle_canvas.yview)
        self.middle_canvas.configure(yscrollcommand=self.middle_scrollbar.set)

        # Pack the canvas and scrollbar
        self.middle_scrollbar.pack(side='right', fill='y')
        self.middle_canvas.pack(side='left', fill='both', expand=True)

        # Create a frame inside the canvas to hold the content
        self.middle_content_frame = ctk.CTkFrame(self.middle_canvas)
        self.middle_canvas.create_window((0, 0), window=self.middle_content_frame, anchor='nw')

        # Bind the canvas to the scrollbar
        self.middle_canvas.bind('<Configure>', lambda e: self.middle_canvas.configure(scrollregion=self.middle_canvas.bbox('all')))

        # Add mod elements to the middle frame
        for _ in range(10): # Example: Add 10 mod elements
            mod_element = self.create_mod_element()
            mod_element.pack(side='top', fill='x', pady=5)

        # Add content to the right frame
        self.right_image = PhotoImage(file="images/placeholdericonlg.png")
        self.right_label = ctk.CTkLabel(self.right_frame, image=self.right_image)
        self.right_label.pack(side='top', fill='x')

        # Use standard Tkinter Text widget for the right text box
        self.right_text = Text(self.right_frame, bg='#282828', fg='white', wrap='word')
        self.right_text.insert('1.0', "Author: Author Name\nMod Name: Mod Name\nDescription: Mod Description\nVersion: 1.0\nDependencies: dlc1, dlc2, dlc3\nRelease Date: 2024-03-26\nTags: tag1, tag2, tag3")
        self.right_text.pack(side='top', fill='x', pady=5)

        self.right_install_button = ctk.CTkButton(self.right_frame, text="Install")
        self.right_install_button.pack(side='top', fill='x', pady=5)

    def create_mod_element(self):
        mod_element_frame = ctk.CTkFrame(self.middle_content_frame)

        mod_image = PhotoImage(file="images/placeholdericon.png")
        mod_label = ctk.CTkLabel(mod_element_frame, image=mod_image)
        mod_label.pack(side='top', fill='x')

        # Use standard Tkinter Text widget for the mod text box
        mod_text = Text(mod_element_frame, bg='#282828', fg='white', wrap='word')
        mod_text.insert('1.0', "Mod Name\nMod Author")
        mod_text.pack(side='top', fill='x')

        return mod_element_frame

if __name__ == "__main__":
    app = RailMod()
    app.mainloop()
