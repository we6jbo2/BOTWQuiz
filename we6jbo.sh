#!/bin/bash

# Jeremiah O'Neal
# September 6, 2020
# This program will check for updates and then it will lauch BOTWQuiz
# Note that in order for the program to check for updates, a special file
# needs to be created.

#update

#script is from: https://stackoverflow.com/questions/35365799/shell-script-self-update-using-git

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
SCRIPTNAME="$0"
ARGS="$@"
BRANCH="master"

self_update() {
    notify-send "Checking for updates..."
    sleep 10
    echo `date +%s >> update_debugger.txt`
    cd $SCRIPTPATH
    git fetch

    [ -n $(git diff --name-only origin/$BRANCH | grep $SCRIPTNAME) ] && {
        notify-send "Found a new version of BOTWQuiz-clone. Updating!"
        echo "Found a new version of me, updating myself..."
        git pull --force
        git checkout $BRANCH
        git pull --force
        echo "Running the new version..."
        #exec "$SCRIPTNAME" "$@"

        # Now exit this old instance
        #exit 1
    }
    echo "Either updated or already the latest version."
}

main() {
   notify-send "Running BOTWQuiz-clone!"
   echo "Running"


   #loop
#   while [ true ]
#   do

      echo Running ...
#      echo Checking to see if the config file exists, if not, copy into directory
#      if [ ! -f ../BOTWQuiz-config/ssh-nao-config-we6jbo2.edn ]; then
#         echo The config file is missing...
#         mkdir ../BOTWQuiz-config
#         cp config/ssh-nao-config-we6jbo2.edn ../BOTWQuiz-config/
#         notify-send "Copied config file. Running BOTWQuiz-clone!"
#      fi   
#      lein run ../BOTWQuiz-config/ssh-nao-config-we6jbo2.edn
      pwd
      cp ~/BOTWcode/BOTWQuiz.py ~/BOTWQuiz/BOTWQuiz.py
      cd ~/BOTWQuiz
      python3 BOTWQuiz.py
      echo Sleeping ...
      sleep 1200
#      done
}
if test -f ~/dontdelete-2428591225.txt; then
   self_update
fi
main
