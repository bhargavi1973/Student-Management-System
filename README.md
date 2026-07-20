# 🎓 Student Management System

A Python-based **Student Management System** that allows users to efficiently manage student records. This project demonstrates the use of **Object-Oriented Programming (OOP)**, **CRUD operations**, **JSON file handling**, **exception handling**, and a **modular code structure**.

---

## 📌 Features

- ➕ Add a new student
- 📋 View all students
- 🔍 Search student by ID
- ✏️ Update student details
- ❌ Delete student records
- 💾 Store data permanently using JSON
- ⚠️ Exception handling for invalid inputs
- 🧩 Modular and easy-to-maintain code structure

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
├── main.py          # Main program
├── student.py       # Student class
├── manager.py       # Student management operations
├── storage.py       # JSON file handling
├── students.json    # Student database
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Student-Management-System
```

### 3. Run the Application

```bash
python main.py
```

---

## 📖 Menu

```
========== Student Management System ==========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

---

## 💾 Data Storage

Student records are stored in the `students.json` file.

Example:

```json
[
    {
        "student_id": 101,
        "name": "Bhargavi",
        "age": 21,
        "course": "Python",
        "email": "bhargavi@gmail.com"
    }
]
```

---

## 🧠 OOP Concepts Used

- Classes and Objects
- Constructors
- Encapsulation
- Methods
- Modular Programming

---

## ⚠️ Exception Handling

The application handles:

- Invalid menu choices
- Invalid numeric inputs
- Duplicate Student IDs
- Student not found
- Missing or empty JSON files

---

## 📸 Sample Output

```
========== Student Management System ==========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice: 1

Enter Student ID: 101
Enter Name: Bhargavi
Enter Age: 21
Enter Course: Python
Enter Email: bhargavi@gmail.com

✅ Student added successfully.
```

---

## 🎯 Future Enhancements

- Search by student name
- Email validation
- Student sorting
- GUI using Tkinter
- SQLite/MySQL database integration
- Export student data to CSV
- Login authentication

---

## 👩‍💻 Author

**Bhargavi Kanojia**

Python Development Internship Project

---

## 📄 License

This project is developed for educational and internship purposes.