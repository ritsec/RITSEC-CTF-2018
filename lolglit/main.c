#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>

int sanitize(char *in){
    unsigned int len = strlen(in);
    for(int i = 0; i < len; i++){
        if(in[i] == ';' || in[i] == '`' || in[i] == '\n' || in[i] == '$' || in[i] == '|' || in[i] == '(' || in[i] == ')' || in[i] == '&'){
            in[i] = ' ';
        }
    }
}


int main(int argc, char **argv){
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    char buf[32];
    char buf_dup[32];


    while(fgets(buf, 32, stdin)){
    }
    strncpy(buf_dup, buf, 32); 
    sanitize(buf);
    char command[64];
//    sprintf(command, "echo %s &>/dev/null || echo %s | figlet | lolcat  && echo %s | figlet | lolcat ", buf, buf_dup, buf);
    sprintf(command, "echo %s", buf);
    int ret = system(command);
    printf("ret: %d\n", ret);
    if (ret != 0){
        sprintf(command, "echo %s | figlet | lolcat", buf_dup);
    }else {
        sprintf(command, "echo %s | figlet | lolcat", buf);
    }
    ret = system(command);



}

