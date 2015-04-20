#include <arpa/inet.h>
#include <assert.h>
#include <errno.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <netdb.h>
#include <unistd.h>

#define SA      struct sockaddr
#define MAXLINE 4096
#define MAXSUB  300


#define LISTENQ         1024

extern int h_errno;


ssize_t process_http(int sockfd, char *host, char *page, char *poststr)
{
     char sendline[MAXLINE + 1], recvline[MAXLINE + 1];
    ssize_t n;
    printf("Longitud %lu\n", strlen(poststr));
    snprintf(sendline, MAXSUB,
             "POST %s HTTP/1.1\r\n"
             "Host: %s\r\n"
             "Connection: Close"
             "Content-type: application/x-www-form-urlencoded\r\n"
             "Content-length: %lu\r\n\r\n"
             "%s", page, host, strlen(poststr), poststr);

    write(sockfd, sendline, strlen(sendline));
    while ((n = read(sockfd, recvline, MAXLINE)) > 0) {
        recvline[n] = '\0';
        printf("%s", recvline);  // <-- this
    }
    return n;

}





int main(void)
{



    int sockfd;
    struct sockaddr_in servaddr;

    char **pptr;
    //********** You can change. Puy any values here *******
    char *hname = "telit.jspblm.com";
    char *page = "/telit-post-request/";
    //char *poststr = "a=1&b=2"; // a=A;C&b=B
    char *poststr = "a=10990&b=150408&c=115549&d=115554&e=59703751&f=0&g=0&h=3&i=0&j=>&k=8950203015001199331";
    //*******************************************************

    char str[50];
    struct hostent *hptr;
    if ((hptr = gethostbyname(hname)) == NULL) {
        fprintf(stderr, " Server down error for host: %s: %s",
                hname, hstrerror(h_errno));
        exit(1);
    }
    printf("hostname: %s \n", hptr->h_name);
    if (hptr->h_addrtype == AF_INET
        && (pptr = hptr->h_addr_list) != NULL) {
        printf("address: %s\n",
               inet_ntop(hptr->h_addrtype, *pptr, str,
                         sizeof(str)));
    } else {
        fprintf(stderr, "Error call inet_ntop \n");
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(80);
    inet_pton(AF_INET, str, &servaddr.sin_addr);

    connect(sockfd, (SA *) & servaddr, sizeof(servaddr));
    process_http(sockfd, hname, page, poststr);
    close(sockfd);
    printf("END\n");
    exit(0);


}