:: DON'T TOUCH THIS FILE, THIS FILE WILL START YOUR SERVER!
:: EDIT IT BY YOURSELF AT YOUR OWN RISK, WE ARE NOT REPONSIBLE OF YOUR ACTS.
:: ------------------------------------
::  DON'T FORGET TO CALL YOUR JAR FILE "Server.jar"
:: ------------------------------------

@echo off
title BlockHost Server Manager - New session

echo Hello, if you are sure to run this server, press ENTER. If you missclicked on BlockHost, directly closes this CMD.
pause
echo blockhost: Server started
echo -------------------------------------
java -Xmx1024M -Xms1024M -jar Server.jar