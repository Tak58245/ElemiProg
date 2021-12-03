class Képviselőjelölt:

    def __init__(self, valaszto_Kerulet, szavazatok_Szaama, jelolt_Vezetek_Neve,jelolt_Kereszt_Neve,tamogato_Párt):
        self.valaszto_Kerulet = int(valaszto_Kerulet);
        self.szavazatok_Szama = int(szavazatok_Szaama);
        self.jelolt_Neve =jelolt_Vezetek_Neve +' '+ jelolt_Kereszt_Neve;
        self.tamogato_Párt=tamogato_Párt

