#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
int var =0;

// int x=1000;


// void setFive() {
//     x = 5;
// }
//
// void* function (void* arg){
//     printf("fils %ld : début\n", pthread_self()) ;
//     sleep(1) ;
//     var=10 ;
//     printf ("fils %ld : modification de var=%d\n", pthread_self(), var) ;
//     sleep(10);
//     printf("fils %ld : fin\n", pthread_self()) ;
//     return NULL ;
// }
//
//
// int main(){
//
//     printf("%d\n",x);
//     setFive();
//     printf("%d\n",x);
//
//     pthread_t tid;
//     printf("père %ld : début (var=%d)\n", pthread_self(), var);
//     pthread_create(&tid, NULL, function, NULL) ;
//     printf ("père %ld : creation de thread %ld\n", pthread_self(), tid);
//     sleep(5) ;
//     printf("père %ld : fin (var= %d)\n", pthread_self(), var);
//     return 0 ;
// }

// prhtred_create vs fork ; leger vs lourd
// thread have shared var if their global
// fork are not you have to configure it



#include <pthread.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>
void *fonc (void *arg){
    int nbsec = (int)arg;
    printf("je suis un thread et j'attends %d secondes\n", nbsec);
    sleep(nbsec);
    puts("je suis un thread et je me termine");
    pthread_exit(NULL); /* termine le thread proprement*/
}
int main(void)
{
    int ret;
    pthread_t tid ;
    int nbsec;
    time_t t1;
    srand(time(NULL));
    t1=time(NULL);
    nbsec= rand()%10; /* on attend entre 0 et 9 secondes*/
    /* on crée le thread*/