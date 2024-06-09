# eligibility to enter for professional course
math_marks = int(input('Enter Marks of Maths'))
physics_marks = int(input('Enter Marks of Physics'))
chemistry_marks = int(input('Enter Marks of Chemistry'))

total_marks = 190
total_maths_physics = 140
total_input_marks = math_marks + physics_marks + chemistry_marks

if total_input_marks >= total_marks:
    print('Eligible')
else:
    print('Not Eligible')    
