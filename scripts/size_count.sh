#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..
data=$base/data
sent=$data/sent

# measure time
SECONDS=0

# array for iteration, where year 2000 is missed
year_1=($(seq 1995 1 1999))
year_2=($(seq 2001 1 2015))

# count corpus size by each year
for i in "${year_1[@]}"
do
  wc $sent/$i.txt
done

for i in "${year_2[@]}"
do
  wc $sent/$i.txt
done

wc $sent/1995-2015.txt

echo "Time taken:"
echo "$SECONDS seconds"
