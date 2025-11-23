# Student Grade Calculator

- Accepts marks of different subjects  
- Calculates total and average  
- Determines grade  
- Gives feedback  

# Objectives
- Take user input for marks  
- Perform calculations using basic programming concepts  
- Use conditional statements for grading  
- Display clear output for the user  

# Features
- Input marks for 5 subjects  
- Calculates:
  - Total Marks  
  - Average Marks  
  - Grade (A/B/C/D/Fail)  
- Simple feedback message  
- Error handling for invalid input  

# Top-Down Design
1. Input marks  
2. Calculate total  
3. Calculate average  
4. Determine grade  
5. Display result

# Algorithm
1. Start  
2. Set total = 0  
3. Repeat 5 times:  
   - Take subject mark  
   - Add to total  
4. average = total / 5  
5. If average >= 90 → Grade A  
   Else if >= 75 → Grade B  
   Else if >= 60 → Grade C  
   Else if >= 40 → Grade D  
   Else → Fail  
6. Print total, average, grade  
7. End  

