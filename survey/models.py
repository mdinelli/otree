from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import math
import statistics


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=125)

    gender = models.CharField(
        choices=['Male', 'Female','Transgender Female','Transgender Male','Gender Variant/Non-conforming','Not listed','Prefer not to answer'],
        verbose_name='To which gender identity do you most identify?',
        widget=widgets.RadioSelect())
    other_g = models.CharField(blank=True,
        verbose_name='If "Not listed," please specify')

    Latinx_ethnicity = models.CharField(
        choices=['Yes', 'No', 'Prefer not to answer'],
        verbose_name='Do you consider yourself to be Hispanic or Latino/Latina/Latinx?',
        widget=widgets.RadioSelect(),
        # widget=widgets.forms.CheckboxSelectMultiple(),
        )

    # checkbox1 = models.BooleanField(initial=False)
    # checkbox2 = models.BooleanField(initial=False)
    # checkbox3 = models.BooleanField(initial=False)



    race = models.CharField(
        choices=[{'American Indian or Alaska Native','Asian'},'American Indian or Alaska Native','Asian','Black or African American','Native Hawaiian or Other Pacific Islander','White','Prefer not to respond'],
        verbose_name='Regardless of your answer to the prior question, please check one or more of the following groups in which you consider yourself to be a member',
        widget=widgets.RadioSelect(),
        #widget=widgets.CheckboxSelectMultiple(),
    blank=True)
    other_r = models.CharField(blank=True,
        verbose_name='If "Other," please specify')

    income = models.CharField(
        choices=['$0 to $19,999','$20,000 to $39,999','$40,000 to $59,999','$60,000 to $79,999','$80,000 to $99,999',
                 '$100,000 to $119,999','$120,000 to $159,999','$160,000 or more','Prefer not to answer'],
        verbose_name='Plese estimate your gross family income',
        widget=widgets.RadioSelect())

    education = models.CharField(
        choices=['First year','Second year','Third year', 'Fourth year', 'Other','Prefer not to answer'],
        verbose_name='What is your level of education? If not in College, pick "other" and please report your level of education below',
        widget=widgets.RadioSelect())

    other_e = models.CharField(blank=True,
                               verbose_name='If "Other," please specify')


    q1 = models.CharField(
        verbose_name='I am someone who... '
                     'Is outgoing, sociable.',
        choices=['1:Disagree Strongly', '2:Disagree a little', '3: No opinion/neutral', '4: Agree a little', '5: Agree strongly'],
        widget=widgets.RadioSelectHorizontal())
    q2 = models.IntegerField(
        verbose_name='Is compassionate, has a soft heart.',
        choices=[1,2,3,4,5],
        # choices = ['1','2','3','4','5'],
        widget=widgets.RadioSelectHorizontal(),
       )
    q3 = models.PositiveIntegerField(
        verbose_name='Tends to be disorganized.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q4 = models.PositiveIntegerField(
        verbose_name='Is relaxed, handles stress well.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q5 = models.PositiveIntegerField(
        verbose_name='Has few artistic interests.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q6 = models.PositiveIntegerField(
        verbose_name='Has an assertive personality.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q7 = models.PositiveIntegerField(
        verbose_name='Is respectful, treats others with respect.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q8 = models.PositiveIntegerField(
        verbose_name='Tends to be lazy.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q9 = models.PositiveIntegerField(
        verbose_name='Stays optimistic after experiencing a setback.',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q10 = models.PositiveIntegerField(
        verbose_name='Is curious about many different things. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q11 = models.PositiveIntegerField(
        verbose_name='Rarely feels excited or eager. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q12 = models.PositiveIntegerField(
        verbose_name='Tends to find fault with others. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q13 = models.PositiveIntegerField(
        verbose_name='Is dependable, steady. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q14 = models.PositiveIntegerField(
        verbose_name='Is moody, has up and down mood swings. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q15 = models.PositiveIntegerField(
        verbose_name='Is inventive, finds clever ways to do things. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q16 = models.PositiveIntegerField(
        verbose_name='Tends to be quiet. ',
        min=1, max=5)
    q17 = models.PositiveIntegerField(
        verbose_name='Feels little sympathy for others. ',
        min=1, max=5)
    q18 = models.PositiveIntegerField(
        verbose_name='Is systematic, likes to keep things in order. ',
        min=1, max=5)
    q19 = models.PositiveIntegerField(
        verbose_name='Can be tense. ',
        min=1, max=5)
    q20 = models.PositiveIntegerField(
        verbose_name='Is fascinated by art, music, or literature. ',
        min=1, max=5)
    q21 = models.PositiveIntegerField(
        verbose_name='Is dominant, acts as a leader. ',
        min=1, max=5)
    q22 = models.PositiveIntegerField(
        verbose_name='Starts arguments with others. ',
        min=1, max=5)
    q23 = models.PositiveIntegerField(
        verbose_name='Has difficulty getting started on tasks. ',
        min=1, max=5)
    q24 = models.PositiveIntegerField(
        verbose_name='Feels secure, comfortable with self. ',
        min=1, max=5)
    q25 = models.PositiveIntegerField(
        verbose_name='Avoids intellectual, philosophical discussions. ',
        min=1, max=5)
    q26 = models.PositiveIntegerField(
        verbose_name='Is less active than other people. ',
        min=1, max=5)
    q27 = models.PositiveIntegerField(
        verbose_name='Has a forgiving nature. ',
        min=1, max=5)
    q28 = models.PositiveIntegerField(
        verbose_name='Can be somewhat careless. ',
        min=1, max=5)
    q29 = models.PositiveIntegerField(
        verbose_name='Is emotionally stable, not easily upset.',
        min=1, max=5)
    q30 = models.PositiveIntegerField(
        verbose_name='Has little creativity. ',
        min=1, max=5)
    q31 = models.PositiveIntegerField(
        verbose_name='Is sometimes shy, introverted. ',
        min=1, max=5)
    q32 = models.PositiveIntegerField(
        verbose_name='Is helpful and unselfish with others.',
        min=1, max=5)
    q33 = models.PositiveIntegerField(
        verbose_name='Keeps things neat and tidy.',
        min=1, max=5)
    q34 = models.PositiveIntegerField(
        verbose_name='Worries a lot.',
        min=1, max=5)
    q35 = models.PositiveIntegerField(
        verbose_name='Values art and beauty.',
        min=1, max=5)
    q36 = models.PositiveIntegerField(
        verbose_name='Finds it hard to influence people.',
        min=1, max=5)
    q37 = models.PositiveIntegerField(
        verbose_name='Is sometimes rude to others.',
        min=1, max=5)
    q38 = models.PositiveIntegerField(
        verbose_name='Is efficient, gets things done. ',
        min=1, max=5)
    q39 = models.PositiveIntegerField(
        verbose_name='Often feels sad.',
        min=1, max=5)
    q40 = models.PositiveIntegerField(
        verbose_name='Is complex, a deep thinker. ',
        min=1, max=5)
    q41 = models.PositiveIntegerField(
        verbose_name='Is full of energy. ',
        min=1, max=5)
    q42 = models.PositiveIntegerField(
        verbose_name='Is suspicious of others’ intentions. ',
        min=1, max=5)
    q43 = models.PositiveIntegerField(
        verbose_name='Is reliable, can always be counted on. ',
        min=1, max=5)
    q44 = models.PositiveIntegerField(
        verbose_name='Keeps their emotions under control. ',
        min=1, max=5)
    q45 = models.PositiveIntegerField(
        verbose_name='Has difficulty imagining things.',
        min=1, max=5)
    q46 = models.PositiveIntegerField(
        verbose_name='Is talkative. ',
        min=1, max=5)
    q47 = models.PositiveIntegerField(
        verbose_name='Can be cold and uncaring.',
        min=1, max=5)
    q48 = models.PositiveIntegerField(
        verbose_name='Leaves a mess, doesn’t clean up. ',
        min=1, max=5)
    q49 = models.PositiveIntegerField(
        verbose_name='Rarely feels anxious or afraid. ',
        min=1, max=5)
    q50 = models.PositiveIntegerField(
        verbose_name='Thinks poetry and plays are boring. ',
        min=1, max=5)
    q51 = models.PositiveIntegerField(
        verbose_name='Prefers to have others take charge. ',
        min=1, max=5)
    q52 = models.PositiveIntegerField(
        verbose_name='Is polite, courteous to others. ',
        min=1, max=5)
    q53 = models.PositiveIntegerField(
        verbose_name='Is persistent, works until the task is finished. ',
        min=1, max=5)
    q54 = models.PositiveIntegerField(
        verbose_name='Tends to feel depressed, blue. ',
        min=1, max=5)
    q55 = models.PositiveIntegerField(
        verbose_name='Has little interest in abstract ideas.',
        min=1, max=5)
    q56 = models.PositiveIntegerField(
        verbose_name='Shows a lot of enthusiasm. ',
        min=1, max=5)
    q57 = models.PositiveIntegerField(
        verbose_name='Assumes the best about people. ',
        min=1, max=5)
    q58 = models.PositiveIntegerField(
        verbose_name='Sometimes behaves irresponsibly. ',
        min=1, max=5)
    q59 = models.PositiveIntegerField(
        verbose_name='Is temperamental, gets emotional easily. ',
        min=1, max=5)
    q60 = models.PositiveIntegerField(
        verbose_name='Is original, comes up with new ideas. ',
        min=1, max=5)

    "b = models.IntegerField(getattr(player, 'q59'))"
    a = models.IntegerField(initial = 2)



    "a = model.Integer(2 + 3)"

    """"
    Sociability: q1, (6-q16),(6-q31), q46
    Assertiveness: q6, q21, (6-q36), (6-q51)
    Energy Level: (6-q11), (6-q26), q41, q56
    Compassion: q2, (6-q17), q32, (6-q47)
    Respectfulness: 7, 22R, 37R, 52
    Trust: (6-q12), q27, (6-q42), q57
    Organization: (6-q3), q18, q33, (6-q48)
    Productiveness: (6-q8), (6-q23), q38, q53
    Responsibility: q13, (6-q28), q43, (6-q58)
    Anxiety: (6-q4), q19, q34, (6-q49)
    Depression: (6-q9), (6-q24), q39, q54
    Emotional Volatility: q14, (6-q29), (6-q44), q59
    Intellectual Curiosity: q10, (6-q25), q40, (6-q55)
    Aesthetic Sensitivity: (6-q5), q20, q35, (6-q50)
    Creative Imagination: q15, (6-q30), (6-q45), q60 """



    """"
    sociability = q1 + q16 + q31 + q46

    bassertiveness = q6 + q21 + q36 + q51
    energy_level = q11 + q26 + q41 + q56
    compassion = q2 + q17 + q32 + q47
    respectfulness = q7 + q22 + q37 + q52
    trust = q12 + q27 + q42 + q57
   COMPUTE
    bfi2_c_organization = MEAN(rbfi3, bfi18, bfi33, rbfi48).
    COMPUTE
    bfi2_c_productiveness = MEAN(rbfi8, rbfi23, bfi38, bfi53).
    COMPUTE
    bfi2_c_responsibility = MEAN(bfi13, rbfi28, bfi43, rbfi58).
    COMPUTE
    bfi2_n_anxiety = MEAN(rbfi4, bfi19, bfi34, rbfi49).
    COMPUTE
    bfi2_n_depression = MEAN(rbfi9, rbfi24, bfi39, bfi54).
    COMPUTE
    bfi2_n_emotional_volatility = MEAN(bfi14, rbfi29, rbfi44, bfi59).
    COMPUTE
    bfi2_o_intellectual_curiosity = MEAN(bfi10, rbfi25, bfi40, rbfi55).
    COMPUTE
    bfi2_o_aesthetic_sensitivity = MEAN(rbfi5, bfi20, bfi35, rbfi50).
    COMPUTE
    bfi2_o_creative_imagination = MEAN(bfi15, rbfi30, rbfi45, bfi60)."""

    crt_bat = models.PositiveIntegerField(
        verbose_name='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )

    crt_widget = models.PositiveIntegerField(
        verbose_name='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )

    crt_lake = models.PositiveIntegerField(
        verbose_name='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )
   #  1:Disagree Strongly, 2:Disagree a little, 3: No opinion/neutral, 4: Agree a little, 5: Agree strongly