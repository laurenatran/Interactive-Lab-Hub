flite -voice slt -t "What is your zip code?"

arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_zipcode.wav
python3 test_words.py recorded_zipcode.wav