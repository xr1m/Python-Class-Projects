"""
Python Learning Project - Main Entry Point
This project contains various Python learning exercises organized by class.
"""

import os
import sys
import subprocess


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name != 'nt' else 'cls')


def list_python_files(directory):
    """List all Python files in a directory."""
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith('.py')]


def run_script(filepath):
    """Run a Python script and return to menu."""
    clear_screen()
    print(f"\n{'='*60}")
    print(f"Running: {filepath}")
    print(f"{'='*60}\n")
    
    try:
        subprocess.run([sys.executable, filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError running script: {e}")
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
    
    print(f"\n{'='*60}")
    input("\nPress Enter to return to menu...")


def display_menu():
    """Display the main menu and handle user selection."""
    while True:
        clear_screen()
        print("="*60)
        print(" "*15 + "PYTHON LEARNING PROJECT")
        print("="*60)
        print("\nSelect a category:\n")
        
        categories = {
            '1': ('Class 1', 'Class 1'),
            '2': ('Class 2', 'Class 2'),
            '3': ('Class 3', 'Class 3'),
            '4': ('Class 4', 'Class 4'),
            '5': ('Activities', 'Activites'),
            '6': ('After Class Projects', 'After Class Projects'),
            '0': ('Exit', None)
        }
        
        for key, (display_name, _) in categories.items():
            print(f"  {key}. {display_name}")
        
        print("\n" + "="*60)
        choice = input("\nEnter your choice (0-6): ").strip()
        
        if choice == '0':
            clear_screen()
            print("\nThank you for using Python Learning Project!")
            sys.exit(0)
        
        if choice not in categories:
            input("\nInvalid choice! Press Enter to continue...")
            continue
        
        display_name, directory = categories[choice]
        
        if directory is None:
            continue
        
        # List files in selected category
        python_files = list_python_files(directory)
        
        if not python_files:
            input(f"\nNo Python files found in {display_name}. Press Enter to continue...")
            continue
        
        # Show files menu
        while True:
            clear_screen()
            print("="*60)
            print(f"{display_name} - Select a script to run:")
            print("="*60)
            print()
            
            for idx, filename in enumerate(python_files, 1):
                print(f"  {idx}. {filename}")
            
            print(f"  0. Back to main menu")
            print("\n" + "="*60)
            
            file_choice = input("\nEnter your choice: ").strip()
            
            if file_choice == '0':
                break
            
            try:
                file_idx = int(file_choice) - 1
                if 0 <= file_idx < len(python_files):
                    filepath = os.path.join(directory, python_files[file_idx])
                    run_script(filepath)
                else:
                    input("\nInvalid choice! Press Enter to continue...")
            except ValueError:
                input("\nInvalid input! Press Enter to continue...")


if __name__ == "__main__":
    try:
        display_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nProgram terminated by user. Goodbye!")
        sys.exit(0)
