""" from datetime import datetime


def save_markdown(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result)
    print(f"Newsletter saved as {filename}") """

from datetime import datetime
import os

def save_markdown(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    # Set the directory path where you want to save the files
    directory = '/home/riju279/Documents/Code/Mushroom/crewai-updated-tutorial-hierarchical/blogs/'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Set the filename with today's date
    filename = os.path.join(directory, f"{today_date}.md")
    
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.results)
    
    print(f"Newsletter saved as {filename}")

