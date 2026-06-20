# Import the 'os' module to let Python talk to your computer's operating system
import os

def create_daily_logs():
    # 1. Ask the user to type a name and save it as text in 'folder_name'
    folder_name = input("Enter a name for your new folder: ")
    
    # 2. Check if the folder does NOT exist yet
    if not os.path.exists(folder_name):
        # Create the new folder on your computer
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")
    
    # 3. Create a list of the days we want to make files for
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # 4. Start a loop to go through each day in our list one by one
    for day in days:
        # Combine the folder name and file name (e.g., "MyFolder/Monday.txt")
        file_path = os.path.join(folder_name, f"{day}.txt")
        
        # Ask the user what they want to write inside this specific day's file
        user_notes = input(f"Enter your main task for {day}: ")
        
        # 5. Open the file in write mode ('w'). This creates the file!
        with open(file_path, "w") as file:
            # Write the header lines into the text file
            file.write(f"--- Notes for {day} ---\n\n")
            file.write("Tasks to complete:\n")
            # Write the user's custom note into the file
            file.write(f"- {user_notes}\n")
            
        # Print a success message for this specific file in the terminal
        print(f"Saved and created file: {day}.txt\n")

    # Print a final message when the whole loop finishes
    print("Success! All files created automatically with your custom data.")

# This line tells Python to start running our function as soon as the script opens
if __name__ == "__main__":
    create_daily_logs()
