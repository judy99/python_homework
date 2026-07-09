# Task 1: Hello
def hello():
  return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
  return f"Hello, {name}!"

# Task 3: Calculator
# operation: add, subtract, multiply, divide, modulo, int_divide (for integer division) and power
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a/b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                print("Unknown operation.")
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operation} those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, name):
    error_str = f"You can't convert {value} into a {name}."
    match name:
        case "float":
            try:
                return float(value)
            except ValueError:
                return error_str
        case "int":
            try:
                return int(value)
            except ValueError:
                return error_str
        case "str":
            return str(value)
        case _:
            return error_str
                
# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg_res = sum(args)/len(args)
    except TypeError:
        return "Invalid data was provided."
    except ZeroDivisionError:
        return "Invalid data was provided."
    
    if (avg_res >= 90):
        return "A"
    elif (avg_res >= 80):
        return "B"
    elif (avg_res >= 70):
        return "C"
    elif (avg_res >= 60):
        return "D"
    else:
        return "F"

grade(85, 90, 76)

#Task 6: Use a For Loop with a Range
def repeat(s, count):
    res = ""
    for _ in range(count):
        res = f"{res}{s}"
    return res

# Task 7: Student Scores, Using **kwargs
def student_scores(p, **kwargs):
    score = 0
    best = None
    best_value = None
    
    for key, value in kwargs.items():
        score = score + value
        if best is None or value > best_value:
            best_value = value
            best = key
    if (p == "mean"):
        return score/len(kwargs)
    if (p == "best"):
        return best
    
# Task 8: Titleize, with String and List Operations
def titleize(s):
    words = s.split() # str to list
    res = ""
    for i, word in enumerate(words):
        if len(word) > 3 or i == len(words) - 1 or i == 0:
            res = f"{res} {word.capitalize()}"
        else:
            res = f"{res} {word}"
    return res.strip()

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    res = ""
    for i in range(len(secret)):
        if secret[i] in guess:
            res = res + secret[i]
        else:
            res = res + "_"
    return res

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(origin):  
    latin_sentence = []
    origin_words = origin.split()
    vowels = "aeiou"
    latin_word = ""
    
    for word in origin_words:
        if word[0] in vowels:
            latin_word = word + "ay"
        else:
            to_end = ""
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    to_end += "qu"
                    i += 2
                else:
                    to_end += word[i]
                    i += 1
            latin_word = word[i:] + to_end + "ay"
        latin_sentence.append(latin_word)
    return " ".join(latin_sentence)                
