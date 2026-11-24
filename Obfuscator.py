import ast
import os
import random
import builtins
os.system('cls')
Path = input("Enter your path python file :")


with open(Path, 'r', encoding="utf-8") as f:
    codesource = f.read()



variable = ast.parse(codesource)
def gennamevariable():
    namevariable = ""
    for i in range(4):
        namevariable +=chr(random.randint(65, 90) if random.randint(0, 1) else random.randint(97, 122))
    return namevariable

class_methods = set()
importes_modules = set()
for node in ast.walk(variable):
 if isinstance(node, (ast.Import, ast.ImportFrom)):
        for alias in node.names:
            nom = alias.asname if alias.asname else alias.name
            importes_modules.add(nom.split('.')[0])
        if isinstance(node, ast.ImportFrom) and node.module:
            importes_modules.add(node.module.split('.')[0])
protected_words = set(dir(builtins)).union(importes_modules)
modified_variables = {}
def r(name):
    return name not in protected_words and not name.startswith("__")

def get_obfuscated_name(original_name):
    if original_name not in modified_variables:
        modified_variables[original_name] = gennamevariable()
    return modified_variables[original_name]

for node in ast.walk(variable):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        if r(node.name):
            get_obfuscated_name(node.name)
    elif isinstance(node, ast.arg):
        if r(node.arg):
            get_obfuscated_name(node.arg)
    elif isinstance(node, (ast.Global, ast.Nonlocal)):
        for name in node.names:
            if r(name):
                get_obfuscated_name(name)
    elif isinstance(node, ast.ExceptHandler) and node.name:
        if r(node.name):
            get_obfuscated_name(node.name)
    elif isinstance(node, ast.Name):
        if r(node.id):
            get_obfuscated_name(node.id)
for node in ast.walk(variable):
    if isinstance(node, ast.Name):
        if node.id in modified_variables:
            node.id = modified_variables[node.id]
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        if node.name in modified_variables:
            node.name = modified_variables[node.name]
    elif isinstance(node, ast.arg):
        if node.arg in modified_variables:
            node.arg = modified_variables[node.arg]
    elif isinstance(node, ast.keyword) and node.arg:
        if node.arg in modified_variables:
            node.arg = modified_variables[node.arg]
    elif isinstance(node, (ast.Global, ast.Nonlocal)):
        node.names = [modified_variables.get(n, n) for n in node.names]
    elif isinstance(node, ast.ExceptHandler) and node.name:
        if node.name in modified_variables:
            node.name = modified_variables[node.name]

with open(Path, 'w', encoding="utf-8") as f:
    f.write(ast.unparse(variable))

print(f"\nFichier modifié avec succès : {Path}")