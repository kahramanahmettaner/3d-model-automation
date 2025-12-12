# STEP to STL Converter (FreeCAD)

A simple utility to convert all `.step` or `.stp` files in a folder into `.stl` files using FreeCAD’s Python interpreter.  
It provides **progress information** in the terminal for both the number of files converted and the total size processed.

---

## Requirements

- Windows  
- FreeCAD installed (version 0.21 recommended)  
- No separate Python installation is required  

---

## Setup

1. **Install FreeCAD** from [FreeCAD Downloads](https://www.freecad.org/downloads.php).

2. **Download or clone** this project folder. Make sure it contains:  
   - `main.py`  
   - `step_utils.py`  
   - `convert_folder.bat`  

3. **Create a `.env` file** in the same folder to specify FreeCAD’s Python path. For example:
FREECAD_PYTHON="C:\Program Files\FreeCAD 0.21\bin\python.exe"

> Make sure to include quotes if the path contains spaces. Replace the path with your own FreeCAD installation path.

---

## Usage

### 1. Using the batch file with a folder path:
convert_folder.bat "C:\path\to\STEPFILES"

### 2. Using the batch file without an argument (interactive mode):
convert_folder.bat

### 3. Run the Batch File and Drag & Drop the Folder


You will be prompted to enter the folder path in the terminal.

---

## Output

- The converted STL files will be saved in a folder next to the input folder:  

<INPUT_FOLDER>-stl-output/


- Terminal shows **progress by file count** and **total STEP file size** during conversion.

---

## Notes

- Supports both **relative and absolute paths**  
- Works with folders that have **spaces in their names**  
- Only FreeCAD is required; a separate Python installation is **not needed**
