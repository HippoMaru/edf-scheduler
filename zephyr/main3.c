#include <zephyr.h>
#include <kernel.h>


#define MY_STACK_SIZE 500
#define MY_PRIORITY 10


extern void my_entry_point(int p1, int p2, void* p3){
   long long i = 0;
   printk("thread #%d entry point\n", p1);
   while (i <= 10000*p2)
   {
       if (i % 10000 == 0)
       {
           printk("%lld\n", i);
       }
       i++;
   }
   printk("thread #%d finished at %ld\n", p1, k_uptime_get());
   // times[*time_i] = k_uptime_get_32();
   // if (*time_i == TASKS){
   //     printk("TOTAL TIME: %d", times[TASKS] - times[0]);
   // }
   // *time_i = *time_i + 1;
   return;
};


K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);
struct k_thread my_thread_data;


K_THREAD_STACK_DEFINE(my_stack_area2, MY_STACK_SIZE);
struct k_thread my_thread_data2;


K_THREAD_STACK_DEFINE(my_stack_area3, MY_STACK_SIZE);
struct k_thread my_thread_data3;


K_THREAD_STACK_DEFINE(my_stack_area4, MY_STACK_SIZE);
struct k_thread my_thread_data4;


K_THREAD_STACK_DEFINE(my_stack_area5, MY_STACK_SIZE);
struct k_thread my_thread_data5;


void main(void)
{
   // int times[TASKS + 1] = {0};
   // int time_i = 1;
   k_tid_t my_tid = k_thread_create(&my_thread_data, my_stack_area,
                                    K_THREAD_STACK_SIZEOF(my_stack_area),
                                    my_entry_point,
                                    1, 7, NULL,
                                    MY_PRIORITY, 0, K_MSEC(2000));


   printk(
       "Created thread 1 with priority %d\n",
       k_thread_priority_get(my_tid));
   k_tid_t my_tid2 = k_thread_create(&my_thread_data2, my_stack_area2,
                                     K_THREAD_STACK_SIZEOF(my_stack_area2),
                                     my_entry_point,
                                     2, 6, NULL,
                                     MY_PRIORITY, 0, K_NO_WAIT);


   printk(
       "Created thread 2 with priority %d\n",
       k_thread_priority_get(my_tid2));
  
   k_tid_t my_tid3 = k_thread_create(&my_thread_data3, my_stack_area3,
                                     K_THREAD_STACK_SIZEOF(my_stack_area3),
                                     my_entry_point,
                                     3, 3, NULL,
                                     MY_PRIORITY, 0, K_NO_WAIT);


   printk(
       "Created thread 3 with priority %d\n",
       k_thread_priority_get(my_tid3));
  
   k_tid_t my_tid4 = k_thread_create(&my_thread_data4, my_stack_area4,
                                     K_THREAD_STACK_SIZEOF(my_stack_area4),
                                     my_entry_point,
                                     4, 2, NULL,
                                     MY_PRIORITY, 0, K_MSEC(200000));


   printk(
       "Created thread 4 with priority %d\n",
       k_thread_priority_get(my_tid4));
  
   k_tid_t my_tid5 = k_thread_create(&my_thread_data5, my_stack_area5,
                                     K_THREAD_STACK_SIZEOF(my_stack_area5),
                                     my_entry_point,
                                     5, 10, NULL,
                                     MY_PRIORITY, 0, K_MSEC(100000));


   printk(
       "Created thread 5 with priority %d\n",
       k_thread_priority_get(my_tid5));
   k_thread_deadline_set(my_tid, 100000);
   printk("Thread 1 deadline set to 100000\n");
   k_thread_deadline_set(my_tid2, 200000);
   printk("Thread 2 deadline set to 200000\n");
   k_thread_deadline_set(my_tid3, 300000);
   printk("Thread 3 deadline set to 300000\n");
   k_thread_deadline_set(my_tid4, 400000);
   printk("Thread 4 deadline set to 400000\n");
   k_thread_deadline_set(my_tid5, 500000);
   printk("Thread 5 deadline set to 500000\n");


   k_thread_start(my_tid);
   printk("Thread 1 started\n");
   k_thread_start(my_tid2);
   printk("Thread 2 started\n");
   k_thread_start(my_tid3);
   printk("Thread 3 started\n");
   k_thread_start(my_tid4);
   printk("Thread 4 started\n");
   k_thread_start(my_tid5);
   printk("Thread 5 started\n");
   printk("Start time: %d\n", k_uptime_get_32());
}
