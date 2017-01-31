Name: Nguyen Nguyen
UID: 004870721

The zip files contains HW1.pdf which is part A-D.

For part E, it contains Apriori.py and a test.csv file.

The script will prompt the user to input a filename WITH extension. For example, if the file name is test, the user will need to enter test.csv or test.txt.
The script will then prompt the user to input the minimum support. If the user does not enter a numeric value, then the script will end.
The script then initialize the Apriori class and go through the calculation. It will calculate frequent k-temsets basing on the provided file and min_sup.

The script was developed using Pycharm and uses csv and itertools package from standard Python Libraries.

========================================================================================================================

To run this script, the user can run it on an IDE or in console.
for example, in windows command prompt, the user can type: C:\python <Apriori.py location>. In mac,

Also, the script can be run in an IDE.

A sample input of a .csv or .txt file:
c,r,a
p,b
r,c,b
p,c,a
a,b,s,c
t,a,b,c


A sample output on screen from python script (given min_sup = 2):
Enter the file name with extension. For example, test.csv or test.txt
test.csv
Enter the minimum support.
2
r : 2
a : 4
p : 2
b : 4
c : 5
ca : 4
cr : 2
ab : 2
cb : 3
cab : 2
Press Enter Key to Continue


