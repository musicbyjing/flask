# Python

## Basics and variables

- Single line comments with `#`
- Wrap multiline comments with `'''` or `"""`
- No semicolons in Python!!
- No need to declare **variable types**
   ```
   x = 1          # int
   isCool = True  # bool
   name = 'John'  # str
   ```
- **Multiple assignment** works for vars:
   ```
   x, isCool, name = (1, True, 'John')
   ```
- `type(VAR)` returns the type of VAR
- **Cast** variables using `str(VAR)`, `int(VAR)`, etc.

## Strings

- To concatenate different types to strings, need to cast them to string
- **String formatting** exists
   - Arguments by position:
      ```
      name = 'Joe'
      age = 66
      print('My name is {name} and I am {age}'.format(name=name, age=age))
      ```
   - *F-Strings* (3.6+), kind of like in JavaScript:
      ```
      print(f'My name is {name} and I am {age}')
      ```
- String methods of interest: 

   <!-- --> | <!-- -->
   ---|---
   `len(str)` | length; works for most data types
   `replace(str1, str2)` | replace str1 with str2
   `str.count(t)` | counts the number of occurrences of t in str
   `str.split()` | turns str into a list
   


`len()` returns 


### Decorators

- Functions return a value based on given args
- Functions are **first-class objects** in Python, i.e. they can be passed around or used as args (remember *higher-order functions*???)
- **Decorators** are defined with `@` 

# Flask

## Intro

- Using **virtual environments**: using a specific set of dependencies or Python version for a specific project, independent of other projects
   - `py -3 -m venv venv` to create, then `. venv/bin/activate` to activate
- `FLASK_ENV` *environment variable* is the name of the module Flask needs to import
- Set `FLASK_ENV` to `development` before running to enable **debug mode**, which lets you reload upon code changes and activates debugger
- 
