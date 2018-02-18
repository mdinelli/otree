from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Trust game tutorial
"""


class Constants(BaseConstants):
    name_in_url = 'trust_tutorial'
    players_per_group = 2
    num_rounds = 1

    M2 = random.randrange(2,5)


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            questions_possible_E1 =  random.randrange(5,15)
            questions_possible_E2 = random.randrange(5, 15)
            questions_possible_M = random.randrange(2, 5)
            questions_possible_G1 = random.randrange(1, 5)
            questions_possible_G2 = random.randrange(1, 5)

            if not 'question_numbers' in p.participant.vars:
                p.participant.vars['question_numbers']=[questions_possible_E1, questions_possible_E2, questions_possible_M, questions_possible_G1, questions_possible_G2]
           # M1 = random.randrange(2,5)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer1 = models.PositiveIntegerField(
        verbose_name='1.How much does P1 now have?',
        min=0, max=125)
    answer2 = models.PositiveIntegerField(
        verbose_name='2.How much does P2 now have?',
        min=0, max=125)
    answer3 = models.PositiveIntegerField(
        verbose_name='3.How much does P1 now have?',
        min=0, max=125)
    answer4 = models.PositiveIntegerField(
        verbose_name='4.How much does P2 now have?',
        min=0, max=125)
    # answer5 = models.PositiveIntegerField(
    #     verbose_name='5.How much does P1 now have?',
    #     min=0, max=125)
    # answer6 = models.PositiveIntegerField(
    #     verbose_name='6.How much does P2 now have?',
    #     min=0, max=125)
    my_error = models.IntegerField(initial=0)


