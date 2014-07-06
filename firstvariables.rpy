label firstvariables:

    $ captain_moralist = 0
    $ captain_prince = 0
    $ affection_ava = 0
    $ affection_asaga = 0
    $ affection_chigara = 0
    $ affection_icari = 0
    $ affection_claude = 0
    $ affection_tera = 0
    $ affection_sola = 0
    $ affection_cosette = 0

    $ MetAsaga = False
    $ ChigaraRefugee = False
    $ mission_pirateattack = False

    $ battlemusic = True

    $ galaxymission1 = False
    $ galaxymission2 = False
    $ galaxymission3 = False
    $ mission1 = None
    $ mission2 = None
    $ mission3 = None
    $ mission1_name = None
    $ mission2_name = None
    $ mission3_name = None

    $ mission3_complete = False
    $ mission4_complete = False
    $ mission5_complete = False
    $ mission6_complete = False

    $ asa_location = None
    $ chi_location = None
    $ pro_location = None
    $ gal_location = None
    $ cal_location = None
    $ res_location = None
    $ ica_location = None
    $ sol_location = None
    $ cla_location = None
    $ cos_location = None
    $ kry_location = None

    $ warpto_tydaria = False
    $ warpto_occupiedcera = False
    $ warpto_astralexpanse = False
    $ warpto_pactstation1 = False
    $ warpto_versta = False
    $ warpto_nomodorn = False

    $ ep2_cancelwarp = False

    $ supportedasagacards = False
    $ paladin = None

    #$ sunrider = 0
    #$ blackjack = 0
    #$ liberty = 0
    #$ phoenix = 0
    #$ bianca = 0
    #$ seraphim = 0
    #$ paradigm = 0
    #$ havoc = 0

    return


##experimental compatibility stuff##

init python:
    class AllVariables(store.object):
        def __init__(self):
            self.captain_moralist = 0
            self.captain_prince = 0
            self.affection_ava = 0
            self.affection_asaga = 0
            self.affection_chigara = 0
            self.affection_icari = 0
            self.affection_claude = 0
            self.affection_tera = 0
            self.affection_sola = 0
            self.affection_cosette = 0

            self.MetAsaga = False
            self.ChigaraRefugee = False
            self.mission_pirateattack = False

            self.battlemusic = True

            self.galaxymission1 = False
            self.galaxymission2 = False
            self.galaxymission3 = False
            self.mission1 = None
            self.mission2 = None
            self.mission3 = None
            self.mission1_name = None
            self.mission2_name = None
            self.mission3_name = None

            self.mission3_complete = False
            self.mission4_complete = False
            self.mission5_complete = False
            self.mission6_complete = False

            self.asa_location = None
            self.chi_location = None
            self.pro_location = None
            self.gal_location = None
            self.cal_location = None
            self.res_location = None
            self.ica_location = None
            self.sol_location = None
            self.cla_location = None
            self.cos_location = None
            self.kry_location = None

            self.warpto_tydaria = False
            self.warpto_occupiedcera = False
            self.warpto_astralexpanse = False
            self.warpto_pactstation1 = False
            self.warpto_versta = False
            self.warpto_nomodorn = False

            self.ep2_cancelwarp = False

            self.supportedasagacards = False

            self.sunrider = None
            self.blackjack = None
            self.liberty = None
            self.phoenix = None
            self.bianca = None
            self.seraphim = None
            self.paradigm = None
            self.havoc = None
            self.paladin = None

            self.check1 = False
            self.check2 = False
            self.check3 = False
            self.check4 = False
            self.check5 = False
            self.check6 = False
            self.check7 = False
            self.check8 = False
            self.check9 = False

            ##new constants##

            self.TURN_SPEED = 0.5  #in seconds
            self.MOVE_IN_SPEED = 0.5 #for buttons and status displays
            self.MOVE_OUT_SPEED = 0.5
            self.MESSAGE_PAUSE = 0.75
            self.MISSILE_SPEED = 0.3
            self.SHIP_SPEED = 0.3
            self.ZOOM_SPEED = 0.1
            self.GRID_SIZE = (18,16)
            self.BM = renpy.store.object()
            self.BM.phase = None
















