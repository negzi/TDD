-module(poker_hands_tests).
-include_lib("eunit/include/eunit.hrl").


parse_player_and_get_name_test() ->
    Player = "Black: 2H 3D 5S 9C KD",
    Res = poker_hands:parse(Player),
    ?assertEqual(["Black", "2H 3D 5S 9C KD"], Res).


parse_player_hand_non_high_value_test() ->
    Hand = "2H 3D 5S 9C 4D",
    Res = poker_hands:parse_hand(Hand),
    ?assertEqual([[2, 3, 5, 9, 4], 
		  ["H", "D", "S", "C", "D"]], Res).

parse_player_hand_high_value_test() ->
    Hand = "TH JD QS KC AD",
    Res = poker_hands:parse_hand(Hand),
    ?assertEqual([[10, 11, 12, 13, 14], 
		  ["H", "D", "S", "C", "D"]], Res).

players_hands_high_card_rank_test() ->
    Values = [10, 11, 12, 13, 14], 
    Res = poker_hands:is_high_card(Values),
    ?assertEqual({true, 14}, Res).

players_hands_high_card_false_test() ->
    Values = [10, 11, 12, 12, 14], 
    Res = poker_hands:is_high_card(Values),
    ?assertEqual(false, Res).

players_hands_pair_rank_test() ->
    Values = [10, 10, 12, 13, 14], 
    Res = poker_hands:is_pair(Values),
    ?assertEqual({true, 10}, Res).

players_hands_pair_rank_false_test() ->
    Values = [10, 11, 12, 13, 14], 
    Res = poker_hands:is_pair(Values),
    ?assertEqual(false, Res).

players_hands_two_pair_rank_second_pair_is_highest_test() ->
    Values = [10, 10, 12, 12, 14],
    Res = poker_hands:is_two_pair(Values),
    ?assertEqual({true, 12}, Res).

players_hands_two_pair_returns_false_if_three_of_kind_test() ->
    Values = [10, 10, 10, 12, 14],
    Res = poker_hands:is_two_pair(Values),
    ?assertEqual(false, Res).

players_hands_two_pair_first_pair_higher_test() ->
    Values = [12, 12, 10, 10, 14],
    Res = poker_hands:is_two_pair(Values),
    ?assertEqual({true, 12}, Res).

players_hands_three_of_a_kind_1_test() ->
    Values = [12, 12, 12, 10, 14],
    Res = poker_hands:is_three_of_a_kind(Values),
    ?assertEqual({true, 12}, Res).

players_hands_three_of_a_kind_2_test() ->
    Values = [10, 12, 12, 10, 12],
    Res = poker_hands:is_three_of_a_kind(Values),
    ?assertEqual(false, Res).

players_hands_three_of_a_kind_false_test() ->
    Values = [10, 11, 12, 10, 12],
    Res = poker_hands:is_three_of_a_kind(Values),
    ?assertEqual(false, Res).

players_hands_four_of_a_kind_test() ->
    Values = [12, 11, 12, 12, 12],
    Res = poker_hands:is_four_of_a_kind(Values),
    ?assertEqual({true,12}, Res).

players_hands_not_four_of_a_kind_test() ->
    Values = [12, 11, 11, 12, 12],
    Res = poker_hands:is_four_of_a_kind(Values),
    ?assertEqual(false, Res).

players_hands_full_house_1_test() ->
    Values = [12, 11, 11, 12, 12],
    Res = poker_hands:is_full_house(Values),
    ?assertEqual({true,12}, Res).

players_hands_full_house_2_test() ->
    Values = [10, 11, 11, 10, 10],
    Res = poker_hands:is_full_house(Values),
    ?assertEqual({true,10}, Res).

players_hands_full_house_false_test() ->
    Values = [10, 11, 11, 10, 13],
    Res = poker_hands:is_full_house(Values),
    ?assertEqual(false, Res).

players_hands_straight_test() ->
    Values = [9, 10, 11, 12, 13],
    Res = poker_hands:is_straight(Values),
    ?assertEqual({true,13}, Res).

players_hands_straight_false_test() ->
    Values = [9, 10, 11, 12, 2],
    Res = poker_hands:is_straight(Values),
    ?assertEqual(false, Res).

count_number_of_occurance_when_there_is_one_pair_test() ->
    Values = [12, 11, 13, 12, 9],
    Res = poker_hands:count_number_of_occurance(Values),
    ?assertEqual([{12,2}],Res).

count_number_of_occurance_when_one_pair_and_tiple_test() ->
    Values = [12, 12, 11, 12, 11],
    Res = poker_hands:count_number_of_occurance(Values),
    ?assertEqual([{11,2}, {12, 3}],Res).

rank_high_card_test() ->
    Values = [3, 9, 11, 12, 10],
    Suites = ["H", "D", "S", "C", "D"],
    Res = poker_hands:rank_hand(Values, Suites),
    ?assertEqual({high_card, 12},Res).
