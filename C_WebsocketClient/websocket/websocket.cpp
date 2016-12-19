#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "stdafx.h"
#include "websocket.h"

using namespace std;

int main()
{
	WSADATA data;
	WORD w = MAKEWORD(2, 2);
	WSAStartup(w, &data);

	char buff[1024] = {};
	wsContext_t *ctx = NULL;
	ctx = wsContextNew();
	wsCreateConnection(ctx, "ws://localhost:1234");
	
	int i = 10;
	while(i--)
	{
		char s[512] = {0};
		cin >> s;
		sendUtf8Data(ctx, s, strlen(s));
		int len = recvData(ctx, buff, 1024);
		if (len)
		{
			fprintf(stderr, "recv ok %d\n", len);
			printf("%s\r\n", buff);
		}

		if (len < 0)
		{
			break;
		}
	}
	
	wsContextFree(ctx);
	return 0;
}
