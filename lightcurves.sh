# This bash script runs the three programs in order.

echo 'Running primary.py ...'
python primary.py
echo 'Primary eclipse values stored. Running secondary.py ...'
sleep 1.5
python secondary.py
echo 'Secondary eclipse values stored. Running results.py ...'
sleep 1.5
python results.py
echo 'Done. Results have been stored in finaloutput.txt.'
