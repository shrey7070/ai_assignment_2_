#!/bin/bash

# Function for state representation
state_representation() {
    local file_name=$1

    # Check if the selected file exists
    if [ -f "$file_name" ]; then
        python3 main.py "print" "$file_name"
    else
        echo "Error: File not found. Please ensure the file exists."
    fi
}

# Function to check whether the puzzle is solved or not
done_state() {
    local file_name=$1

    # Check if the selected file exists
    if [ -f "$file_name" ]; then
        python3 main.py "done" "$file_name"
    else
        echo "Error: File not found. Please ensure the file exists."
    fi
}

# Function to print all the available moves
available_moves() {
    local file_name=$1

    # Check if the selected file exists
    if [ -f "$file_name" ]; then
        python3 main.py "availableMoves" "$file_name"
    else
        echo "Error: File not found. Please ensure the file exists."
    fi
}

# Function to apply moves
apply_move() {
    local file_name=$1
    local move=$2

    # Check if the selected file exists
    if [ -f "$file_name" ]; then
        python3 main.py "applyMove" "$file_name" "$move"
    else
        echo "Error: File not found. Please ensure the file exists."
    fi
}

# Function to compare two state files
compare_states() {
    local file1=$1
    local file2=$2

    # Check if both files exist
    if [ -f "$file1" ] && [ -f "$file2" ]; then
        python3 main.py "compare" "$file1" "$file2"
    else
        echo "Error: One or both files do not exist. Please check the file paths."
    fi
}

# Function to normalize a state file
normalize_state() {
    local file_name=$1

    # Check if the selected file exists
    if [ -f "$file_name" ]; then
        python3 main.py "norm" "$file_name"
    else
        echo "Error: File not found. Please ensure the file exists."
    fi
}

# Main function to handle input arguments
main() {
    if [ "$#" -lt 2 ]; then
        echo "Error: Insufficient arguments provided."
        echo
        echo "  $0 print <file_name>"
        echo "  $0 done <file_name>"
        echo "  $0 availableMoves <file_name>"
        echo "  $0 applyMove <file_name> <move>"
        echo "  $0 compare <file1> <file2>"
        echo "  $0 norm <file_name>"
        exit 1
    fi

    local action=$1
    local file_name=$2
    local move=$3
    case $action in
        print) state_representation "$file_name" ;;
        done) done_state "$file_name" ;;
        availableMoves) available_moves "$file_name" ;;
        applyMove)
            if [ -z "$move" ]; then
                echo "Error: Move argument missing for applyMove."
                echo "Example: $0 applyMove SBP-levels/SBP-level1.txt \"(3,down)\""
                exit 1
            fi
            apply_move "$file_name" "$move"
            ;;
        compare)
            if [ "$#" -ne 3 ]; then
                echo "Error: Missing file paths for compare."
                echo "Example: $0 compare <file1> <file2>"
                exit 1
            fi
            compare_states "$2" "$3"
            ;;
        norm) normalize_state "$file_name" ;;  # Handle normalize action
        *)
            echo "Invalid action: $action"
            echo "Supported actions: print, done, availableMoves, applyMove"
            exit 1
            ;;
    esac
}

# Call the main function with all script arguments
main "$@"