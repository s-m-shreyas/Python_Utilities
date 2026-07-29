import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# 1. Creating a Notepad class, Inherits directly from tk.Tk.

class SimpleNotepad(tk.Tk):

    # 2. Initialize the parent class (tk.Tk) with all the UI variables.
    def __init__(self)->None:
        super().__init__()
        self.title('Shreyas\'s Notepad')

        # 3. Creating a text widget for entering the content
        self.text_area: tk.Text = tk.Text(self, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # 4. Creating a frame to hold buttons.
        self.button_frame: tk.Frame = tk.Frame(self)
        self.button_frame.pack()

        # 5. Creating the save button.
        self.save_button: tk.Button = tk.Button(self.button_frame,
                                                text='Save',
                                                command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # 6. Creating the load button.
        self.load_button: tk.Button = tk.Button(self.button_frame,
                                                text='Load',
                                                command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)


        # if you want a separate update button

        # self.update_button: tk.Button = tk.Button(self.button_frame,
        #                                         text='Update',
        #                                         command=self.update_file)
        # self.update_button.pack(side=tk.BOTTOM)

        # Autosave setup
        self.current_file_path: str | None = None
        self.autosave_dir = Path.home() / ".simple_notepad"
        self.autosave_path = self.autosave_dir / "autosave.txt"
        self.autosave_dir.mkdir(parents=True, exist_ok=True)

        # Load autosave on startup (recover unsaved work)
        if self.autosave_path.exists():
            try:
                content = self.autosave_path.read_text(encoding='utf-8')
                if content.strip():
                    self.text_area.insert(1.0, content)
            except Exception:
                pass

        # Auto-save loop
        self.auto_save_interval_ms = 100  # 0.1 seconds
        self.auto_save_job: str | None = None
        self.schedule_auto_save()

        # self.current_file_path: str|None = None


    # 7. Creating a function to save the content
    def save_file(self)->None:

        if self.current_file_path is None:
            file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                            filetypes=[('Text files', '*.txt')])
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

            self.current_file_path = file_path
            print(f'File saved to: {file_path}')

        with open(self.current_file_path, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))

        print(f'File saved to: {self.current_file_path}')


    # If using update button

    # def update_file(self)->None:

    #     if self.current_file_path is None:
    #         return
        
    #     with open(self.current_file_path, 'w') as file:
    #         file.write(self.text_area.get(1.0, tk.END))
    #     print(f'File updated to: {self.current_file_path}')


    # 8. Creating a function to laod the content 
    def load_file(self)->None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                    filetypes=[('Text files', '*.txt')])
        with open(file_path, 'r') as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)

        self.current_file_path = file_path
        print(f'File loaded from: {file_path}')

    # ---------- Auto-save ----------

    def schedule_auto_save(self) -> None:
        if self.auto_save_job is not None:
            self.after_cancel(self.auto_save_job)
        self.auto_save_job = self.after(self.auto_save_interval_ms, self.auto_save_tick)

    def auto_save_tick(self) -> None:
        content = self.text_area.get(1.0, tk.END)

        # Always write to autosave file (covers new/unsaved docs)
        try:
            self.autosave_path.write_text(content, encoding='utf-8')
        except Exception:
            pass

        # If we have a real file, also save there
        if self.current_file_path is not None:
            try:
                with open(self.current_file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception:
                pass

        self.schedule_auto_save()


# 9. Main entry point of the script.

def main()->None:
    app: SimpleNotepad = SimpleNotepad()
    app.mainloop()

if __name__ == '__main__':
    main()


