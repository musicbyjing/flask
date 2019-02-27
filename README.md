# Flask notes

## Misc. Python notes

### Decorators
- Functions return a value based on given args
- Functions are **first-class objects** in Python, i.e. they can be passed around or used as args (remember *higher-order functions*???)
- **Decorators** are defined with `@` 

## Intro

- Using **virtual environments**: using a specific set of dependencies or Python version for a specific project, independent of other projects
   - `py -3 -m venv venv` to create, then `. venv/bin/activate` to activate
- `FLASK_ENV` *environment variable* is the name of the module Flask needs to import
- Set `FLASK_ENV` to `development` before running to enable **debug mode**, which lets you reload upon code changes and activates debugger
- 
