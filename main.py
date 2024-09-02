def get_int_value(prompt, min_value=None, max_value=None, value_list=None):
    getting_value = True

    while getting_value:
        getting_integer = True
        while getting_integer:
            if min_value:
                print(f'Min value: {min_value}')
            if max_value:
                print(f'Max value: {max_value}')
            if value_list:
                print(f'Value list: {value_list}')

            value_entered = input(f'{prompt}: ')
            try:
                possible_value = int(value_entered)
                getting_integer = False

            except ValueError:
                getting_integer = True

        if min_value and possible_value < min_value:
            print('Too low')
            getting_value = True
        elif max_value and possible_value > max_value:
            print('Too high')
            getting_value = True
        elif value_list and possible_value not in value_list:
            print('Not in list')
            getting_value = True
        else:
            print('Accepted')
            getting_value = False
        return possible_value

def get_yes_or_no(prompt):
    print(prompt)

    getting_response = True

    while getting_response:
        response = input('Yes or No: ')

        if response.lower() == 'yes' or response.lower() == 'no':
            getting_response = False

    return response.lower() == 'yes'


def get_num_players():
    return get_int_value('How many players', min_value=1)


def get_course_num_holes():
    return get_int_value('How many holes', value_list=[9, 18])


def get_course_par(num_holes):
    return get_int_value('What is the par for this course', min_value=num_holes)


def get_game_players(num_players):
    player_names = []

    for i in range(num_players):
        player_names.append(input(f'Player {i+1} name: '))

    return player_names


def game_initialise_scores(player_names, course_num_holes):
    scores = {}

    for player in player_names:
        scores[player] = [0 for i in range(course_num_holes)]

    return scores


def display_status(
        num_players,
        player_names,
        course_num_holes,
        course_par
):
    print(f'{num_players} players with names {player_names}\n'
          f'{course_num_holes} holes with par {course_par}'
          )

def get_strokes_for_round(player, round_number, scores):
    getting_score = True
    while getting_score:
        first_score = get_int_value(f'Enter score for {player} in round {round_number + 1}: ', min_value=1)
        second_score = get_int_value(f'Enter score again for {player} in round {round_number + 1}: ', min_value=1)

        if first_score == second_score:
            getting_score = False
            score_for_round = first_score

    scores[player][round_number] = score_for_round


def summary_required(player, round_number):
    return get_yes_or_no(f'Round {round_number + 1} summary for {player}? ')



def show_summary(player, round_number, scores):
    print(f'{player} total up to round {round_number + 1}: {sum(scores[player][:round_number + 1])}')


def play_game(num_players, player_names, course_num_holes, course_par, scores):
    for round_num in range(course_num_holes):
        for player in player_names:
            get_strokes_for_round(player, round_num, scores)
            if summary_required(player, round_num):
                show_summary(player, round_num, scores)




def end_of_round_summary(num_players, player_names, course_num_holes, course_par, scores):
    for player in player_names:
        player_total = sum(scores[player])

        player_scores = ", ".join(str(n) for n in scores[player])

        if player_total < course_par:
            message = f'{course_par - player_total} below par'
        elif player_total > course_par:
            message = f'{player_total - course_par} above par'
        else:
            message = 'par'

        print(f'{player} scores {player_scores} with total {player_total}, {message}')






game_num_players = get_num_players()
game_course_num_holes = get_course_num_holes()
game_course_par = get_course_par(game_course_num_holes)
game_player_names = get_game_players(game_num_players)
game_scores = game_initialise_scores(game_player_names, game_course_num_holes)


display_status(
    game_num_players,
    game_player_names,
    game_course_num_holes,
    game_course_par
    )


play_game(
    game_num_players,
    game_player_names,
    game_course_num_holes,
    game_course_par,
    game_scores
)


end_of_round_summary(
    game_num_players,
    game_player_names,
    game_course_num_holes,
    game_course_par,
    game_scores
)

