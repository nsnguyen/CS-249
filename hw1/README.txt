Name: Nguyen Nguyen
UID: 004870721

The zip files contains HW1.pdf which is part A-D.

For part E, it contains Apriori.py and a test.csv file.



========================================================================================================================

To run this script, the user can run it on an IDE (if the Python intepreter is setup correctly) or in console preferably.

For example, in windows or MacOS, the user can type: C:\python <Apriori.py location>.

Assumptions: File name is static and set it as run_file.csv. File contains only single alphabet character in ascending order (though it doesn't matter) and is comma separated value.

In the beginning, the script will prompt the user to input the minimum support. If the user does not enter a numeric value, then the script will return a response and terminate.
If the user inputs valid min_sup value, the script then initialize the Apriori class and go through the calculation. It will calculate frequent k-temsets basing on the provided file and min_sup.

Development: The script was developed using Pycharm and uses csv and itertools package from standard Python Libraries.

Sample Input:
A sample input of a .csv or .txt file:
a,b,c,d,e,f,g,h,i,j,k,l,m,n
o,p,q,r,s,t,u,v,w,x,y,z
a,b,c,d
a,b,c,d
e,f,g,h
h,i,j,k,l
a,o,p
a,o,r,s,t,u
x,y,z
z
a,b,c,d,e
a,b,c,d
a,b
h,j,k,m
i,n,o,p,q
a,b,c
r,s,t,u,v
a,h,j,k
j,k



Sample Output:
A sample output on screen from python script (given min_sup = 5):

Make sure that your input file is name run_file.csv and is in the same folder as Apriori.py script.
Enter the minimum support.
5
j : 5
k : 5
h : 5
b : 7
c : 6
a : 10
d : 5
ad : 5
jk : 5
ac : 6
ab : 7
bc : 6
cd : 5
bd : 5
bcd : 5
abc : 6
abd : 5
acd : 5
abcd : 5
Press Enter Key to Continue

