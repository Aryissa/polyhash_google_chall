from gift import Gift


class Game:
    def __init__(self, challenge):
        self.max_time = challenge['time']
        self.current_time = 0
        self.range = challenge['delivery_distance']
        self.nb_acceleration_ranges = challenge["acceleration_ranges"]
        self.nb_gifts = challenge["nb_gifts"]
        self.gifts = []
        for gift in challenge["gifts_list"]:
            self.gifts.append(Gift(
                gift['name'],
                gift['weight'],
                gift['x'],
                gift['y'],
                gift['score']
            ))
        self.acceleration_ranges = dict()
        for r in challenge['accelerations']:
            self.acceleration_ranges[r['weight_interval_to']] = r['max_acceleration']
