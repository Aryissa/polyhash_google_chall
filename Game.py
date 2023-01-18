from Gift import Gift


class Game:
    """
    Classe Jeu
    Initialise la partie
    """

    def __init__(self, challenge):
        self.max_time = int(challenge['time'])
        self.current_time = 0
        self.range = int(challenge['delivery_distance'])
        self.nb_acceleration_ranges = challenge["acceleration_ranges"]
        self.nb_gifts = int(challenge["nb_gifts"])
        self.gifts = []
        for gift in challenge["gifts_list"]:
            self.gifts.append(Gift(
                gift['name'],
                int(gift['weight']),
                int(gift['x']),
                int(gift['y']),
                int(gift['score']),
                float(gift['ratio'])
            ))
        self.acceleration_ranges = dict()
        for r in challenge['accelerations']:
            self.acceleration_ranges[int(r['weight_interval_to'])] = int(r['max_acceleration'])

    def __str__(self):
        s = ''
        s += f'Temps imparti : {self.max_time}\n'
        s += f'Nombre de cadeaux : {self.nb_gifts}\n'
        score_max = sum([g.score for g in self.gifts])
        s += f'Score max : {score_max}\n'
        return s
