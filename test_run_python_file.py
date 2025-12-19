from functions.run_python_file import run_python_file

def test():    
    output = run_python_file("calculator", "main.py")
    print('running run_python_file("calculator", "main.py")')
    print(output)
    print("")

    output = run_python_file("calculator", "main.py", ["3 + 5"])
    print('running run_python_file("calculator", "main.py", ["3 + 5"])')
    print(output)
    print("")

    output = run_python_file("calculator", "tests.py")
    print('running run_python_file("calculator", "tests.py")')
    print(output)
    print("")

    output = run_python_file("calculator", "../main.py")
    print('running run_python_file("calculator", "../main.py")')
    print(output)
    print("")

    output = run_python_file("calculator", "nonexistent.py")
    print('running run_python_file("calculator", "nonexistent.py")')
    print(output)
    print("")

    output = run_python_file("calculator", "lorem.txt")
    print('running run_python_file("calculator", "lorem.txt")')
    print(output)
    print("")

if __name__ == "__main__":
    test()
