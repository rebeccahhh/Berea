-module(chat).
% module should be named the same as the name of the file.
-compile(export_all).
% export all of the functions inside the module. 

modify(Username, Message, Dictionary) ->
	% the modify function takes in a username, Message, and Dictionary and returns
	% the updated dictionary with the message for the user
	case  lists:keymember(Username, 1, Dictionary) of
		%in the case that the username is in the dictionary 
		true ->
			%first define the new value by setting the element of the tuple to the message
			%that is specified. It will overwrite existing messages currently.
			NewVal = setelement(2, lists:keyfind(Username, 1, Dictionary), [Message]),
			
			%we then replace the entire value with the New one
			lists:keyreplace(Username, 1, Dictionary, NewVal);
		false ->
		
			%if false then state that the username doesn't exist
			'Username does not exist!'
	end.

get_message(Username, Dictionary) ->
	%this function is no longer used but we used it for testing how to return messages for a user
	case lists:keymember(Username, 1, Dictionary) of
		true -> 
			%if the user is in the dictionary return the message if there is one
			element(2, lists:keyfind(Username, 1, Dictionary));
		false ->
			'Username does not exist!'
	end.
 
inbox(Dictionary) ->
	receive
		{From, {send, Username, Message}} ->
			case  lists:keymember(Username, 1, Dictionary) of
				%in the case that the username is in the dictionary 
				true ->
					From ! {self(), ok},
					%first define the new value by setting the element of the tuple to the message
					%that is specified. It will overwrite existing messages currently.
					NewVal = setelement(2, lists:keyfind(Username, 1, Dictionary), [Message]),
					
					%we then replace the entire value with the New one
					inbox(lists:keyreplace(Username, 1, Dictionary, NewVal));
				false ->
				
					%if false then state that the username doesn't exist
					From ! {self(), 'Username does not exist!'},
					inbox(Dictionary)
			end;
			
		{From, {check, Username}} ->
			case lists:keymember(Username, 1, Dictionary) of
				true ->
					From ! {self(), element(2, lists:keyfind(Username, 1, Dictionary))},
					From ! {self(), 'you have no messages'};		
				false ->
					From ! {self(), 'Username does not exist'},
					inbox(Dictionary)
			end;
		terminate ->
			ok
	end.

send(Pid, Username, Message) ->
	Pid ! {self(), {send, Username, Message}},
	receive
		{Pid, Msg} -> Msg
	end.
	 
check(Pid, Username) ->
	Pid ! {self(), {check, Username}},
	receive
		{Pid, Msg} -> Msg
	end.

create_dict(UsernameList, Dictionary) ->
	% This takes in the usernames and an empty list and 
	% creates key, value tuples for each username 
	%it follows the racket recursion pattern 
	
	%first define what Empty is
	Empty = [],
	
	%check to see if the username list is empty
	case UsernameList == Empty of
		true ->
			%if it is just return the dictionary that was passed to it
			Dictionary;
		false ->
			%if it is not empty then define first and rest of the Username list
			[First |Rest] = UsernameList,
			
			% and cons the first key, pair onto the Dictionary (List passed in)
			Updated_dict = [{First, []}| Dictionary],
			% and make your recursive call to the function to update the dictionary
			create_dict(Rest, Updated_dict)
	end.

start(UsernameList) ->
	% We need to take the usernames and create a dictionary making them the keys
	Dict = create_dict(UsernameList, []),
	
	%spawn creates a process for us using the module we are in, calling the inbox server with the arguments of the list of users
	spawn(?MODULE, inbox, [Dict]).
