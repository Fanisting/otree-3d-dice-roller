from otree.api import *



doc = """
This app is a 3d dice roller, and the dice outcome is generated as variable "dice_number" inside Python. 

1. Before instruction page, the dice outcome is determined as "dice_number";
2. At roll_dice page, the 3d dice simulation would ensure the outcome is "dice_number";
3. Finally, the Results page would present the "dice_number". 

Tip: the js package for 3d-dice roller is dice-box-threejs
"""

class C(BaseConstants):
    NAME_IN_URL = 'dice_roller'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dice_number = models.IntegerField(min=1, max=6)
    chosen = models.BooleanField(label="Have you already chosen a side?",
                                choices=[[1, True], [0, False]],
                                widget=widgets.RadioSelectHorizontal
                                    )
    mind_side = models.BooleanField(label="Please report the chosen side in your mind",
                                choices=[[1, 'UP'], [0, 'DOWN']],
                                widget=widgets.RadioSelectHorizontal
                                    )

# PAGES
class instruction(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # pre-determine the dice outcome randomly
        import random
        random_integer = random.randint(1, 6)
        player.dice_number = random_integer
    
class roll_dice(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(dice_number = player.dice_number)
        
class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        dice_number = player.dice_number
        return dict(dice_number = dice_number)


page_sequence = [instruction, roll_dice, Results]
