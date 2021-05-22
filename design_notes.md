# Parallelism

> How to maintain thread isolation? AKA - how each thread gets it's 'next file'

0) Use a threadpool, driver, and queue of files.
1) Use the driver to initialize threadpool & queue
1.1) Start with smaller queue sizes to test incrementally
2) Threads just read their assigned file from the queue

> How to make the threads more easily identifiable

https://stackoverflow.com/questions/34361035/python-thread-name-doesnt-show-up-on-ps-or-htop