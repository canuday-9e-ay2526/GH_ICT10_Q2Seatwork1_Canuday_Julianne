#Math Club checker
from pyscript import display, document

def view_member(e):
    document.getElementById('result').innerHTML = ' '
    student_first = document.getElementById('firstname').value
    student_last = document.getElementById('lastname').value

    student_name = str(student_first) + " " + str(student_last) # Combine input values

    Math_members = ['Aisha Padua', 'Julianne Canuday', 'Pocholo Commanda', 'Jesse Villante', 'Dwayne Chua', 'Rachmiel Lozada', 'Alonzo Paulino', 'Zoe Laquindanum', 'Clarisse Casal', 'Zedric Ramirez', 'Megan Ty', 'Reina Fortaleza']
    member_checker = student_name in Math_members # checks boolean 0 or 1

    display_message = (f'Sorry, you are not included in Math club', f'Congratulations {student_name}, you are part of Math club')
    display(display_message[member_checker], target='result')