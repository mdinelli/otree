from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):
        # rounds is used for the instructions template
        return {'instructions_template':'market_wage/Instructions.html',
                'rounds': list(range(1, Constants.num_rounds + 1))}

class Instructions(Page):
    def vars_for_template(self):
        rounds = list(range(1, Constants.num_rounds + 1))
        return {'rounds': rounds,}

class Firm(Page):
    def is_displayed(self):
        return self.player.role() == "firm"

    form_model = models.Group
    form_fields = ["wage"]

    def wage_max(self):
        return Constants.REVENUE[self.round_number]

    def vars_for_template(self):
        groups = self.group.in_all_rounds()
        return {
            # 'history_template': "market_wage/History.html",
            'groups': groups,
            'instructions_template': 'market_wage/Instructions.html',
            'rounds': list(range(1, Constants.num_rounds + 1)),
            'round_number': self.subsession.round_number,
            'revenue_this_round': Constants.REVENUE[self.subsession.round_number],
            'max_revenues': float(self.session.config["base_revenue"] * self.session.config["boom_multiplier"]),
        }

class Worker(Page):
    def is_displayed(self):
        return self.player.role() == "worker"

    form_model = models.Group
    form_fields = ["effort"]

    def vars_for_template(self):
        groups = self.group.in_all_rounds()
        
        return {
            'wage': self.group.wage,
            'groups': groups,
            'instructions_template': 'market_wage/Instructions.html',
            'rounds': list(range(1, Constants.num_rounds + 1)),
            'round_number': self.subsession.round_number,
            'revenue_this_round': Constants.REVENUE[self.subsession.round_number]
        }


class ResultsWaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() == "worker":
            body_text = "You are the worker. Waiting for the firm"
        else:
            body_text = "You are the firm. Waiting for the worker to set an effort value."

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class RoundWaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() == 'worker':
            body_text = "You are the worker. Waiting for the firm to propose a wage."
        else:
            body_text = "You are the firm. Waiting for the worker to set an effort value."
        return {'body_text': body_text}

class Results(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        if self.player.role() == "firm":
            body_text = "Waiting for the worker to set an effort value."
        else:
            body_text = "Waiting for the firm to propose a wage."
        return {
            'groups': self.group.in_all_rounds(),
            'body_text': body_text,
            'firm_total_payoff': sum([g.get_player_by_role("firm").payoff for g in self.group.in_all_rounds()]),
            'worker_total_payoff': sum([g.get_player_by_role("worker").payoff for g in self.group.in_all_rounds()]),
            'role': self.player.role()
        }


page_sequence = [
    Introduction,
    Firm,
    RoundWaitPage,
    Worker,
    ResultsWaitPage,
    Results
]
