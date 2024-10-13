# **Program Tracking Program**

## **Overview**

The Program Tracking Program is a Python-based tool designed to help users efficiently manage and track program-related data. This tool allows users to store, retrieve, and manage information such as program names, tracking codes, start and end dates, program status, and additional comments. It is particularly useful for professionals who need to keep track of multiple programs or projects across various stages.

## **Features**

- **Add Program Details**: Store detailed information about programs, including name, tracking code, start and end dates, status, and optional comments.
- **Lookup by Tracking Code**: Search for program details using a specific tracking code to view all associated information.
- **Lookup by Program Name**: Retrieve program details using the program name for a quick overview.
- **View All Programs**: Display a complete list of all saved programs, including relevant details.
- **Delete Program Data**: Option to delete all stored program data (requires a password for security).

## **Installation**

### **To use the Program Tracking Program as a standalone executable:**

1. **Download the Executable**:
   - Locate the `Program Tracking Program.exe` file, typically found in the `dist` folder if you have built the program yourself.

2. **Run the Application**:
   - Double-click on the `.exe` file to launch the Program Tracking Program.

### **Requirements**

- **Python 3.8+**: If running the Python script directly.
- **Tkinter**: Library for the graphical user interface.
- **JSON**: For data storage.

### **Building the Executable**

If you'd like to create your own standalone version of the Program Tracking Program:

1. **Install PyInstaller**:

    ```bash
    pip install pyinstaller
    ```

2. **Navigate to the Project Directory and run the following command**:

    ```bash
    pyinstaller --onefile --windowed "Program Tracking Program.py"
    ```

    The executable will be created in the `dist` folder within your project directory.

## **Usage**

- **Add Program Details**: Enter the program name, tracking code, start date, end date, program status, and any optional comments.
- **Lookup by Tracking Code**: Search for details about a specific program using its tracking code.
- **Lookup by Program Name**: Retrieve program details using the program name.
- **View All Programs**: Display a comprehensive list of all saved programs with their corresponding details.
- **Delete Program Data**: Clear all stored program data by entering the correct password (default password: `ERASEDATA`).

## **Technologies Used**

- **Python**: Programming language used to build the application.
- **Tkinter**: Library used for the graphical user interface.
- **JSON**: File format used for data storage.

## **Contributing**

Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## **License**

This project is licensed under the MIT License. See the LICENSE file for more details.

## **Contact**

For any inquiries, suggestions, or issues, please contact **Christopher Lajoie** at **lajoiechristopher82@gmail.com**.
