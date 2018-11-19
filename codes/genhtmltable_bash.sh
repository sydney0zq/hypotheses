#!/bin/bash

[ "$1" == "" ] && echo "Usage: tablegen.sh <ROW> <COLUMN>" && exit

echo "<table>"

for k in $( seq 1 $1 )
do
    echo "  <tr>"
    for j in $( seq 1 $2 )
    do
        echo -n '    <td>'
        echo    '</td>'
    done
    echo "  </tr>"
done

echo "</table>"
