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
    num_rounds = 1

    endowment1 = c(10)
    endowment2 = c(10)
    multiplication_factor = 3

    offer_increment = c(1)

    offer_choices = currency_range(0, endowment1, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment1 - offer))




    doc = """ offer_increment = c(1)  " \
          offer_choices = currency_range(0, endowment1, offer_increment)" \
          offer_choices_count = len(offer_choices) " \
          def question(amount):" \
          return 'Would you accept an offer of {}?'.format(c(amount))"
    response_0 = models.BooleanField(
       widget=widgets.RadioSelectHorizontal(), verbose_name=question(0))
    response_1 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(1))
    response_2 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(2))
    response_3 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(3))
    response_4 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(4))
    response_5 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(5))
    response_6 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(6))
    response_7 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(7))
    response_8 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(8))
    response_9 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(9))
    response_10 = models.BooleanField(
        widget=widgets.RadioSelectHorizontal(), verbose_name=question(10))"""


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        for g in self.get_groups():
            if 'treatment' in self.session.config:
                g.use_strategy_method = self.session.config['use_strategy_method']
            else:
                g.use_strategy_method = random.choice([True, False])


def question(amount):
        return 'Would you accept an offer of {}?'.format(c(amount))


class Group(BaseGroup):
    use_strategy_method = models.BooleanField(
        doc="""Whether this group uses strategy method"""
    )

    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )


response_0 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(0))
response_1 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(1))
response_2 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(2))
response_3 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(3))
response_4 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(4))
response_5 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(5))
response_6 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(6))
response_7 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(7))
response_8 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(8))
response_9 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(9))
response_10 = models.BooleanField(
    widget=widgets.RadioSelectHorizontal(), verbose_name=question(10))

sent_amount = models.CurrencyField()
sent_back_amount = models.CurrencyField()

sent_amount = models.CurrencyField(
        choices=currency_range(0, Constants.endowment1, c(1)),
    )

def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment1 - self.sent_amount + self.sent_back_amount
        p2.payoff = Constants.endowment2 + self.sent_amount * Constants.multiplication_factor - self.sent_back_amount

class Player(BasePlayer):
    pass

