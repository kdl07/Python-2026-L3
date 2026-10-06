import os
import gzip
import pickle

DATA_FILE = "students.dat"

def load_data():
    """Loads, decompresses, and unpickles data from students.dat if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with gzip.open(DATA_FILE, "rb") as f:
                data = pickle.load(f)
                return (
                    data.get("students", []),
                    data.get("courses", []),
                    data.get("marks_list", [])
                )
        except (EOFError, pickle.UnpicklingError, gzip.BadGzipFile):
            print("Error loading or decompressing save file. Starting with empty data.")
    return [], [], []

def save_data(students, courses, marks_list):
    """Compresses and serializes students, courses, and marks into students.dat using pickle."""
    data = {
        "students": students,
        "courses": courses,
        "marks_list": marks_list
    }
    with gzip.open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)