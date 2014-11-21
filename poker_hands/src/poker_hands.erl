-module(poker_hands).
-compile(export_all).

parse(Player) ->
    [Name, Hand] = string:tokens(Player, ":"),
    [Name ,string:strip(Hand)].

parse_hand(Hand) ->
    Cards = string:tokens(Hand, " "),
    Values = [ map([V]) || [V,_] <- Cards ],
    Suites = [ [S] || [_,S] <- Cards ],
    [Values,Suites].

map("T") ->
    10;
map("J") ->
    11;
map("Q") ->
    12;
map("K") ->
    13;
map("A") ->
    14;
map(X) ->
    list_to_integer(X).

rank_hand(Values,_) ->
    
    case  count_number_of_occurance(Values) of
	[] ->
	    {high_card, lists:max(Values)}
    end.

is_high_card(Values) ->    
    case count_number_of_occurance(Values) of
	[] ->
	    {true, lists:max(Values)};
	_ ->
	    false
    end.
		
is_pair(Values) ->
    is_rank(Values, 2).

is_two_pair(Values) ->
    case count_number_of_occurance(Values) of 
	[{_,2},{V,2}] ->
	    {true, V};
	_ ->
	    false
    end.

is_three_of_a_kind(Values) ->
    is_rank(Values, 3).

is_four_of_a_kind(Values) -> 
    is_rank(Values, 4).

is_full_house(Values) -> 
    case count_number_of_occurance(Values) of 
	[_,{V,3}] ->
	    {true, V};
	[{V,3},_] ->
	    {true, V};
	_ ->
	    false
    end.

is_straight(Values) ->
    Sorted = lists:sort(Values),
    
    case is_sequential(Sorted) of 
	true -> 
	    {true, lists:max(Values)};
	false ->
	    false
    end.

is_sequential([_]) ->
    true;
is_sequential([H,S|Rest]) when S-H == 1 ->
    is_sequential([S|Rest]);
is_sequential(_) ->
    false.
    
is_rank(Values, Occurances) ->
    case count_number_of_occurance(Values) of 
	[{V, Occurances}] ->
	    {true, V};
	_ ->
	    false
    end.	   

count_number_of_occurance(Values) ->
    Results = [count_number_of_occurance([X|Values--[X]],  1)
	       || X <- Values],
    SortedList = lists:usort(Results),
    FilterOnesOcured = fun({_, Y}) ->  Y =/= 1 end,
    lists:filter(FilterOnesOcured, SortedList).

count_number_of_occurance([V], Counter) ->
    {V,Counter};
count_number_of_occurance([V|Values], Counter) ->
    case lists:member(V, Values) of
	true ->
	    Remaining = Values -- [V],
	    count_number_of_occurance([V|Remaining], Counter+1);
	false ->
	    count_number_of_occurance([V],Counter)
    end.




     
