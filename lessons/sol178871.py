def solution(players, callings):
    rank_dict = {rank+1:player for rank, player in enumerate(players)}
    player_dict = {player:rank+1 for rank, player in enumerate(players)}
    for overtake_name in callings:
        origin_rank = player_dict[overtake_name]
        overtaken_name = rank_dict[origin_rank-1]
        player_dict[overtake_name], player_dict[overtaken_name] = origin_rank-1, origin_rank
        rank_dict[origin_rank], rank_dict[origin_rank-1] = overtaken_name, overtake_name
    return [name for _, name in rank_dict.items()]