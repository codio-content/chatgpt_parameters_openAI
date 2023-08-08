import os
import subprocess
import sys

sys.path.append('/usr/share/codio/assessments')
from lib.grade import send_partial_v2, FORMAT_V2_MD, FORMAT_V2_HTML, FORMAT_V2_TXT

f = open("ktest1.py", "r")
flag=0
respline=[]

for x in f:
  if "ChatCompletion.create" in x:
    flag=1
  if ")" in x and flag ==1:
    flag=2
  if flag>0:
    respline.append(x.strip())
  if flag==2:
    flag=0

f.close()

feedback=''
global points 
points = 100

respline=' '.join(respline)
firstP=respline.find('(')
lastP=respline.rfind(')')
respline=respline[firstP+1:lastP]
d = dict(map(str.strip, x.split("=")) for x in respline.split(",") if "=" in x)

total=5
for a,b in d.items():
  if "temperature" in a:
    if float(b.strip())!=(1 or 2):
      total-=1
      feedback+="Please check your randomness variable. It should be set to maximum which is 1.\n"
  if "max_tokens" in a:
    if int(b)!=25:
      total-=1
      feedback+="Completion token limit should be set 25.\n"
  if "n" in a:
    if int(b)!= 6:
      #feedback+="You should generate 6 responses.\n"
      total-=1

def check_variable1():
  if total !=4:
    return False
  return True 

def check_variable2():
  global feedback
  if len(d) != 5:
    feedback+="Please make sure that only necessary arguments are included according to the requirements.\n"
    return False
  return True


def check_variable_counter():
  global feedback
  try: 
    import ktest1 
    return True
  except:
    feedback+="Please make sure your code is not generating any error before submission\n"
    return False

if not check_variable1():
  points -= 30
  feedback+= "<h2>Test did not pass</h2>\n"

if not check_variable2():
  points -= 30
  feedback+="<h2>Test did not pass</h2>\n"

if not check_variable_counter():
  points -= 40
  feedback+="<h2>Test did not pass</h2>\n"
  feedback+='Please make sure to fix code\n'

if feedback == "":
  feedback = "<h2>Test passed</h2>\n"

res = send_partial_v2(points, feedback, FORMAT_V2_HTML)
exit(0 if res else 1)
