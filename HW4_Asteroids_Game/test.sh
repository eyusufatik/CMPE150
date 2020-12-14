#!/bin/sh
echo "Starting tests..."
emptyline="\n"
for i in {1..16}
do
  echo ">testing input$i.txt"
  pythonout=$(python3 $1<input$i.txt>hw4tempcreatedbybash.txt)
  echo "$pythonout"
  output=$(diff hw4tempcreatedbybash.txt output$i.txt)
  if [[ $output = "" ]]
  then
    echo "Test$i passed successfully.\n"
  else
    echo "There is a problem in test$i"
    echo "diff command output: \n"
    echo "$output"
    echo "There was a problem in test$i. Above is the diff command otput."
    break
  fi
done