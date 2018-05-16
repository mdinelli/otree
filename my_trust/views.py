from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
class Instructions(WaitPage):
    # TODO - We probably only need to get these values for player 2 in the group


    def after_all_players_arrive(self):
        for p in self.group.get_players():
            index = p.participant.vars['treatment_order'][self.round_number - 1]
            p.participant.vars['e1'] = Constants.Treatment_matrix[index]['E1']
            p.e1 = Constants.Treatment_matrix[index]['E1']
            p.participant.vars['e2'] = Constants.Treatment_matrix[index]['E2']
            p.e2 = Constants.Treatment_matrix[index]['E2']
            p.participant.vars['m'] = Constants.Treatment_matrix[index]['M']
            p.m = Constants.Treatment_matrix[index]['M']

        play1 = self.group.get_player_by_id(1)
        play2 = self.group.get_player_by_id(2)
        par1 = self.group.get_player_by_id(1).participant
        par2 = self.group.get_player_by_id(2).participant
        par1.vars['e1'] = par2.vars['e1']
        play1.e1 = play2.e1
        par1.vars['e2'] = par2.vars['e2']
        play1.e2 = play2.e2
        par1.vars['m'] = par2.vars['m']
        play1.m = play2.m


class Send(Page):
    form_model = models.Group
    def get_form_fields(self):
        if self.player.id_in_group == 1:
            return ['sent_amount']
        else:
            return ['response_{}'.format(int(i)) for i in range(0,1 + int(self.participant.vars['e1']))]

    def question(self, amount):
        endow1_less_amount = self.participant.vars['e1'] - amount
        endow2_plus_multiplied_amount = int(self.participant.vars['e2'] + (self.participant.vars['m'] * amount))

        return 'P1 sends you {}. '.format(c(amount)) +  'You have {}'.format(c(endow2_plus_multiplied_amount))
              # ' with Player 1 keeping {}'.format(c(endow1_less_amount)) + \


    # TODO - FINISH THIS LIST AFTER TESTING
    def vars_for_template(self):
        return {
            'number_of_fields': self.participant.vars['e1'] + 1,
            'response_00_label': self.question(0),
            'response_01_label': self.question(1),
            'response_02_label': self.question(2),
            'response_03_label': self.question(3),
            'response_04_label': self.question(4),
            'response_05_label': self.question(5),
            'response_06_label': self.question(6),
            'response_07_label': self.question(7),
            'response_08_label': self.question(8),
            'response_09_label': self.question(9),
            'response_10_label': self.question(10),
            'response_11_label': self.question(11),
            'response_12_label': self.question(12),
            'response_13_label': self.question(13),
            'response_14_label': self.question(14),
            'response_15_label': self.question(15),
        }



# TODO - Determine the max values for Player 1
    def sent_amount_max(self):
        return self.participant.vars['e1']

    # TODO - Determine the max values for each response
    # Helper function that does the math
    def determine_max_for_gift_amount(self, amount):
        return self.participant.vars['e2'] + (self.participant.vars['m'] * amount)

    # These functions determine the max amount for each resopnse field
    def response_0_max(self):
        return self.determine_max_for_gift_amount(0)

    def response_1_max(self):
        return self.determine_max_for_gift_amount(1)

    def response_2_max(self):
        return self.determine_max_for_gift_amount(2)

    def response_3_max(self):
        return self.determine_max_for_gift_amount(3)

    def response_4_max(self):
        return self.determine_max_for_gift_amount(4)

    def response_5_max(self):
        return self.determine_max_for_gift_amount(5)

    def response_6_max(self):
        return self.determine_max_for_gift_amount(6)

    def response_7_max(self):
        return self.determine_max_for_gift_amount(7)

    def response_8_max(self):
        return self.determine_max_for_gift_amount(8)

    def response_9_max(self):
        return self.determine_max_for_gift_amount(9)

    def response_10_max(self):
        return self.determine_max_for_gift_amount(10)

    def response_11_max(self):
        return self.determine_max_for_gift_amount(11)

    def response_12_max(self):
        return self.determine_max_for_gift_amount(12)

    def response_13_max(self):
        return self.determine_max_for_gift_amount(13)

    def response_14_max(self):
        return self.determine_max_for_gift_amount(14)

    def response_15_max(self):
        return self.determine_max_for_gift_amount(15)









class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    def vars_for_template(self):
        return {
            'npled_amount':  self.group.sent_amount*self.player.participant.vars['m']

        }





page_sequence = [
    Instructions,
    Send,
    ResultsWaitPage,
    Results,
]
