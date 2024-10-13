import json
import os
import sys

# Function to get the correct base path for the application
def get_base_path():
    if getattr(sys, 'frozen', False):  # Checks if the application is frozen (bundled by PyInstaller)
        return sys._MEIPASS  # Returns the temporary folder created by PyInstaller for the bundled app
    return os.path.dirname(os.path.abspath(__file__))  # Returns the directory of the current script

# Updated load and save functions
def load_paint_data():
    try:
        base_path = get_base_path()
        file_path = os.path.join(base_path, 'paint_collection.json')
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_paint_data():
    base_path = get_base_path()
    file_path = os.path.join(base_path, 'paint_collection.json')
    with open(file_path, 'w') as file:
        json.dump(paint_collection, file, indent=4)

# Dictionary to store paint data
paint_collection = load_paint_data()


# Predefined list of valid paint manufacturers
valid_manufacturers = ['PANTONE', 'BENJAMIN MOORE', 'SHERWIN WILLIAMS', 'MATTHEWS']

# Function to choose paint manufacturer
def choose_manufacturer():
    manufacturer = simpledialog.askinteger("Paint Manufacturer", 
                                           "\n".join([f"[{i+1}] {m}" for i, m in enumerate(valid_manufacturers)]))
    if manufacturer and 1 <= manufacturer <= len(valid_manufacturers):
        return valid_manufacturers[manufacturer - 1]
    else:
        messagebox.showerror("Error", "Invalid selection.")
        return None

# Function to validate job number input (numeric only)
def get_valid_job_number():
    job_number = simpledialog.askstring("Job Number", "Enter Job Number (numbers only):")
    if job_number and job_number.isdigit():
        return job_number
    else:
        messagebox.showerror("Error", "Job number must contain only numbers.")
        return None

# Function to add Paint Code and relevant information
def add_paint_code():
    paint_manufacturer = choose_manufacturer()
    if not paint_manufacturer:
        return

    paint_code = simpledialog.askstring("Paint Code", "Enter Paint Code or Color Name:").strip().upper()
    paint_version = simpledialog.askstring("Paint Version", "Enter Paint Version Number:").strip().upper()
    job_number = get_valid_job_number()
    comments = simpledialog.askstring("Comments", "Enter any additional comments (optional):").strip().upper()

    if not paint_manufacturer or not paint_code or not paint_version or not job_number:
        messagebox.showerror("Error", "All fields except comments are required.")
        return

    if job_number in paint_collection:
        paint_collection[job_number]["paint_codes"].append({
            "code": paint_code,
            "manufacturer": paint_manufacturer,
            "version": paint_version,
            "comments": comments
        })
        messagebox.showinfo("Success", f"Paint code {paint_code} has been added to job number {job_number}.")
    else:
        paint_collection[job_number] = {
            "paint_codes": [{
                "code": paint_code,
                "manufacturer": paint_manufacturer,
                "version": paint_version,
                "comments": comments
            }]
        }
        messagebox.showinfo("Success", f"New job number {job_number} has been added with paint code {paint_code}.")
    
    save_paint_data()

# Function to look up by paint code
def lookup_by_paint_code():
    paint_code = simpledialog.askstring("Paint Code Lookup", "Enter Paint Code to look up:")
    
    # Handle the case where the user cancels the input dialog
    if not paint_code:
        return
    
    paint_code = paint_code.strip().upper()
    
    found = False
    details = ""
    for job_number, job_details in paint_collection.items():
        for paint in job_details["paint_codes"]:
            if paint["code"] == paint_code:
                details += (f"Found details for Paint Code {paint_code} under Job Number {job_number}:\n"
                            f"  MANUFACTURER: {paint['manufacturer']}\n"
                            f"  VERSION: {paint['version']}\n"
                            f"  COMMENTS: {paint['comments']}\n\n")
                found = True

    if found:
        messagebox.showinfo("Paint Code Found", details)
    else:
        messagebox.showerror("Not Found", "Paint Code not found.")

# Function to look up by job number
def lookup_by_job_number():
    job_number = get_valid_job_number()
    if not job_number:
        return

    if job_number in paint_collection:
        details = "\n".join([f"Paint Code: {paint['code']}\nMANUFACTURER: {paint['manufacturer']}\nVERSION: {paint['version']}\nCOMMENTS: {paint['comments']}\n"
                             for paint in paint_collection[job_number]["paint_codes"]])
        messagebox.showinfo("Job Number Lookup", f"Details for Job Number {job_number}:\n{details}")
    else:
        messagebox.showerror("Not Found", "Job number not found.")

# Function to display all added paint information
def view_all_paint_info():
    if paint_collection:
        details = ""
        for job_number, job_details in paint_collection.items():
            if "paint_codes" in job_details:  # Ensure job number has 'paint_codes' key
                details += f"Job Number: {job_number}\n"
                for paint in job_details["paint_codes"]:
                    details += (f"  Paint Code: {paint['code']}\n"
                                f"  MANUFACTURER: {paint['manufacturer']}\n"
                                f"  VERSION: {paint['version']}\n"
                                f"  COMMENTS: {paint['comments']}\n\n")
            else:
                details += f"Job Number: {job_number} does not have any valid associated paint codes or is incorrectly formatted.\n\n"

        messagebox.showinfo("All Paint Codes and Details", details)
    else:
        messagebox.showerror("Not Found", "No paint codes have been added yet.")


# Function to delete the database
def delete_database():
    password = simpledialog.askstring("Delete Database", "Enter the password to delete the database:", show='*')
    if password == "ERASEDATABASE":
        if os.path.exists('paint_collection.json'):
            os.remove('paint_collection.json')
            messagebox.showinfo("Success", "The database has been deleted.")
        else:
            messagebox.showerror("Error", "No database file found to delete.")
        paint_collection.clear()
    else:
        messagebox.showerror("Error", "Incorrect password. The database has not been deleted.")

# Main program loop with GUI
def main():
    root = tk.Tk()
    root.title("Paint Code Tracking System")
    root.geometry("400x400")

    tk.Button(root, text="Add Paint Code", command=add_paint_code).pack(pady=5)
    tk.Button(root, text="Lookup by Paint Code", command=lookup_by_paint_code).pack(pady=5)
    tk.Button(root, text="Lookup by Job Number", command=lookup_by_job_number).pack(pady=5)
    tk.Button(root, text="View All Paint Codes", command=view_all_paint_info).pack(pady=5)
    tk.Button(root, text="Delete Database", command=delete_database).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
