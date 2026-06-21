# Import the 'os' to let Python talk to computer's operating system
import os

def create_daily_logs():
    #Ask the user to type a name and save
    folder_name = input("Enter a name for your new folder: ")
    
    #Check if the folder does NOT exist yet
    if not os.path.exists(folder_name):
        # Create the new folder in your computer
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")
    
    #Create a list of the days to make files for
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    #Start a FOR loop
    for day in days:
        #Combine the folder name and file name 
        file_path = os.path.join(folder_name, f"{day}.txt")
        
        #Ask the user what they want to write inside the specific day file
        user_notes = input(f"Enter your main task for {day}: ")
        
        #Open the file in write mode ('w')
        with open(file_path, "w") as file:
            #Write the header lines into the text file
            file.write(f"--- Notes for {day} ---\n\n")
            file.write("Tasks to complete:\n")
            #Write the user's custom note into the file
            file.write(f"- {user_notes}\n")
            
        #Print a success message for this specific file in the terminal
        print(f"Saved and created file: {day}.txt\n")

    # Print a final message when the whole loop finishes
    print("Success! All files created automatically with your custom data.")

# Main 
if __name__ == "__main__":
    create_daily_logs()
