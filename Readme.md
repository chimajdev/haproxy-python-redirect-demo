To see it quickly in action you need docker and docker-compose installed.  

Clone the repository and start it with docker-compose up.  

Open http://127.0.0.1:8000/?url=params&you=want&to=test in your browser and test it.

If url path starts with /lua/ then you can test the equivalent lua service inside haproxy. 
Check http://127.0.0.1:8000/lua/?a=1 for example.

fromLua=true query param gets added when lua worker sends the redirect. 

Delay is 3 seconds in both workers right now.
