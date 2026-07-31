import os
import subprocess
import sys

# This is a simplified simulation of a cloud AI agent's capability.
# In a real-world scenario, this would involve complex LLM interactions,
# cloud infrastructure provisioning, and robust error handling.

def execute_task(task_description):
    """Simulates an AI agent executing a task.

    Args:
        task_description (str): A description of the task to be performed.

    Returns:
        str: The result of the task execution.
    """
    print(f"AI Agent: Received task: '{task_description}'")

    # --- Simulation of AI Agent's 'thinking' and 'planning' ---
    # In a real agent, this would involve an LLM to break down the task,
    # identify necessary tools/commands, and plan execution steps.
    if "create a file named" in task_description.lower() and ".txt" in task_description.lower():
        filename = task_description.split("named ")[-1].split(".txt")[0] + ".txt"
        content = "This file was created by a simulated AI agent.\n"
        try:
            with open(filename, "w") as f:
                f.write(content)
            print(f"AI Agent: Successfully created file '{filename}'.")
            return f"File '{filename}' created successfully."
        except Exception as e:
            print(f"AI Agent: Error creating file '{filename}': {e}")
            return f"Error creating file '{filename}': {e}"

    elif "list files in current directory" in task_description.lower():
        try:
            files = os.listdir(".")
            print(f"AI Agent: Listing files.")
            return "Files in directory: " + ", ".join(files)
        except Exception as e:
            print(f"AI Agent: Error listing files: {e}")
            return f"Error listing files: {e}"

    elif "run python script" in task_description.lower():
        # This is a very basic simulation. Real agents would be more careful.
        script_name = task_description.split("run python script ")[-1].strip()
        if script_name.endswith(".py"):
            try:
                # Simulate running a script in a sandboxed environment if possible
                # For simplicity, we'll just run it directly here.
                print(f"AI Agent: Executing Python script '{script_name}'...")
                result = subprocess.run([sys.executable, script_name], capture_output=True, text=True, check=True)
                return f"Script '{script_name}' output:\n{result.stdout}\nError:\n{result.stderr}"
            except FileNotFoundError:
                return f"Error: Script '{script_name}' not found."
            except subprocess.CalledProcessError as e:
                return f"Error running script '{script_name}':\n{e.stdout}\n{e.stderr}"
            except Exception as e:
                return f"An unexpected error occurred while running script '{script_name}': {e}"
        else:
            return f"Error: '{script_name}' is not a valid Python script."

    else:
        print("AI Agent: Task not understood or supported by this simulation.")
        return "Task not understood."

if __name__ == "__main__":
    # Example usage:
    print("--- Simulating Cloud AI Agent Execution ---")

    # Task 1: Create a file
    task1_desc = "Create a file named my_document.txt with some initial content."
    result1 = execute_task(task1_desc)
    print(f"User: Task 1 Result: {result1}\n")

    # Task 2: List files
    task2_desc = "List files in the current directory."
    result2 = execute_task(task2_desc)
    print(f"User: Task 2 Result: {result2}\n")

    # Task 3: Simulate running a simple Python script (create a dummy script first)
    dummy_script_content = "print('Hello from dummy script!')\nimport os\nprint(f'Current dir from script: {os.getcwd()}')"
    with open("dummy_script.py", "w") as f:
        f.write(dummy_script_content)
    print("Created dummy_script.py for demonstration.")

    task3_desc = "Run python script dummy_script.py."
    result3 = execute_task(task3_desc)
    print(f"User: Task 3 Result: {result3}\n")

    # Clean up dummy script
    if os.path.exists("dummy_script.py"):
        os.remove("dummy_script.py")
        print("Cleaned up dummy_script.py.")
    if os.path.exists("my_document.txt"):
        os.remove("my_document.txt")
        print("Cleaned up my_document.txt.")

    print("--- Simulation Complete ---")
