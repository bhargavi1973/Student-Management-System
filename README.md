# 🎓 Student Management System

A Python-based **Student Management System** developed as part of the **Python Development Internship**. The application allows users to manage student records using **Object-Oriented Programming (OOP)** and **JSON file handling** for persistent storage.

---

## 📌 Features

- ➕ Add a new student
- 📋 View all student records
- 🔍 Search a student by Student ID
- ❌ Delete a student record
- 💾 Store student data in a JSON file
- ⚠️ Exception handling for invalid input
- 🧩 Modular code structure using multiple Python files

---

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- JSON File Handling
- Standard Python Libraries

---

## 📂 Project Structure

```
Student-Management-System/
│
├── main.py              # Main application
├── student.py           # Student class
├── manager.py           # Student management operations
├── storage.py           # JSON file handling
├── student.json         # Stores student records
├── README.md
└── requirements.txt
```

---

## 📚 Student Information Stored

Each student record contains:

- Student ID
- Student Name
- Student Age
- Student Email
- Course Name
- Course ID

Example JSON record:

```json
{
    "id": 101,
    "name": "Riya",
    "age": 23,
    "email": "riya841@gmail.com",
    "course_name": "B.Com.",
    "course_id": 13
}
```

---

## 🚀 How to Run

### Clone the Repository

```bash
git clone https://github.com/your-github-username/Student-Management-System.git
```

### Open the Project Folder

```bash
cd Student-Management-System
```

### Run the Program

```bash
python main.py
```

---

## 📖 Menu

```
--- Student Management System ---

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
```

---

## 💻 Sample Output

```
--- Student Management System ---

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit

Enter your choice: 1

Enter student ID: 101
Enter student name: Riya
Enter student age: 23
Enter student email: riya841@gmail.com
Enter course name: B.Com.
Enter course ID: 13

Student added successfully.
```

---

## 🧠 OOP Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Static Methods
- Object Serialization (`to_dict()`)
- Object Deserialization (`from_dict()`)

---

## 📁 Data Storage

Student records are stored in a **JSON file** (`student.json`).

The application automatically:

- Loads records when the program starts.
- Saves records whenever a student is added or deleted.

---

## ⚠️ Exception Handling

The application handles:

- Duplicate Student IDs
- Invalid menu choices
- Invalid numeric input
- Missing JSON file
- Empty JSON file

---

## 🔮 Future Improvements

- Update student information
- Search by student name
- Email validation
- Course-wise student filtering
- Student record sorting
- SQLite/MySQL database integration
- Graphical User Interface (Tkinter)
- User Login System

---

## 👩‍💻 Author

**Bhargavi Kanojia**

Python Development Internship Project

---

## 📄 License

This project is developed for learning and internship purposes.
