"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import acp_times
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
log = logging.getLogger(__name__)

#####
# TEST OF SIMPLE BREVET ACROSS ONLY ONE SPEED BRACKET
# NO ODDITIES PRESENT
#####

def test_example_one_200km_brevet():
    """
    Tests a 200km brevet with controls at
    60km 120km 175km and 205km finish.
    This is example one from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [0, 60, 120, 175, 205]
    times = acp_times.get_times_from_list(
        control_locations, 
        200, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0   : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        60  : arrow.get('2000-01-01 01:46:00', 'YYYY-MM-DD HH:mm:ss'),
        120 : arrow.get('2000-01-01 03:32:00', 'YYYY-MM-DD HH:mm:ss'),
        175 : arrow.get('2000-01-01 05:09:00', 'YYYY-MM-DD HH:mm:ss'),
        205 : arrow.get('2000-01-01 05:53:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0   : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        60  : arrow.get('2000-01-01 04:00:00', 'YYYY-MM-DD HH:mm:ss'),
        120 : arrow.get('2000-01-01 08:00:00', 'YYYY-MM-DD HH:mm:ss'),
        175 : arrow.get('2000-01-01 11:40:00', 'YYYY-MM-DD HH:mm:ss'),
        205 : arrow.get('2000-01-01 13:30:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])

#####
# TEST OF LONGER BREVET ACROSS MULTIPLE SPEED BRACKETS
# NO ODDITIES PRESENT
#####

def test_example_two_600km_brevet():
    """
    Tests a 600km brevet with controls every 50km
    and 609km finish.
    This is example two from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [0, 100, 200, 350, 550, 609]

    times = acp_times.get_times_from_list(
        control_locations, 
        600, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        0   : arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'),
        100 : arrow.get('2000-01-01 02:56:00', 'YYYY-MM-DD HH:mm:ss'),
        200 : arrow.get('2000-01-01 05:53:00', 'YYYY-MM-DD HH:mm:ss'),
        350 : arrow.get('2000-01-01 10:34:00', 'YYYY-MM-DD HH:mm:ss'),
        550 : arrow.get('2000-01-01 17:08:00', 'YYYY-MM-DD HH:mm:ss'),
        609 : arrow.get('2000-01-01 18:48:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
        0   : arrow.get('2000-01-01 01:00:00', 'YYYY-MM-DD HH:mm:ss'),
        100 : arrow.get('2000-01-01 06:40:00', 'YYYY-MM-DD HH:mm:ss'),
        200 : arrow.get('2000-01-01 13:20:00', 'YYYY-MM-DD HH:mm:ss'),
        350 : arrow.get('2000-01-01 23:20:00', 'YYYY-MM-DD HH:mm:ss'),
        550 : arrow.get('2000-01-02 12:40:00', 'YYYY-MM-DD HH:mm:ss'),
        609 : arrow.get('2000-01-02 16:00:00', 'YYYY-MM-DD HH:mm:ss')
    }

    for control in times:
        log.debug(f"test for {control}")
        log.debug(f"{times[control]['open_time']} == {truth_open[control]}")
        assert(times[control]['open_time'] == truth_open[control])
        log.debug(f"{times[control]['close_time']} == {truth_close[control]}")
        assert(times[control]['close_time'] == truth_close[control])


#####
# TEST OF ODDITY - CLOSE TO START CONTROL POINTS
# PAGES CLAIMS CODE UPDATED TO INCLUDE FRENCH TIME RELAXATION
#####
