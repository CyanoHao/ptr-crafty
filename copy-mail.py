#!/usr/bin/python3

import sys
import time

import pyautogui
import yaml


def click(xy: dict, sleep: float = .5):
    x, y = xy['x'], xy['y']
    pyautogui.moveTo(x, y, duration=.2)
    pyautogui.click()
    if sleep:
        time.sleep(sleep)


def write_str(s: str):
    pyautogui.write(s, interval=.05)
    time.sleep(.1)


def press(key, sleep=.1):
    pyautogui.press(key)
    time.sleep(sleep)


with open(sys.argv[1], 'rb') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    glue = config['glue']
    world = config['world']

time.sleep(3)

i = 0
while True:
    click(glue['xy_copy_character'])
    if glue['change_region']:
        click(glue['xy_select_region_dropdown'])
        click(glue['xy_select_region_my_region'],
              sleep=glue['switch_region_latency'])
    for _ in range(1, glue['character_page']):
        click(glue['xy_page_down'])
    click(glue['xy_my_character_in_copy_list'])
    click(glue['xy_do_copy'])
    click(glue['xy_do_copy_confirm'], sleep=glue['copy_character_latency'])

    click(glue['xy_my_character'])
    if glue['change_name']:
        click(glue['xy_enter_world'])
        write_str(glue['new_name'])
        click(glue['xy_change_name_confirm'], sleep=glue['enter_world_latency'])
    else:
        click(glue['xy_enter_world'], sleep=glue['enter_world_latency'])

    click(world['xy_mailbox'])
    click(world['xy_send_mail_tab'])

    for action in world['send_action']:
        write_str(action['to'])
        press('enter')  # auto complete
        press('esc')
        if 'gold' in action:
            click(world['xy_gold_input'])
            write_str(str(action['gold']))
            press('esc')
        if type(action['macro']) == str:
            press('enter')
            write_str(action['macro'])
            press('enter', sleep=world['macro_execution_latency'])
        else:
            for m in action['macro']:
                press('enter')
                write_str(m)
                press('enter', sleep=world['macro_execution_latency'])
        click(world['xy_send_button'], sleep=world['send_mail_latency'])

    click(world['xy_game_menu'])
    click(world['xy_log_out'], sleep=world['log_out_latency'])

    click(glue['xy_delete_character'])
    write_str('delete')
    click(glue['xy_confirm_deletion'], sleep=glue['delete_character_latency'])

    i += 1
    print(i)
    sys.stdout.flush()
