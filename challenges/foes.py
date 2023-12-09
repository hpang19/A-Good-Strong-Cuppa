"""
This module includes all features related to the challenges.
"""

from challenges import FOE_MAP, RATS_WEAPONS, MATH_QUESTIONS, PYTHON_QUESTIONS
from board import LOCATION_PREFIX
from random import choice
import sys
sys.path.append('..')
from GUI import prompts
from levels import ASCII_ART, KO_ART


def get_foe(current_room_description: list) -> str:
    """
    Get the foe based on the current room description.

    :param current_room_description: a list
    :precondition: current_room_description is a list consist of three elements [level, room, item]
    :postcondition: get the foe with corresponding level and location
    :return: a string representing the foe

    >>> current_room_description = [1, 'Kitchen', "Nothing"]
    >>> get_foe(current_room_description)
    'rats'

    >>> current_room_description = [2, 'Grocery Store', "Nothing"]
    >>> get_foe(current_room_description)
    'dogs'
    """
    foe = FOE_MAP[current_room_description[1]]
    level = current_room_description[0]
    foe = foe[level-1] if current_room_description[1] == 'Street' else foe
    return foe


def check_for_foes(current_room_description: list) -> bool:
    """
    Check for the presence of foes in the current room by matching two random choices.

    :param current_room_description: a list
    :precondition: current_room_description is a list consist of three elements [level, room, item]
    :postcondition: check if foe exist by matching two random choices and return the result in boolean
    :return: a boolean indicating if there are foes present
    """
    foe = get_foe(current_room_description)
    if foe == 'rats':
        return choice(range(4)) == choice(range(4))
    elif foe == 'dogs':
        return choice(range(3)) == choice(range(3))
    elif foe == 'kids':
        return choice(range(3)) == choice(range(3))
    else:
        return True


def rats_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> bool:
    """
    Engage in a challenge against rats in a specific location.

    This function will print the message to ask player to kill the rats. When expected input is received,
    it will return True.

    :param location: a string indicating the location of the challenge
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: return True after expected input is received, otherwise keep looping in the while loop
    :return: True
    """
    prompts.print_message(f'There is a rat {LOCATION_PREFIX[location]} {location.lower()}.\n', text_area_object)
    message = 'To proceed, you need to kill the rats. Please select a weapon to kill the rats from the list:\n'
    challenge_question = '[1]: Air Gun  [2]: Pesticides  [3] Hot Water '
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(message + '\n' + challenge_question + end, rats_callback, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        int(input('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))


def rats_callback(answer, character, text_area_object=None, button_frame=None):
    if answer in ('1', '2', '3'):
        weapon_id = int(answer)
        message = RATS_WEAPONS[weapon_id] + '\n'
        prompts.print_message(message, text_area_object)
        if weapon_id != 1:
            penalty(1, character, 10, text_area_object)
    else:
        prompts.print_message("Why don't you pick from the list, Chris?\n", text_area_object)
        penalty(1, character, 10, text_area_object)


def dogs_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> bool:
    """
    Engage in a challenge against dogs in a specific location.

    This function will print the message to ask player to choose a direction to dodge the dog attack. Function will
    return True if the dodge direction is opposite of dog attack direction, and False otherwise.

    :param location: a string indicating the location of the challenge
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: return True if the dodge direction is opposite of dog attack direction, and False otherwise
    :return: a boolean
    """
    message = f'There is a dog {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    msg = 'Now the dog is trying to attack, you need to decide whether to dodge left or right. Please make a choice:\n'
    challenge_question = 'You decide to dodge [1]: left  [2]: right '
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(msg + '\n' + challenge_question + end, dogs_callback, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        int(input(challenge_question))


def dogs_callback(answer, character, text_area_object=None, button_frame=None):
    if answer in ('1', '2'):
        dodge = ["left", "right"][int(answer) - 1]
        dog_choice = choice(['1', '2'])
        msg = f'You are dodging {dodge.upper()} and dog attacked {["left", "right"][int(dog_choice) - 1].upper()}\n'
        prompts.print_message(msg, text_area_object)
        if answer != dog_choice:
            penalty(None, character, 20, text_area_object)
        else:
            prompts.print_message('Yay! It missed you.\n', text_area_object)
    else:
        prompts.print_message("Why don't you pick from the list, Chris?\n", text_area_object)
        penalty(None, character, 20, text_area_object)


def kids_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> bool:
    """
    Engage in a challenge against kids in a specific location.

    This function will print the message to ask player to answer a math question. Function will return True if the
    answer is correct, and False otherwise.

    :param location: a string indicating the location of the challenge
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: return True if the answer is correct, and False otherwise
    :return: a boolean
    """
    message = f'There are kids running {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    message = 'You called school and the teacher comes. The teacher is challenging you with a Math question:\n'
    challenge_question = choice(list(MATH_QUESTIONS.keys()))
    challenge_answer = MATH_QUESTIONS[challenge_question]
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(f'{message}\n{challenge_question} {end}', kids_callback,
                                      challenge_answer=challenge_answer, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        input(f'{challenge_question} ')
    
    
def kids_callback(answer, challenge_answer, character, text_area_object=None, button_frame=None):
    if answer == challenge_answer:
        prompts.print_message('Great! That is correct answer!\n', text_area_object)
    else:
        penalty(challenge_answer, character, 50, text_area_object)


def boss_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> None:
    """
    Engage in a challenge against the boss character at a specific location.

    :param location: A string indicating the location of the challenge
    :param character: A dictionary representing the game character
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: caffeine level in the character will be dropped everytime the player answer a question wrong
    """
    students = ['Joey', 'Hsin']
    message = f'There are {students[0]} and {students[1]} {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    prompts.print_message('Final exam is approaching, they have a lot of questions to ask you.\n', text_area_object)
    challenge_question = choice(list(PYTHON_QUESTIONS.keys()))
    challenge_answer = PYTHON_QUESTIONS[challenge_question]
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(f'{choice(students)} has a question:\n\n{challenge_question} {end}',
                                      boss_callback, challenge_answer=challenge_answer, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        your_answer = input(f'{challenge_question} ').upper()
        boss_callback(your_answer, challenge_answer, character)


def boss_callback(answer, challenge_answer, character, text_area_object=None, button_frame=None):
    if challenge_answer == answer:
        character['kill_final_boss'] = True
        message = ASCII_ART + '\n\n' + 'Congratulations, Chris! You defeated Joey and Hsin!'
        prompts.print_message(message, text_area_object)
    else:
        penalty(challenge_answer, character, 500, text_area_object)


def penalty(answer, character, loss_caffeine, text_area_object):
    if answer:
        prompts.print_message(f'[X] The answer should be {answer}.\n', text_area_object)
    character['caffeine'] -= loss_caffeine
    message = f'Your caffeine just dropped {loss_caffeine}. Your current caffeine level is {max(character["caffeine"], 0)}\n'
    prompts.print_message(message, text_area_object)
    if character['caffeine'] <= 0:
        message = KO_ART + '\n\n' + "You have run out of your caffeine! :'(\n"
        prompts.print_message(message, text_area_object)


def fight_with_foe(current_room: list, character: dict, frame=None, text_area_object=None, button_frame=None):
    """
    Fight with a foe and calculate caffeine level based on fight result.

    :param current_room: a list representing the current room's description
    :param character: a dictionary representing the game character
    :precondition: current_room is a list consist of three elements [level, room, item]
    :precondition: character is a dictionary where "caffeine" exists as a key
    """
    foe = get_foe(current_room)
    if foe == 'rats':
        rats_challenge(current_room[1], character, frame, text_area_object, button_frame)
    elif foe == 'dogs':
        dogs_challenge(current_room[1], character, frame, text_area_object, button_frame)
    elif foe == 'kids':
        kids_challenge(current_room[1], character, frame, text_area_object, button_frame)
    else:
        boss_challenge(current_room[1], character, frame, text_area_object, None)
