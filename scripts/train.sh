#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..
data=$base/data
sent=$data/sent
models=$base/models

mkdir -p $models

# measure time
SECONDS=0

# array for iteration, where year 2000 is missed
year_1=($(seq 1995 1 1999))
year_2=($(seq 2001 1 2015))

# train model from corpus by each year
for i in "${year_1[@]}"
do
  python train_model.py -i $sent/$i.txt -o $models/$i-model
done

for i in "${year_2[@]}"
do
  python train_model.py -i $sent/$i.txt -o $models/$i-model
done

python train_model.py -i $sent/1995-2015.txt -o $models/1995-2015-model

echo "Time taken:"
echo "$SECONDS seconds"
