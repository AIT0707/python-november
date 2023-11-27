# Scenario: Student Roster Management
student_roster = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
print(student_roster) # Output: ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava']

#Assignments:
    # 1. Append and Extend:

        # Append two new students, "William" and "Sophia", to the end of the list.
student_roster.append("William")
student_roster.append("Sophia") # Operator 'append' can add only 1 item, therefore each name appended seperatly 
print(student_roster) # Output: ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Sophia']

        # Extend the list with another list of students: ["James", "Isabella"]
new_students = ["James", "Isabella"]
student_roster.extend(new_students)
print(student_roster) # Output: ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'James', 'Isabella']

    # 2. Insert and Remove:

        # Insert "Mia" at the third position in the list.
student_roster.insert(2, "Mia") # We use index 2 because the first position has index 0.
print(student_roster) # Output:['Emma', 'Liam', 'Mia', 'Olivia', 'Noah', 'Ava', 'William', 'Sophia', 'James', 'Isabella']

        # Remove "Noah" from the list using the appropriate method.
student_roster.remove("Noah")
print(student_roster) # Output:['Emma', 'Liam', 'Mia', 'Olivia', 'Ava', 'William', 'Sophia', 'James', 'Isabella']

    # 3. Count and Index:

        # Count the occurrences of the name "Emma" in the list.
x=student_roster.count("Emma")
print(x) # Output: 1

        # Find the index of the first occurrence of "Ava" in the list.
x=student_roster.index("Ava")
print(x) # Output: 4

    # 4. Pop and Clear:
        
        # Pop the last element from the list.
student_roster.pop()
print(student_roster) # Output: ['Emma', 'Liam', 'Mia', 'Olivia', 'Ava', 'William', 'Sophia', 'James']

        # Clear the entire list of students.
student_roster.clear()
print(student_roster) # Output: []

    # 5. Copy, Reverse, and Sort:

        # Create a copy of the original list and store it as 'student_roster_copy'.
student_roster = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
student_roster_copy=student_roster.copy()
print(student_roster_copy) # Output: ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava']

        # Reverse the elements of the copied list.
student_roster_copy.reverse()
print(student_roster_copy) # Output: ['Ava', 'Noah', 'Olivia', 'Liam', 'Emma']

        # Sort the reversed list alphabetically.
student_roster_copy.sort(reverse=True)
print(student_roster_copy) # Output: ['Olivia', 'Noah', 'Liam', 'Emma', 'Ava']




