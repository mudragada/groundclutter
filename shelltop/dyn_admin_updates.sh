##########################################################################
##  Version:         0.1 - 08/20/2014 - Krishna Mudragada               ##
##                   0.2 - 08/22/2014 - Krishna Mudragada               ##
##                   0.3 - 03/12/2015 - Krishna Mudragada               ##
##                   0.4 - 05/11/2015 - Krishna Mudragada               ##
##  Purpose:         Script to update dyn/admin properties using 'curl' ##
##########################################################################
#!/bin/bash
. /u01/aescripts/.env

INSTANCES_TO_RUN_ALL=${FLUSH_DIR}/instancesspreadout
INSTANCES_TO_RUN=instances_to_run.txt
echo -e "\nWhich JVMs do you want to make the change in?";
echo -e "1. All COMMERCE?";
echo -e "2. All CAP?";
echo -e "3. All CSR?";
echo -e "4. All Fulfillments?";
echo -e "5. All OrderStatuses?";
echo -e "6. All Services?";
echo -e "7. All";
echo -e "8. I have the instances of my choice already in instances_to_run.txt";
read JVMCHOICE

if [ $JVMCHOICE = "1" ] ; then
        > $INSTANCES_TO_RUN
        /bin/awk '/831/{ print $0 }' $INSTANCES_TO_RUN_ALL > $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "2" ] ; then
        > $INSTANCES_TO_RUN
        /bin/awk '/832/{ print $0 }' $INSTANCES_TO_RUN_ALL > $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "3" ] ; then
        > $INSTANCES_TO_RUN
        /bin/awk '/8340/{ print $0 }' $INSTANCES_TO_RUN_ALL > $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "4" ] ; then
        > $INSTANCES_TO_RUN
        /bin/awk '/8370/{ print $0 }' $INSTANCES_TO_RUN_ALL > $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "5" ] ; then
        > $INSTANCES_TO_RUN
        /bin/awk '/8372/{ print $0 }' $INSTANCES_TO_RUN_ALL > $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "6" ] ; then
        > $INSTANCES_TO_RUN
        /bin/awk '/8373/{ print $0 }' $INSTANCES_TO_RUN_ALL > $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "7" ] ; then
        /bin/cp $INSTANCES_TO_RUN_ALL $INSTANCES_TO_RUN
        /bin/cat $INSTANCES_TO_RUN
elif [ $JVMCHOICE = "8" ] ; then
        /bin/cat $INSTANCES_TO_RUN
else
        echo "ERROR:: You made a wrong choice. Try again."
        exit 0;
fi
echo "If you don't see what you wanted, quit NOW !! (use - Ctrl-C)";
FIRSTLINE=$(head -n 1 $INSTANCES_TO_RUN)
if [ -z FIRSTLINE ] ; then
        echo "ERROR:: Didn't read the file $FILENAME. Check the file";
        exit 0;
fi
echo -e "Enter username:";
read USERNAME

if [[ "$USERNAME" =~ [^a-zA-Z0-9] ]]; then
  echo "ERROR:: Invalid USERNAME. Make sure you enter an alphanumeric Username"
  exit 0
fi
echo -e "Enter password:";
read -s PASSWORD
echo -e "Enter relative path:[Ex: aeo/integration/transactionwireless/MobileConfiguration]";
read PATH
case "$PATH" in
*/)
    echo "ERROR:: Remove the slash in the end and try again."
    exit 0
    ;;
/*)
    echo "ERROR:: Remove the slash in the start and try again."
    exit 0
    ;;
esac
echo -e "\nWhat Action do you want to perform?";
echo -e "1. Invoke a Method";
echo -e "2. Change Property Value";
read CHOICE

if [ $CHOICE = "1" ] ; then
        ACTION="invokeMethod"
        echo -e "Enter Method Name:[Ex: forceScheduledTask]"
        read INVOKEMTHD
        if [[ "$INVOKEMETHOD" =~ [^a-zA-Z0-9] ]]; then
                echo "ERROR:: Invalid INVOKEMETHOD. Make sure you enter the INVOKEMETHOD name correct. "
                exit 0
        fi
        /bin/cat ~/bin/instances | while read LINE ; do
        OUT=`/usr/bin/curl -u $USERNAME:$PASSWORD http://$LINE/dyn/admin/nucleus/$PATH/?$ACTION=$INVOKEMTHD > /dev/null`
        done
elif [ $CHOICE = "2" ] ; then
        ACTION="propertyName"
        echo -e "Enter property Name:[Ex: URL]"
        read PROPERTYNAME
        if [[ "$PROPERTYNAME" =~ [^a-zA-Z0-9] ]]; then
                echo "ERROR:: Invalid PROPERTYNAME. Make sure you enter the PROPERTYNAME name correct. "
                exit 0
        fi
        echo -e "Enter Value:"
        read VALUE
        if [[ "$VALUE" =~ [^a-zA-Z0-9:/.-?=] ]]; then
                echo "ERROR:: Invalid VALUE. Make sure you enter the VALUE name correct. "
                exit 0
        fi
        /bin/cat ~/bin/instances | while read LINE ; do
        OUT=`/usr/bin/curl -u $USERNAME:$PASSWORD -d "newValue=$VALUE&change=Change Value" http://$LINE/dyn/admin/nucleus/$PATH/?$ACTION=$PROPERTYNAME > /dev/null`
        done
else
        echo "ERROR:: You didn't make the right choice. Try again.";
        exit 0;

fi
exit 0
