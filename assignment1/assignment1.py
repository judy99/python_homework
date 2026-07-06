# Task 1: Hello
def hello():
  return "Hello!"

print(f"Hello function returns: {hello()}")

# Task 2: Greet with a Formatted String
def greet(name):
  return "Hello, " + name + "!"

print(f"Greet function returns: {greet("Ann")}")

# Task 3: Calculator
# operation: add, subtract, multiply, divide, modulo, int_divide (for integer division) and power
def calc(a, b, operation="multiply"):
    result = None
    try:
        a_float = float(a)
        b_float = float(b)
    except ValueError:
        return "You can't " + operation + " those values!"
    
    match operation:
        case "add":
            result = a_float + b_float
        case "subtract":
            result = a_float - b_float
        case "multiply":
            result = a_float * b_float
        case "divide":
            try:
                result = a_float / b_float
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "modulo":
            try:
                result = int(a_float) % int(b_float)
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "int_divide":
            try:
                result = int(a_float) // int(b_float)
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "power":
            result = a_float ** int(b_float)
        case _:
            print("Unknown operation.")
    return result

print(f"Add: {calc(1,2,"add")}")

# Task 4: Data Type Conversion
def data_type_conversion(value, name):
    error_str = f"You can't convert {value} into a {name}."
    match name:
        case "float":
            try:
                return float(value)
            except:
                return error_str
        case "int":
            try:
                return int(value)
            except:
                return error_str
        case "str":
            try:
                return str(value)
            except:
                return error_str
        case _:
            return error_str
        
data_type_conversion(5, "str")
data_type_conversion(5, "float")
data_type_conversion(5, "int")
data_type_conversion(5.4, "str")
data_type_conversion(5.4, "float")
data_type_conversion(5.4, "int")
data_type_conversion("1", "int")
data_type_conversion("1.2", "float")
data_type_conversion("1.2", "int")
data_type_conversion("1.34", "str")
data_type_conversion("qwerty", "float")
        
# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg_res = int(sum(args)/len(args))
    except:
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
    
    for key, value in kwargs.items():
        score = score + value
        if (best == None or value > best_value):
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

print(titleize("hello in at Friday wd!"))

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    res = ""
    current_res = ""
    for i in range(len(guess)):
        current_res = ""
        j = 0
        for j in range(len(secret)):
            if secret[j] == guess[i]:
                current_res = current_res + guess[i]
            elif len(res) > 0 and res[j] != "_":
                current_res = current_res + res[j]
            else:
                current_res = current_res + "_"
        res = current_res
    return res

hangman("difficulty","ic")

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(origin):  
    latin_sentence = []
    origin_words = origin.split()
    vowels = "aeoui"
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
pig_latin("apple")                
                
            
    