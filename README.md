# 🔐 Python Password Generator

A secure and customizable password generator built with Python. Generate strong passwords with your preferred combination of characters.

## ✨ Features

- **Customizable Length**: Choose any password length you need
- **Character Options**: 
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z) 
  - Numbers (0-9)
  - Special symbols (!@#$%^&*()_+-=[]{}|;:,.<>?/)
- **Random Generation**: Uses Python's secure random module
- **Interactive Interface**: User-friendly command-line interface

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Running the Program
```bash
python main.py
```

## 📋 Usage

1. **Start the program**: Run `python main.py`
2. **Enter password length**: Input how many characters you want
3. **Choose character types**: Specify how many of each type:
   - Letters (uppercase & lowercase)
   - Numbers
   - Symbols
4. **Get your password**: The program generates a secure, randomized password

## 🔧 Code Structure

```python
# Main components:
- Character sets (uppercase, lowercase, numbers, symbols)
- User input handling
- Random password generation
- Password shuffling for security
```

## 🛡️ Security Features

- Uses `random.choice()` for secure randomization
- Shuffles final password to avoid predictable patterns
- No password storage - generated on-demand only

## 📱 Example Output

```
Welcome to the PyPassword Generator!
How many letters would you like in your password? 8
How many numbers would you like? 3
How many symbols would you like? 2

Your generated password is: aB7#kL9@mP2!x
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.

---
**Created by**: funix-phanphuctruong  
**Language**: Python  
**Version**: 2.0
