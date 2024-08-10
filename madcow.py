bench_5rm = 100
squat_5rm = 120
pullup_5rm = 100
deadlift_5rm = 140


def lb_plate_round(x, smallest_unit =2.5):
  # Adding smallest_unit/2 wil middle round it
  x = int((x+smallest_unit/2)/smallest_unit) * smallest_unit
  return x

def _5rm_to_1rm(x):
  return 10/9*x

def lb_to_kg(x):
  return x*.454

def kg_to_lb(x):
  return x*1/.454

def kg_lb_number_str(kg):
  return "("+str(kg)+"KG/"+str(int(kg_to_lb(kg)))+"LB)"

def kg_to_str_barbell(x):
  x = (x-20)/2
  plates = int((x)/20)
  remainder = (x - 20*plates)
  remainder = lb_plate_round(kg_to_lb(remainder))
  
  if remainder>0:
    remainder_str = str(remainder)
  else:
    remainder_str = "0"
  return "--"+plates*"I"+"("+remainder_str+")-"
  

def kg_to_str_pullup(x, bodyweight_kg=86):
  x = (x-bodyweight_kg)
  plates = int((x)/20)
  remainder = (x - 20*plates)
  remainder = lb_plate_round(kg_to_lb(remainder))
  
  if remainder>0:
    remainder_str = str(remainder)
  else:
    remainder_str = "0"
  return "\-"+plates*"I"+"("+remainder_str+")-/"


  
def madcow_workout_print(name, _5rm, weight_strfunc, goals=[]):
  print("\n========================================")
  print(name)
  print("========================================\n")
  
  _1rm = _5rm_to_1rm(_5rm)
  sets = [ int(i/10 * _1rm) for i in [5,6,7,8,9,10]]
  
  for i,s in enumerate(sets):
    if i+1<6:
      setstr = "set"+str(i+1)
    else:
      setstr = "setx"
    
    print(setstr, kg_lb_number_str(s), weight_strfunc(s), )
  print()
  for i,g in enumerate(goals):
    print("5rm_goal"+str(i+1), kg_lb_number_str(g), weight_strfunc(g))
    
    
madcow_workout_print(
  name="Bench",
  _5rm=bench_5rm,
  weight_strfunc=kg_to_str_barbell,
  goals=[120])
  
madcow_workout_print(
  name="Squat",
  _5rm=squat_5rm,
  weight_strfunc=kg_to_str_barbell,
  goals=[140, 160])
  
madcow_workout_print(
  name="Pullup",
  _5rm=pullup_5rm,
  weight_strfunc=kg_to_str_pullup,
  goals=[120])

madcow_workout_print(
  name="Deadlift",
  _5rm=deadlift_5rm,
  weight_strfunc=kg_to_str_barbell,
  goals=[160,180])
