# phrase-counter

One-time virtual environment set-up:
```
python3 -m venv .venv   
```

Run everytime we want to spin the virtual environment:
```
source .venv/bin/activate
```
Run the program with 
```
python main.py 
```
Run to get ot of venv
```
deactivate
```

```
Program accepts stdin.
To change file permissions and make it executable: chmod u+x main.py 
Then you can run: cat text.txt | ./main.py
```


What does the program do?
Program will count 3-word phrases
Ignore capitalization
Ignore punctuation