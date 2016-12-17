# This bash script runs the three programs in order.

#echo 'Enter the name of your dataset:'
#read dataset

echo 'Running primary.py ...'
sleep 0.5
python primary.py

echo 'Primary eclipse values stored. Running secondary.py ...'
sleep 1.5
python secondary.py

echo 'Secondary eclipse values stored. Running results.py ...'
sleep 1.5

python results.py
echo 'Done. Results have been stored in an output file.'


