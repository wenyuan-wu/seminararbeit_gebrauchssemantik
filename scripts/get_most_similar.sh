#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..
data=$base/data
models=$base/models

# measure time
SECONDS=0

# array for iteration, where year 2000 is missed
year_1=($(seq 1995 1 1999))
year_2=($(seq 2001 1 2015))

# datenschutz
echo "datenschutz"
for i in "${year_1[@]}"
do
  echo "year: $i"
  python most_similar.py -m $models/$i-model -w datenschutz
  echo "================================================="
done

for i in "${year_2[@]}"
do
  echo "year: $i"
  python most_similar.py -m $models/$i-model -w datenschutz
  echo "================================================="
done

echo "year: 1995-2015"
python most_similar.py -m $models/1995-2015-model -w datenschutz
echo "================================================="


# privatsphäre
echo "privatsphäre"
for i in "${year_1[@]}"
do
  echo "year: $i"
  python most_similar.py -m $models/$i-model -w privatsphäre
  echo "================================================="
done

for i in "${year_2[@]}"
do
  echo "year: $i"
  python most_similar.py -m $models/$i-model -w privatsphäre
  echo "================================================="
done

echo "year: 1995-2015"
python most_similar.py -m $models/1995-2015-model -w privatsphäre
echo "================================================="


echo "Time taken:"
echo "$SECONDS seconds"
