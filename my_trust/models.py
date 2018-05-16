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
    #change number of rounds to 6
    num_rounds = 6

    # endowment1 = c(10)
    # endowment2 = c(11)
    # send_increment = 1
    # Round = 1
    #
    # multiplication_factor = 3
    #
    #
    # send_choices = currency_range(0, endowment1, send_increment)




    # C = {'E1': 10, 'E2': 10, 'M': 2}
    # T1 = {'E1': 7, 'E2': 10, 'M': 5}
    # T2 = {'E1': 10, 'E2': 15, 'M': 1}
    # T3 = {'E1': 10, 'E2': 10, 'M': 5}
    # T4 = {'E1': 10, 'E2': 10, 'M': 1}

    C = {'E1': c(8), 'E2': c(12), 'M': 4}
    T1 = {'E1': c(8), 'E2': c(10), 'M': 5}
    T2 = {'E1': c(10), 'E2': c(12), 'M': 2}
    T3 = {'E1': c(8), 'E2': c(12), 'M': 5}
    T4 = {'E1': c(8), 'E2': c(12), 'M': 2}

    #want to multiply by 1.5
    # C = {'E1': c(12), 'E2': c(18), 'M': 4}
    # T1 = {'E1': c(12), 'E2': c(15), 'M': 5}
    # T2 = {'E1': c(12), 'E2': c(18), 'M': 2}
    # T3 = {'E1': c(12), 'E2': c(18), 'M': 5}
    # T4 = {'E1': c(12), 'E2': c(18), 'M': 2}

    Treatment_matrix = [C, T1, T2, T3, T4]


class Subsession(BaseSubsession):
   # def creating_session(self): self.group_randomly(fixed_id_in_group=True)

    def creating_session(self):


        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            for p in self.get_players():
#this needed an extra 0
                p.participant.vars['payoff_array']= [0, 0, 0, 0, 0, 0]

                #make three treatment arrays
                # treatment_array1 = [0, 1, 2, 3, 4]
                # treatment_array2 = [4, 3, 2, 1, 0]
                # treatment_array3 = [1, 0, 3, 4, 2]

                # modify the treatment arrays by adding a random round at the end:
                treatment_array1 = [0, 1, 2, 3, 4, random.randint(0, 4)]
                treatment_array2 = [4, 3, 2, 1, 0, random.randint(0, 4)]
                treatment_array3 = [1, 0, 3, 4, 2, random.randint(0, 4)]

                #random.shuffle(treatment_array)
                if not 'treatment_order' in p.participant.vars:
                    # if statement to distinguish among three possible treatments
                    r = random.randint(1,3)
                    if r ==1:
                        p.participant.vars['treatment_order'] = treatment_array1
                    if r == 2:
                        p.participant.vars['treatment_order'] = treatment_array2
                    else:
                        p.participant.vars['treatment_order'] = treatment_array3

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





class Group(BaseGroup):


    sent_back_amount = models.IntegerField()



   # the label and max value are dynamically generated in the views.py
    #sent_amount = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))

#We are replacing the sliders with text boxes

    sent_amount = models.IntegerField(min=0, max=100)

    # response_0 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_1 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_2 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_3 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_4 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_5 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_6 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_7 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_8 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_9 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_10 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_11 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_12 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_13 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_14 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))
    # response_15 = models.IntegerField(min=0, max=100, widget=widgets.Slider(attrs={'step': '1'}))

    response_0 = models.IntegerField(min=0, max=100)
    response_1 = models.IntegerField(min=0, max=100)
    response_2 = models.IntegerField(min=0, max=100)
    response_3 = models.IntegerField(min=0, max=100)
    response_4 = models.IntegerField(min=0, max=100)
    response_5 = models.IntegerField(min=0, max=100)
    response_6 = models.IntegerField(min=0, max=100)
    response_7 = models.IntegerField(min=0, max=100)
    response_8 = models.IntegerField(min=0, max=100)
    response_9 = models.IntegerField(min=0, max=100)
    response_10 = models.IntegerField(min=0, max=100)
    response_11 = models.IntegerField(min=0, max=100)
    response_12 = models.IntegerField(min=0, max=100)
    response_13 = models.IntegerField(min=0, max=100)
    response_14 = models.IntegerField(min=0, max=100)
    response_15 = models.IntegerField(min=0, max=100)


    def set_payoffs(self):

            p1 = self.get_player_by_id(1)
            p2 = self.get_player_by_id(2)

            self.sent_back_amount = getattr(self, 'response_{}'.format(
                int(self.sent_amount)))


            p1.participant.vars['temp_payoff'] = self.get_player_by_id(1).participant.vars['e1'] - self.sent_amount + self.sent_back_amount
            p2.participant.vars['temp_payoff'] = self.get_player_by_id(1).participant.vars['e2'] + self.sent_amount * self.get_player_by_id(1).participant.vars['m'] - self.sent_back_amount
            p1.participant.vars['payoff_array'][self.round_number-1] = p1.participant.vars['temp_payoff']
            p2.participant.vars['payoff_array'][self.round_number - 1] = p2.participant.vars['temp_payoff']
# we have to change this too:
            if self.round_number == 6:
                # we actually want to pick one round for everyone here
                a = [0,1,2,3,4,5]
                random.shuffle(a)
                b = a[0]


                #random.shuffle(p1.participant.vars['payoff_array'])
                #random.shuffle(p2.participant.vars['payoff_array'])

                p1.payoff = p1.participant.vars['payoff_array'][b]
                #p1.participant.vars['money'] = float(p1.payoff)*0.25
                p1.participant.vars['money'] = p1.payoff.to_real_world_currency(self.session)
                p2.payoff = p2.participant.vars['payoff_array'][b]
                p2.participant.vars['money'] = p2.payoff.to_real_world_currency(self.session)






class Player(BasePlayer):
    # I need data for endowments etc.
    e1 = models.IntegerField(initial=0)
    e2 = models.IntegerField(initial=0)
    m = models.IntegerField(initial=0)



