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
    my_error_s = models.IntegerField(initial=0)


    age = models.PositiveIntegerField(
        verbose_name='What is your age? If you prefer not to answer, put "0"',

        min=0, max=125)

    gender = models.CharField(
        choices=['Male', 'Female','Transgender Female','Transgender Male','Gender Variant/Non-conforming','Not listed','Prefer not to answer'],
        verbose_name='With which gender identity do you most identify?',
        widget=widgets.RadioSelect())
    other_g = models.CharField(blank=True,
        verbose_name='If "Not listed," please specify')

    Latinx_ethnicity = models.CharField(
        choices=['Yes', 'No', 'Prefer not to answer'],
        verbose_name='Do you consider yourself to be Hispanic or Latino/Latina/Latinx?'
                     '(A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race)',
        widget=widgets.RadioSelect()
        )


    race = models.CharField(
        choices=['American Indian or Alaska Native','Asian','Black or African American',
                 'Native Hawaiian or Other Pacific Islander'
                 '(A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands)',
                 'White(A person having origins in any of the original peoples of Europe, the Middle East, or North Africa)',
                 'Not listed or Multiracial','Prefer not to answer'],
        verbose_name='Regardless of your answer to the prior question, please choose one or more of the following groups '
                     'in which you consider yourself to be a member',
        widget=widgets.RadioSelect()
    )
    other_r = models.CharField(blank=True,
        verbose_name='If "Not listed or Multiracial," please specify')

    income = models.CharField(
        choices=['$0 to $59,999','$60,000 to $79,999','$80,000 to $99,999',
                 '$100,000 to $119,999','$120,000 to $159,999','$160,000 or more','Prefer not to answer'],
        verbose_name='Please estimate your gross family income',
        widget=widgets.RadioSelect())

    education = models.CharField(
        choices=['College first year/Freshman','College second year/Sophomore','College third year/Junior',
                 'College fourth year/Senior', 'Other','Prefer not to answer'],
        verbose_name='What is your level of education? If not in College, pick "other" and please report your level of education below',
        widget=widgets.RadioSelect())

    other_e = models.CharField(blank=True,
                               verbose_name='If "Other," please specify')


    q1 = models.CharField(
        verbose_name='Is outgoing, sociable.',
        choices=['1:Disagree Strongly', '2:Disagree a little', '3: No opinion/neutral', '4: Agree a little', '5: Agree strongly'],
        blank=True,
        widget=widgets.RadioSelectHorizontal())
    q2 = models.IntegerField(
        verbose_name='Is compassionate, has a soft heart.',
        choices=[1,2,3,4,5],
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
       )
    q3 = models.PositiveIntegerField(
        verbose_name='Tends to be disorganized.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q4 = models.PositiveIntegerField(
        verbose_name='Is relaxed, handles stress well.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q5 = models.PositiveIntegerField(
        verbose_name='Has few artistic interests.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q6 = models.PositiveIntegerField(
        verbose_name='Has an assertive personality.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q7 = models.PositiveIntegerField(
        verbose_name='Is respectful, treats others with respect.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q8 = models.PositiveIntegerField(
        verbose_name='Tends to be lazy.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q9 = models.PositiveIntegerField(
        verbose_name='Stays optimistic after experiencing a setback.',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q10 = models.PositiveIntegerField(
        verbose_name='Is curious about many different things. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q11 = models.PositiveIntegerField(
        verbose_name='Rarely feels excited or eager. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q12 = models.PositiveIntegerField(
        verbose_name='Tends to find fault with others. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q13 = models.PositiveIntegerField(
        verbose_name='Is dependable, steady. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q14 = models.PositiveIntegerField(
        verbose_name='Is moody, has up and down mood swings. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q15 = models.PositiveIntegerField(
        verbose_name='Is inventive, finds clever ways to do things. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q16 = models.PositiveIntegerField(
        verbose_name='Tends to be quiet. ',
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q17 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Feels little sympathy for others. ',
        choices=[1, 2, 3, 4, 5])
    q18 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is systematic, likes to keep things in order. ',
        choices=[1, 2, 3, 4, 5])
    q19 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Can be tense. ',
        choices=[1, 2, 3, 4, 5])
    q20 = models.PositiveIntegerField(
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is fascinated by art, music, or literature. ',
        blank=True,
        choices=[1, 2, 3, 4, 5])
    q21 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is dominant, acts as a leader. ',
        choices=[1, 2, 3, 4, 5])
    q22 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Starts arguments with others. ',
        choices=[1, 2, 3, 4, 5])
    q23 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Has difficulty getting started on tasks. ',
        choices=[1, 2, 3, 4, 5])
    q24 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Feels secure, comfortable with self. ',
        choices=[1, 2, 3, 4, 5])
    q25 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Avoids intellectual, philosophical discussions. ',
        choices=[1, 2, 3, 4, 5])
    q26 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is less active than other people. ',
        choices=[1, 2, 3, 4, 5])
    q27 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Has a forgiving nature. ',
        choices=[1, 2, 3, 4, 5])
    q28 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Can be somewhat careless. ',
        choices=[1, 2, 3, 4, 5])
    q29 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is emotionally stable, not easily upset.',
        choices=[1, 2, 3, 4, 5])
    q30 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Has little creativity. ',
        choices=[1, 2, 3, 4, 5])
    q31 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is sometimes shy, introverted. ',
        choices=[1, 2, 3, 4, 5])
    q32 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is helpful and unselfish with others.',
        choices=[1, 2, 3, 4, 5])
    q33 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Keeps things neat and tidy.',
        choices=[1, 2, 3, 4, 5])
    q34 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Worries a lot.',
        choices=[1, 2, 3, 4, 5])
    q35 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Values art and beauty.',
        choices=[1, 2, 3, 4, 5])
    q36 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Finds it hard to influence people.',
        choices=[1, 2, 3, 4, 5])
    q37 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is sometimes rude to others.',
        choices=[1, 2, 3, 4, 5])
    q38 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is efficient, gets things done. ',
        choices=[1, 2, 3, 4, 5])
    q39 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Often feels sad.',
        choices=[1, 2, 3, 4, 5])
    q40 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is complex, a deep thinker. ',
        choices=[1, 2, 3, 4, 5])
    q41 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is full of energy. ',
        choices=[1, 2, 3, 4, 5])
    q42 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is suspicious of others’ intentions. ',
        choices=[1, 2, 3, 4, 5])
    q43 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is reliable, can always be counted on. ',
        choices=[1, 2, 3, 4, 5])
    q44 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Keeps their emotions under control. ',
        choices=[1, 2, 3, 4, 5])
    q45 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Has difficulty imagining things.',
        choices=[1, 2, 3, 4, 5])
    q46 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is talkative. ',
        choices=[1, 2, 3, 4, 5])
    q47 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Can be cold and uncaring.',
        choices=[1, 2, 3, 4, 5])
    q48 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Leaves a mess, doesn’t clean up. ',
        choices=[1, 2, 3, 4, 5])
    q49 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Rarely feels anxious or afraid. ',
        choices=[1, 2, 3, 4, 5])
    q50 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Thinks poetry and plays are boring. ',
        choices=[1, 2, 3, 4, 5])
    q51 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Prefers to have others take charge. ',
        choices=[1, 2, 3, 4, 5])
    q52 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is polite, courteous to others. ',
        choices=[1, 2, 3, 4, 5])
    q53 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is persistent, works until the task is finished. ',
        choices=[1, 2, 3, 4, 5])
    q54 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Tends to feel depressed, blue. ',
        choices=[1, 2, 3, 4, 5])
    q55 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Has little interest in abstract ideas.',
        choices=[1, 2, 3, 4, 5])
    q56 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Shows a lot of enthusiasm. ',
        choices=[1, 2, 3, 4, 5])
    q57 = models.PositiveIntegerField(
        blank=True,
        verbose_name='Assumes the best about people. ',
        widget=widgets.RadioSelectHorizontal(),
        choices=[1, 2, 3, 4, 5])
    q58 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Sometimes behaves irresponsibly. ',
        choices=[1, 2, 3, 4, 5])
    q59 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is temperamental, gets emotional easily. ',
        choices=[1, 2, 3, 4, 5])
    q60 = models.PositiveIntegerField(
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name='Is original, comes up with new ideas. ',
        choices=[1, 2, 3, 4, 5])


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