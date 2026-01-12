import math

def initialize():
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global star_activity, star_time
    global bored_with_stars
    global last_activity_end_time
    global last_star_time1, last_star_time2

    cur_hedons = 0
    cur_health = 0
    cur_time = 0

    last_activity = None
    last_activity_duration = 0

    star_activity = None
    star_time = None
    bored_with_stars = False

    last_activity_end_time = None
    last_star_time1 = None
    last_star_time2 = None


def get_cur_hedons():
    return cur_hedons


def get_cur_health():
    return cur_health


def is_tired():
    global last_activity_end_time, cur_time
    if last_activity_end_time is None:
        return False
    return cur_time - last_activity_end_time < 120


def star_can_be_taken(activity):
    global star_time, cur_time, bored_with_stars, star_activity
    if (not bored_with_stars and
            star_activity == activity and
            star_time == cur_time): return True
    return False


def offer_star(activity):
    global star_activity, star_time, bored_with_stars, cur_time, last_star_time1, last_star_time2

    star_activity = activity
    star_time = cur_time

    if not bored_with_stars and last_star_time2 is not None and (cur_time - last_star_time2) < 120:
        bored_with_stars = True

    last_star_time2 = last_star_time1
    last_star_time1 = cur_time


def estimate_hedons_delta(activity, duration):
    if not (activity in ["running", "textbooks", "resting"]):
        return 0

    tired = is_tired()
    star_taken = star_can_be_taken(activity)
    hedons = 0

    if activity == "resting":
        return 0

    if tired:
        if star_taken:
            star_bonus = min(duration, 10)
            hedons += star_bonus
            hedons += (duration - star_bonus) * -2
        else:
            hedons += duration * -2
    else:
        if activity == "running":
            first_ten = min(duration, 10)
            rest = duration - first_ten
            hedons += first_ten * 2 + rest * -2
        else:
            first_twenty = min(duration, 20)
            rest = duration - first_twenty
            hedons += first_twenty - rest

        if star_taken:
            star_bonus = min(duration, 10)
            hedons += star_bonus * 3

    return hedons


def estimate_health_delta(activity, duration):
    if activity == "running":
        if last_activity == "running":
            prev_running = last_activity_duration
        else:
            prev_running = 0

        remainder = max(0, 180 - prev_running)
        three = min(remainder, duration)
        one = duration - three
        return three * 3 + one

    elif activity == "textbooks":
        return duration * 2
    else:
        return 0


def perform_activity(activity, duration):
    global cur_health, cur_hedons, cur_time, last_activity, last_activity_duration, star_activity, star_time, last_activity_end_time

    if activity not in ["running", "textbooks", "resting"]:
        return

    cur_hedons += estimate_hedons_delta(activity, duration)
    cur_health += estimate_health_delta(activity, duration)

    star_activity = None
    star_time =  None

    cur_time += duration
    if last_activity == activity:
        last_activity_duration += duration
    else:
        last_activity = activity
        last_activity_duration = duration

    if activity in ["running", "textbooks"]:
        last_activity_end_time = cur_time


def most_fun_activity_minute():
    activities = ["textbooks","running", "resting",]
    max_activity = None
    max_hedons = -math.inf
    for activity in activities:
        hedons = estimate_hedons_delta(activity, 1)
        if hedons > max_hedons:
            max_hedons = hedons
            max_activity = activity
    return max_activity

################################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
