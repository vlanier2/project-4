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

def test_example_one_200km_brevet():
    """
    Tests a 200km brevet with controls at
    60km 120km 175km and 205km finish.
    This is example one from 
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    control_locations = [60, 120, 175, 205]
    times = acp_times.get_times_from_list(
        control_locations, 
        200, 
        arrow.get('2000-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss'))

    truth_open = {
        60  : arrow.get('2000-01-01 01:46:00', 'YYYY-MM-DD HH:mm:ss'),
        120 : arrow.get('2000-01-01 03:32:00', 'YYYY-MM-DD HH:mm:ss'),
        175 : arrow.get('2000-01-01 05:09:00', 'YYYY-MM-DD HH:mm:ss'),
        205 : arrow.get('2000-01-01 05:53:00', 'YYYY-MM-DD HH:mm:ss')
    }

    truth_close = {
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

# test for edges of locations, 200, 400, 600
# solution - 
