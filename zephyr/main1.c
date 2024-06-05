#include <zephyr.h>
#include <kernel.h>

#define MY_STACK_SIZE 500
#define MY_PRIORITY 10

extern void my_entry_point(int p1, void *p2, void *p3)
{
	long long i = 0;
	printk("thread #%d entry point\n", p1);
	while (i <= 1000000)
	{
    	if (i % 100000 == 0)
    	{
        	printk("%lld\n", i);
    	}
    	i++;
	}
	return;
};

K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);
struct k_thread my_thread_data;

K_THREAD_STACK_DEFINE(my_stack_area2, MY_STACK_SIZE);
struct k_thread my_thread_data2;

void main(void)
{
	k_tid_t my_tid = k_thread_create(&my_thread_data, my_stack_area,
                                 	K_THREAD_STACK_SIZEOF(my_stack_area),
                                 	my_entry_point,
                                 	1, NULL, NULL,
                                 	MY_PRIORITY, 0, K_MSEC(10000));

	printk(
    	"Created thread 1 with priority %d\n",
    	k_thread_priority_get(my_tid));
	k_thread_priority_set(my_tid, MY_PRIORITY / 2);
	printk("Thread 1 priority changed to %d\n", k_thread_priority_get(my_tid));
	k_tid_t my_tid2 = k_thread_create(&my_thread_data2, my_stack_area2,
                                  	K_THREAD_STACK_SIZEOF(my_stack_area2),
                                  	my_entry_point,
                                  	2, NULL, NULL,
                                  	MY_PRIORITY, 0, K_NO_WAIT);

	printk(
    	"Created thread 2 with priority %d\n",
    	k_thread_priority_get(my_tid2));
	k_thread_start(my_tid2);
	printk("Thread 2 started\n");
	k_thread_start(my_tid);
	printk("Thread 1 started\n");
}
