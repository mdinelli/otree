from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['age',
                   'gender',
                   'other_g',
                   'Latinx_ethnicity',
                   # 'checkbox1',
                   # 'checkbox2',
                   # 'checkbox3',
                   'race',
                   'other_r',
                   'education',
                   'income',
                   ]

    def error_message(self, values):
        error_string = ''
        if values["age"] == '':
            self.player.my_error_s = self.player.my_error_s + 1
            if self.player.my_error_s == 0:
                return 'Please tell us your age.'






class Personality(Page):
    form_model = models.Player
    form_fields = ['q1',
                   'q2',
                   'q3',
                   'q4',
                   'q5',
                   'q6',
                   'q7',
                   'q8',
                   'q9',
                   'q10',
                   'q11',
                   'q12',
                   'q13',
                   'q14',
                   'q15',
                   'q16',
                   'q17',
                   'q18',
                   'q19',
                   'q20',
                   'q21',
                   'q22',
                   'q23',
                   'q24',
                   'q25',
                   'q26',
                   'q27',
                   'q28',
                   'q29',
                   'q30',
                   'q31',
                   'q32',
                   'q33',
                   'q34',
                   'q35',
                   'q36',
                   'q37',
                   'q38',
                   'q39',
                   'q40',
                   'q41',
                   'q42',
                   'q43',
                   'q44',
                   'q45',
                   'q46',
                   'q47',
                   'q48',
                   'q49',
                   'q50',
                   'q51',
                   'q52',
                   'q53',
                   'q54',
                   'q55',
                   'q56',
                   'q57',
                   'q58',
                   'q59',
                   'q60',
                   ]



class CognitiveReflectionTest(Page):
    form_model = models.Player
    form_fields = ['crt_bat',
                   'crt_widget',
                   'crt_lake']


page_sequence = [
    Demographics,
    Personality,
    CognitiveReflectionTest
]
