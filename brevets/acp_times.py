"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

BREVETS_SPEED_TABLE = {
   200  : {'minimum' : 15, 'maximum' : 34},
   400  : {'minimum' : 15, 'maximum' : 32},
   600  : {'minimum' : 15, 'maximum' : 30},
   1000 : {'minimum' : 11.428, 'maximum' : 28},
   1300 : {'minimum' : 13.333, 'maximum' : 26}
}

HARDCODED_TIME_LIMITS = {
   200  : "13:30",
   300  : "20:00",
   400  : "27:00",
   600  : "40:00",
   1000 : "75:00"
}

def get_speed(control_location_km, maximum_or_minimum):
   """
   Get the speed associated with the given control location
   in kilometers - Specifying maximum or minimum speed.
   """
   for control_cutoff in BREVETS_SPEED_TABLE:
      if control_location_km <= control_cutoff:
         return BREVETS_SPEED_TABLE[control_cutoff][maximum_or_minimum]
   return False

def minimum_speed(control_location_km):
   """
   Get the minimum speed for the given control location
   """
   return get_speed(control_location_km, 'minimum')

def maximum_speed(control_location_km):
   """
   Get the maximum speed for the given control location
   """
   return get_speed(control_location_km, 'maximum')

def get_time_pair(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   returns a dictionary with both the opening and closing time for the
   given control distance. Times are arrow datetime objects.
   return format:
   {
      'open_time'  : <time>
      'close_time' : <time>
   }
   """
   return {
      'open_time'  : open_time(control_dist_km, brevet_dist_km, brevet_start_time),
      'close_time' : close_time(control_dist_km, brevet_dist_km, brevet_start_time)
      }

def get_times_from_list(control_dists_km, brevet_dist_km, brevet_start_time):
   """
   returns a dictionary containing all starting and ending times from the given
   list of control distances. Function assumes control distances are in increasing
   order.
   return format:
   {
      <dist1> : 
      {
         'open_time'  : <time>
         'close_time' : <time>
      },

      <dist2> :
      {
         'open_time'  : <time>
         'close_time' : <time>
      }
   }
   """
   start_times_dict = dict()
   for control_dist_km in control_dists_km:
      start_times_dict[control_dist_km] = get_time_pair(control_dist_km,
                                          brevet_dist_km, brevet_start_time)
   return start_times_dict

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now()

if __name__ == "__main__":
   tests = [200, 10, 400, 540, 650, 1000, 1202]
   for e in tests:
      print('test for', e)
      print('minimum', minimum_speed(e))
      print('maximum', maximum_speed(e))