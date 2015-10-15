@ECHO off
selocal EnableDelayedExpansion

ECHO START RUN CASES
F:  
cd F:\testApp01  
start pythonw testSet\run.py
ECHO END RUN
PAUSE 

