# General purpose function to ask user to enter integer

def get_int_value(prompt, min_value=None, max_value=None, value_list=None):
    getting_value = True

    while getting_value:
        getting_integer = True

        prompt_list = []

        while getting_integer:
            if min_value:
                prompt_list.append(f'Min: {min_value}')
            if max_value:
                prompt_list.append(f'Max: {max_value}')
            if value_list:
                prompt_list.append(f'Values: {', '.join(str(v) for v in value_list)}')

            value_entered = input(f'{prompt} ({', '.join(prompt_list)}): ')

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
            getting_value = False
    return possible_value


# General purpose function to get user choice of "yes" or "no"

def get_yes_or_no(prompt):
    print(prompt)

    getting_response = True

    while getting_response:
        response = input('Yes or No: ')

        if response.lower() == 'yes' or response.lower() == 'no':
            getting_response = False

    return response.lower() == 'yes'


# Get number of players from user

def get_num_players():
    return get_int_value('How many players', min_value=1)


# Get number of holes from user

def get_course_num_holes():
    return get_int_value('How many holes', value_list=[9, 18])


# Get par from user

def get_course_par(num_holes):
    return get_int_value('What is the par for this course', min_value=num_holes)


# Get number of players

def get_game_players(num_players):
    player_names = []

    for i in range(num_players):
        player_names.append(input(f'Player {i + 1} name: '))

    return player_names


# Function to create a scorecard

def game_initialise_scorecard(player_names, course_num_holes):
    scores = {}

    for player in player_names:
        scores[player] = [0 for i in range(course_num_holes)]

    return scores


# Function to display game status

def display_status(
        num_players,
        player_names,
        course_num_holes,
        course_par
):
    print(f'{num_players} players with names {', '.join(player_names)}\n'
          f'{course_num_holes} holes with par {course_par}'
          )


# Function to get scores for current round (with a check)

def get_strokes_for_round(player, round_number, scores):
    getting_score = True
    while getting_score:
        first_score = get_int_value(
            f'Enter score for {player} in round {round_number + 1}',
            min_value=1
        )
        second_score = get_int_value(
            f'Enter score again for {player} in round {round_number + 1}',
            min_value=1
        )

        if first_score == second_score:
            getting_score = False
            score_for_round = first_score
        else:
            print('Scores don\'t match. Try again.')

    scores[player][round_number] = score_for_round


# Ask if the user would like a summary for the current player

def summary_required(player, round_number):
    return get_yes_or_no(f'Round {round_number + 1} summary for {player}? ')


# Show a summary for the current player

def show_summary(player, round_number, scores):
    print(f'{player} total up to round {round_number + 1}: {sum(scores[player][:round_number + 1])}')


# Routine to run a game loop

def play_game(num_players, player_names, course_num_holes, course_par, scores):
    for round_num in range(course_num_holes):
        for player in player_names:
            get_strokes_for_round(player, round_num, scores)
            if summary_required(player, round_num):
                show_summary(player, round_num, scores)


# Summary of scores at the end of the game


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


# Run the game if called directly

if __name__ == "__main__":
    
    # Collect required info
    
    game_num_players = get_num_players()
    game_course_num_holes = get_course_num_holes()
    game_course_par = get_course_par(game_course_num_holes)
    game_player_names = get_game_players(game_num_players)
    game_scorecard = game_initialise_scorecard(game_player_names, game_course_num_holes)

    # Summarise

    display_status(
        game_num_players,
        game_player_names,
        game_course_num_holes,
        game_course_par
    )

    # Run game loop

    play_game(
        game_num_players,
        game_player_names,
        game_course_num_holes,
        game_course_par,
        game_scorecard
    )
    
    # Summarise at the end of the game

    end_of_round_summary(
        game_num_players,
        game_player_names,
        game_course_num_holes,
        game_course_par,
        game_scorecard
    )
