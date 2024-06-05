#!/bin/bash

# Start process.py in the background


python pull-service.py &
FILE1_PID=$!

python app.py





cleanup() {
    echo "Stopping services..."
    kill $FILE1_PID $FILE2_PID  # Kill both processes
    exit
}


# Trap termination signals together
trap cleanup INT TERM


while true; do
    if ! kill -0 $FILE2_PID >/dev/null 2>&1; then
        echo "pull-service.py has exited."
        exit 1
    fi
    sleep 1
done
