from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 5

    endowment1 = c(10)
    endowment2 = c(11)
    send_increment = 1
    Round = 1

    multiplication_factor = 3


    send_choices = currency_range(0, endowment1, send_increment)
    # C = {'E1': 10, 'E2': 10, 'M': 2}
    # T1 = {'E1': 7, 'E2': 10, 'M': 5}
    # T2 = {'E1': 10, 'E2': 15, 'M': 1}
    # T3 = {'E1': 10, 'E2': 10, 'M': 5}
    # T4 = {'E1': 10, 'E2': 10, 'M': 1}
    C = {'E1': 1, 'E2': 10, 'M': 2.5}
    T1 = {'E1': 2, 'E2': 10, 'M': 5.5}
    T2 = {'E1': 3, 'E2': 15, 'M': 1.5}
    T3 = {'E1': 4, 'E2': 10, 'M': 5.5}
    T4 = {'E1': 5, 'E2': 10, 'M': 1.5}

    Treatment_matrix = [C, T1, T2, T3, T4]


class Subsession(BaseSubsession):
   # def creating_session(self): self.group_randomly(fixed_id_in_group=True)

    def creating_session(self):

        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            for p in self.get_players():

                p.participant.vars['payoff_array']= [0, 0, 0, 0, 0]

                treatment_array = [0, 1, 2, 3, 4]
                random.shuffle(treatment_array)
                if not 'treatment_order' in p.participant.vars:
                    p.participant.vars['treatment_order'] = treatment_array
                    index=p.participant.vars['treatment_order'][0]
                    p.participant.vars['e1']=Constants.Treatment_matrix[index]['E1']
                    p.participant.vars['e2'] = Constants.Treatment_matrix[index]['E2']
                    p.participant.vars['m'] = Constants.Treatment_matrix[index]['M']
            for g in self.get_groups():
                par1=g.get_player_by_id(1).participant
                par2=g.get_player_by_id(2).participant
                par1.vars['e1']=par2.vars['e1']
                par1.vars['e2'] = par2.vars['e2']
                par1.vars['m'] = par2.vars['m']



# def question(amount):
#         return 'How much would you like to send back if Player 1 sends you {},'.format(c(amount))+\
#                ' with Player 1 keeping {}'.format(c(Constants.endowment1)-c(amount))+\
#                ' and leaving you with {}'.format(c(Constants.endowment2)+c(amount*Constants.multiplication_factor))
#
class Group(BaseGroup):
#
#     def Q(r, x):
#         return models.IntegerField(
#
#             min=0, max=Constants.Treatment_matrix[r - 1]['E1'],
#             widget=widgets.Slider(attrs={'step': '1'}),
#             verbose_name=question(x))
#
#

    sent_back_amount = models.FloatField()
    # sent_amount = Q(2,0)


   # the label and max value are dynamically generated in the views.py
    sent_amount = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))

    response_0 = models.FloatField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_1 = models.FloatField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_2 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_3 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_4 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_5 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_6 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_7 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_8 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_9 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_10 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_11 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_12 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_13 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_14 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    response_15 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))





    def set_payoffs(self):

            p1 = self.get_player_by_id(1)
            p2 = self.get_player_by_id(2)

            self.sent_back_amount = getattr(self, 'response_{}'.format(
                int(self.sent_amount)))


            p1.participant.vars['temp_payoff'] = self.get_player_by_id(1).participant.vars['e1'] - self.sent_amount + self.sent_back_amount
            p2.participant.vars['temp_payoff'] = self.get_player_by_id(1).participant.vars['e2'] + self.sent_amount * self.get_player_by_id(1).participant.vars['m'] - self.sent_back_amount
            p1.participant.vars['payoff_array'][self.round_number-1] = p1.participant.vars['temp_payoff']
            p2.participant.vars['payoff_array'][self.round_number - 1] = p2.participant.vars['temp_payoff']

            if self.round_number == 5:
                random.shuffle(p1.participant.vars['payoff_array'])
                random.shuffle(p2.participant.vars['payoff_array'])

                p1.payoff = p1.participant.vars['payoff_array'][0]
                p2.payoff = p2.participant.vars['payoff_array'][0]


            # p1.participant.vars['winnings array'][p1.round_number-1]= p1.payoff
            # p2.participant.vars['winnings array'][p2.round_number - 1] = p2.payoff




class Player(BasePlayer):
   pass

