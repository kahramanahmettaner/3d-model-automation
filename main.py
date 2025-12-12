import sys
import os
import FreeCAD
import Part
import MeshPart

def step_to_stl(step_path, stl_path, linear_deflection=0.1, angular_deflection=0.523599):
    """Convert a single STEP file to STL."""
    if not os.path.exists(step_path):
        raise FileNotFoundError(f"STEP file not found: {step_path}")

    shape = Part.read(step_path)
    if shape is None:
        raise ValueError(f"Failed to create shape from STEP: {step_path}")

    mesh = MeshPart.meshFromShape(
        Shape=shape,
        LinearDeflection=linear_deflection,
        AngularDeflection=angular_deflection,
        Relative=False
    )
    mesh.write(stl_path)
    return os.path.getsize(step_path)  # return original STEP size for progress


def convert_folder_steps(folder_path):
    """Convert all STEP files inside a folder to STL.
    Creates an output folder named <folder>-stl-output in the same directory.
    Shows two progress bars: files and total size."""

    folder_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    folder_name = os.path.basename(folder_path)
    parent_dir = os.path.dirname(folder_path)
    output_dir = os.path.join(parent_dir, f"{folder_name}-stl-output")
    os.makedirs(output_dir, exist_ok=True)

    # Collect all STEP files and total size
    step_files = []
    total_bytes = 0
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.lower().endswith(('.step', '.stp')):
                path = os.path.join(root, f)
                step_files.append(path)
                total_bytes += os.path.getsize(path)

    if not step_files:
        print("No STEP files found in folder.")
        return

    converted_bytes = 0
    total_files = len(step_files)
    for idx, step_file in enumerate(step_files, 1):
        stl_name = os.path.splitext(os.path.basename(step_file))[0] + ".stl"
        stl_path = os.path.join(output_dir, stl_name)
        size = step_to_stl(step_file, stl_path)
        converted_bytes += size

        # File count progress
        file_progress = (idx / total_files) * 100

        # Size progress
        size_progress = (converted_bytes / total_bytes) * 100

        print(f"[{idx}/{total_files}] Files: {file_progress:.1f}% | Size: {size_progress:.1f}% - Converted {step_file}")

    print(f"\nAll STL files created in: {output_dir}")
    return output_dir


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/folder")
        sys.exit(1)

    folder_path = sys.argv[1]
    convert_folder_steps(folder_path)
