# how to run and setup websocket backend implementation locally
1.install python higher than 3.7
2.install the 'websocket' library
3. pip install websockets
## Create a websocket server
1.Create a new folder in vs code name is 'websocket_server.py' in desktop to folder 
2.implement the websocket server in the path of the specific folder
3. handling messsage 'echo_with_delay' send the message back with 0.1 - second delay
4. 'reverse_message' reverse the message
5. count_last_char' counts courrance of the last character in the message(excluding the last character)
6. 'websocket_handler' handles the given meassage to the server
7. Websocket server to the python websocket_ser.py(to name of the server ) run the server in vs code
###  Create a websocket server
1.Create  a new file in websocket common folder ‘test_client.py’
2.using the split terminal option to run the server to client ‘python test_client.py’
3.server URL:'ws://localhost:8765'
#### Request format
1.message a plain text format
##### response format
1.Type: Type of response (echo, reversed, count_last_char).
2.Message: The actual message or the reversed message.
3.Count: Count of occurrences of the last character (if applicable).
###### echo with delay
1.{"type": "echo", "message": "The quick brown fox jumped over the lazy dog o"}
####### Reversed message
1.{"type": "reversed", "message": "o yzal eht revo depmuj xof nworb kciuq ehT"}
######## Count of last character
1.{"type": "count_last_char", "count": 4}





