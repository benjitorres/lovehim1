#!/bin/bash

echo "hello hello!"
echo "Please enter a topic to find a Bible verse:"

read topic

echo "Generating verse..."

python3 get_verse.py "$topic"
