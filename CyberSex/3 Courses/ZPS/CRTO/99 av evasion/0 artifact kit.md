
- working on artifact32
	- clean
	- big and stageless
- working on artifact64
	- clean
	- big and stageless
- all SVC clean
	- big and stageless

















Before Arti64.exe

```
void start(HINSTANCE mhandle) {
   /* switched from snprintf... as some A/V product was flagging based on the function *sigh* 
      92, 92, 46, 92, 112, 105, 112, 101, 92 is \\.\pipe\
   
   */
   sprintf(pipename, "%c%c%c%c%c%c%c%c%cmicrosvc\\%d", 92, 92, 46, 92, 112, 105, 112, 101, 92, (int)(GetTickCount() % 9898));

   /* start our server and our client */
```

after Arti64.exe

```
void start(HINSTANCE mhandle) {
   /* switched from snprintf... as some A/V product was flagging based on the function *sigh* 
      92, 92, 46, 92, 112, 105, 112, 101, 92 is \\.\pipe\
   
   */
   sprintf(pipename, "%c%c%c%c%c%c%c%c%cnetwork\\monC", 92, 92, 46, 92, 112, 105, 112, 101, 92);


```

