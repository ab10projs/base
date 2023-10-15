// ConsoleApplication1.cpp : main project file.

#include "stdafx.h"
#include "hiredis.h"


using namespace System;

typedef struct timeval {
	long tv_sec;    /* seconds */
	long tv_usec;   /* microseconds */
}timeval;

int main(array<System::String ^> ^args)
{
    Console::WriteLine(L"Hello World");

	unsigned int j, isunix = 0;
	redisContext *c;
	redisReply *reply;
	const char *hostname =  "127.0.0.1";
	int port =  6379;
	



	struct timeval timeout = { 1, 500000 }; // 1.5 seconds
	c = redisConnectWithTimeout(hostname, port, timeout);

	

	/* PING server */
	reply = (redisReply *)redisCommand(c, "PING");
	printf("PING: %s\n", reply->str);
	freeReplyObject(reply);

	/* Set a key */
	reply = (redisReply *)redisCommand(c, "SET %s %s", "foo", "hello world");
	printf("SET: %s\n", reply->str);
	freeReplyObject(reply);

	/* Set a key using binary safe API */
	reply = (redisReply *)redisCommand(c, "SET %b %b", "bar", (size_t)3, "hello", (size_t)5);
	printf("SET (binary API): %s\n", reply->str);
	freeReplyObject(reply);

	/* Try a GET and two INCR */
	reply = (redisReply *)redisCommand(c, "GET foo");
	printf("GET foo: %s\n", reply->str);
	freeReplyObject(reply);

	reply = (redisReply *)redisCommand(c, "INCR counter");
	printf("INCR counter: %lld\n", reply->integer);
	freeReplyObject(reply);
	/* again ... */
	reply = (redisReply *)redisCommand(c, "INCR counter");
	printf("INCR counter: %lld\n", reply->integer);
	freeReplyObject(reply);

	/* Create a list of numbers, from 0 to 9 */
	reply = (redisReply *)redisCommand(c, "DEL mylist");
	freeReplyObject(reply);
	for (j = 0; j < 10; j++) {
		char buf[64];

		//snprintf(buf, 64, "%u", j);
		reply = (redisReply *)redisCommand(c, "LPUSH mylist element-%s", buf);
		freeReplyObject(reply);
	}

	/* Let's check what we have inside the list */
	reply = (redisReply *)redisCommand(c, "LRANGE mylist 0 -1");
	if (reply->type == REDIS_REPLY_ARRAY) {
		for (j = 0; j < reply->elements; j++) {
			printf("%u) %s\n", j, reply->element[j]->str);
		}
	}
	freeReplyObject(reply);

	/* See function for an example of redisCommandArgv */
	

	/* Disconnects and frees the context */
	redisFree(c);

	Console::WriteLine("Done");


    return 0;
}
