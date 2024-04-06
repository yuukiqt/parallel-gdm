#!/bin/bash
while true; do
    echo "Choose an option:"
    echo "1. Start node service"
    echo "2. Stop node service"
    echo "3. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Starting node service..."
            nohup python run_worker.py >/dev/null 2>&1 &
            exit
            ;;
        2)
            echo "Stopping node service..."
            pid=$(pgrep -f "python run_worker.py")
            if [ -n "$pid" ]; then
                kill "$pid"
                echo "Node service stopped."
            else
                echo "Node service is not running."
            fi
            exit
            ;;
        3)
            echo "Exiting..."
            exit
            ;;
        *)
            echo "Invalid choice. Please choose 1, 2, or 3."
            ;;
    esac
done
