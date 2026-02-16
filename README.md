# 🧠 Python Console Quiz Application

A simple and interactive **console-based quiz application** built using Python.

This project demonstrates the use of:
- Dictionaries
- Nested data structures
- Loops
- Input validation
- Functions
- Score calculation
- Percentage formatting

---

## 🚀 Features

✅ Multiple-choice questions (A/B/C/D format)  
✅ Input validation (prevents invalid answers)  
✅ Instant feedback (Correct / Wrong)  
✅ Displays correct answer when wrong  
✅ Final score calculation  
✅ Percentage calculation  
✅ Clean and structured output  

---

## 📂 Project Structure

```
quiz.py
README.md
```

---

## 🧠 Data Structure Used

Questions are stored using a nested dictionary structure:

```python
{
    "Question text": {
        "options": ["Option1", "Option2", "Option3", "Option4"],
        "answer": "A"
    }
}
```

- **Key** → Question  
- **Value** → Dictionary containing:
  - List of options
  - Correct answer  

---

## ▶️ How to Run

1. Make sure Python is installed:
   ```
   python --version
   ```

2. Run the program:
   ```
   python quiz.py
   ```

---

## 📊 Sample Output

```
Question 1: What is the capital of India?
A. Mumbai
B. Delhi
C. Chennai
D. Kolkata

Enter your answer (A/B/C/D): B
Correct! ✅

Your final score is: 5 / 6
Percentage: 83.33%
```

---

## 📚 Concepts Practiced

- Dictionary iteration using `.items()`
- `enumerate()` for numbering
- ASCII character handling using `chr()`
- Input validation using loops
- String methods (`strip()`, `upper()`)
- Score and percentage calculation
- Clean function-based program design

---

## 🎯 Learning Outcome

This project helped me improve:

- Logical thinking
- Handling nested data
- Writing structured and interactive programs
- Implementing validation in user input
- Formatting program output cleanly

---

## 🔮 Future Improvements

- Add difficulty levels
- Shuffle questions randomly
- Add replay option
- Add timer feature
- Store high scores

---

## 👨‍💻 Author

Theerthan N

---

⭐ If you like this project, feel free to star the repository!
