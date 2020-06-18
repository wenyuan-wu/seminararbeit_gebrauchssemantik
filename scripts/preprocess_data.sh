#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..
data=$base/data

mkdir -p $data/sent

# extract files from different years/folders, where year 2000 is missed
year_1=($(seq 1995 1 1999))
year_2=($(seq 2001 1 2010))
year_3=($(seq 2011 1 2015))

# measure time
SECONDS=0

# make sentence corpus for each year
for i in "${year_1[@]}"
do
  file_name=deu_news_${i}_1M
  mkdir -p $data/$file_name
  tar -xzvf $data/$file_name.tar.gz -C $data/$file_name
  cp $data/$file_name/$file_name-sentences.txt $data/sent/$i.txt
  cut -f2 $data/sent/$i.txt > $data/sent/$i.txt.cut
  mv $data/sent/$i.txt.cut $data/sent/$i.txt
  rm -R $data/$file_name
done

for i in "${year_2[@]}"
do
  file_name=deu_news_${i}_1M
  mkdir -p $data/$file_name
  tar -xzvf $data/$file_name.tar.gz -C $data/$file_name
  cp $data/$file_name/$file_name-sentences.txt $data/sent/$i.txt
  cut -f2 $data/sent/$i.txt > $data/sent/$i.txt.cut
  mv $data/sent/$i.txt.cut $data/sent/$i.txt
  rm -R $data/$file_name
done

# compressed file which has root folders
for i in "${year_3[@]}"
do
  file_name=deu_news_${i}_1M
  tar -xzvf $data/$file_name.tar.gz -C $data/
  cp $data/$file_name/$file_name-sentences.txt $data/sent/$i.txt
  cut -f2 $data/sent/$i.txt > $data/sent/$i.txt.cut
  mv $data/sent/$i.txt.cut $data/sent/$i.txt
  rm -R $data/$file_name
done

# combine all corpus
cat $data/sent/* > $data/sent/1995-2015.txt

# sizes of sentence corpus
echo "Sizes of data files:"
wc -l $data/sent/*

# sanity check
echo "At this point, please make sure that number of lines are as expected."

echo "Time taken:"
echo "$SECONDS seconds"