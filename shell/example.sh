#!/usr/bin/env bash

# add this line to import the dialog api
source "./dialog.sh"

aa=$(TITLE='select your docker image source from the list:';
     TITLE_SHORT='docker image source';
     OPTIONS=(0 "docker.oa"
              1 "Tencent Cloud"
              2 "official Dockerhub")
     DEFAULT_OPTION=0;
     ui.show_options)

bb=$(TITLE='use random port?';
     TITLE_SHORT='port config';
     ui.show_yesno)

cc=$(TITLE='what is the name of your server';
     TITLE_SHORT='name of the server';
     ui.show_input)

dd=$(TITLE='this is just a message to inform user, information collected';
     TITLE_SHORT='short message';
     ui.show_msgbox)

printf "1. you choose $aa\n"
printf "2. you choose $bb\n"
printf "3. you choose $cc\n"
printf "4. you choose $dd\n"
