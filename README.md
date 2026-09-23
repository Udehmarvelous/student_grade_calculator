# 🎓 Student Grade Calculator

A beginner-friendly **Python student grading system** that accepts scores for different subjects, calculates the appropriate **WAEC-style grade**, and calculates the student's overall average and performance comment.

## 📌 About the Project

This project was created to practice fundamental Python programming concepts such as:

- Dictionaries
- Functions
- `if / elif / else` statements
- User input
- Type conversion with `int()`
- The `sum()` function
- f-strings
- Returning values from functions
- Calculating averages

The program currently supports four subjects:

- English
- Mathematics
- Biology
- Physics

---

## 🚀 Features

### 1. Student Score Input

The program asks the user to enter a score for each subject.

```python
student_grade = {
    "English": int(input("Enter your Score on English: ")),
    "Mathematics": int(input("Enter your score on Mathematics: ")),
    "Biology": int(input("Enter your score on Biology: ")),
    "Physics": int(input("Enter your score on Physics: "))
}
```

### 2. Automatic Grade Calculation

The program converts each score into a grade:

| Score | Grade | Comment |
|---:|:---:|---|
| 75–100 | A1 | Excellent |
| 70–74 | B2 | Very Good |
| 65–69 | B3 | Good |
| 60–64 | C4 | Credit |
| 55–59 | C5 | Credit |
| 45–54 | C6 | Credit |
| 40–44 | D7 | Pass |
| 35–39 | E8 | Pass |
| 0–34 | F9 | Fail |

### 3. Subject-Specific Functions

Each subject has its own grading function:

```python
english_grade()
math_grade()
biology_grade()
physics_grade()
```

These functions retrieve the student's score and determine the corresponding grade.

### 4. Average Calculation

The program calculates the student's total score using:

```python
total = sum(student_grade.values())
```

It then calculates the average:

```python
Average = total / 4
```

### 5. Overall Performance Comment

The program also provides an overall performance comment based on the student's average.

Examples:

```text
Excellent
Very Good
Good
Credit
Pass
Fail
```

---

## 💻 Example

### Input

```text
Enter your Score on English: 78
Enter your score on Mathematics: 72
Enter your score on Biology: 65
Enter your score on Physics: 58
```

### Output

```text
English A1
Mathematics B2
Biology B3
Physics C5

Your Average is 68.25 And You did Good
```

---

## 🧠 Python Concepts Practiced

This project helped practice several important Python concepts.

### Dictionary

```python
student_grade = {
    "English": 78,
    "Mathematics": 72,
    "Biology": 65,
    "Physics": 58
}
```

### Functions

```python
def english_grade():
    ...
```

### Conditional Statements

```python
if english >= 75:
    ...
elif english >= 70:
    ...
else:
    ...
```

### `sum()`

```python
total = sum(student_grade.values())
```

### Average

```python
Average = total / 4
```

### f-Strings

```python
return f"English {Grade}"
```

---

## 📂 Project Structure

```text
student-grade-calculator/
│
├── main.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-grade-calculator.git
```

### 2. Open the project

```bash
cd student-grade-calculator
```

### 3. Run the Python file

```bash
python main.py
```

---

## 🔮 Future Improvements

Some improvements I plan to make as I continue learning Python:

- [ ] Add more subjects
- [ ] Allow multiple students
- [ ] Add student names
- [ ] Validate scores so users cannot enter values below 0 or above 100
- [ ] Reduce repeated grading code
- [ ] Store student results in a file
- [ ] Generate a complete student report
- [ ] Add a simple menu system
- [ ] Add GPA calculation
- [ ] Build a graphical interface
- [ ] Store results using a database

---

## 📚 What I Learned

While building this project, I practiced how to:

- Store data in dictionaries
- Create and call functions
- Use conditional statements
- Get information from users with `input()`
- Convert strings to integers
- Calculate totals and averages
- Return values from functions
- Format output using f-strings

This is a **beginner Python project** and part of my journey toward becoming a better Python developer.

---

## 👨‍💻 Author

**Udeh Chibuike Marvelous**

### Skills I'm currently learning

- Python
- JavaScript
- HTML
- CSS
- Front-end Development
- Software Engineering

---

⭐ If you find this project useful, feel free to star the repository!
