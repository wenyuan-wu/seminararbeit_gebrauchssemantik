#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..
data=$base/data

#year_1=( 1995 1996 2013 2014 2015 )
#year_2=( 1995 1996 2013 2014 2015 )
year=( 1995 )

for i in "${year[@]}"
do
#  echo "this_$i"
  file_name=deu_news_${i}_1M
  tar -xzvf $data/$file_name.tar.gz

done

#
#cut -f2 input
#
#
#
#cut -f2 csbulletin-1-20.tsv | sort | uniq -c | sort -rn | head -n50
#
## download preprocessed data
#
#wget https://files.ifi.uzh.ch/cl/archiv/2020/mt20/data.tar.gz -P $base
#tar -xzvf $base/data.tar.gz
#
#rm $base/data.tar.gz
#
## download shared models (truecasing and BPE model, vocabulary files)
#
#wget https://files.ifi.uzh.ch/cl/archiv/2020/mt20/shared_models.tar.gz -P $base
#tar -xzvf $base/shared_models.tar.gz
#
#rm $base/shared_models.tar.gz
#
## sizes
#echo "Sizes of data files:"
#wc -l $data/*
#
#echo "Sizes of shared_model files:"
#wc -l $shared_models/*
#
## sanity checks
#echo "At this point, please make sure that 1) number of lines are as expected, 2) language suffixes are correct and 3) files are parallel"
