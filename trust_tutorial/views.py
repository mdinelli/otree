from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Directions(Page):
    pass

class Practice(Page):
    form_model = models.Player
    form_fields = ['answer1',
                   'answer2',
                   'answer3',
                   'answer4',
                   # 'answer5',
                   # 'answer6'
                    ]

    def error_message(self, values):
        error_string= ''
        # if values["answer1"] !=self.player.participant.vars['question_numbers'][0]- self.player.participant.vars['question_numbers'][3]:
        #     self.player.my_error = self.player.my_error + 1
        #     error_string = error_string + 'Your answer to question 1 was incorrect. '
        #
        # if values["answer2"] != self.player.participant.vars['question_numbers'][1]+\
        #         self.player.participant.vars['question_numbers'][2]*self.player.participant.vars['question_numbers'][3]:
        #     self.player.my_error = self.player.my_error + 1
        #     error_string = error_string + 'Your answer to question 2 was incorrect. '
        #
        #
        # if values["answer3"] != self.player.participant.vars['question_numbers'][0]- self.player.participant.vars['question_numbers'][3]\
        #         +self.player.participant.vars['question_numbers'][4]:
        #     self.player.my_error = self.player.my_error + 1
        #     error_string = error_string + 'Your answer to question 3 was incorrect. '
        #
        # if values["answer4"] != self.player.participant.vars['question_numbers'][1]+\
        #         self.player.participant.vars['question_numbers'][2]*self.player.participant.vars['question_numbers'][3]\
        #         -self.player.participant.vars['question_numbers'][4]:
        #     self.player.my_error = self.player.my_error + 1
        #     error_string = error_string + 'Your answer to question 4 was incorrect. '


        if values["answer1"] !=6:
            self.player.my_error = self.player.my_error + 1
            error_string = error_string + 'Your answer to question 1 was incorrect. '

        if values["answer2"] !=21:
            self.player.my_error = self.player.my_error + 1
            error_string = error_string + 'Your answer to question 2 was incorrect. '


        if values["answer3"] != 10:
            self.player.my_error = self.player.my_error + 1
            error_string = error_string + 'Your answer to question 3 was incorrect. '

        if values["answer4"] != 17:
            self.player.my_error = self.player.my_error + 1
            error_string = error_string + 'Your answer to question 4 was incorrect. '



        # if values["answer5"] != 13:
        #     self.player.my_error = self.player.my_error + 1
        #     error_string = error_string + 'Your answer to question 5 was incorrect. '
        #
        # if values["answer6"] != 32:
        #     self.player.my_error = self.player.my_error + 1
        #     error_string = error_string + 'Your answer to question 6 was incorrect. '

        if error_string != '':
            return error_string + ' \n Try again!'






class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Practice,
    ResultsWaitPage,
    Results
]
