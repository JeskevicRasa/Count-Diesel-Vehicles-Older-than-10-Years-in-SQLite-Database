import sqlite3
import csv

db_name = "autoparkas.db"
table_name = "Autoparkas"
csv_file = "Atviri_TP_parko_duomenys.csv"

columns = """
    MARKE, KOMERCINIS_PAV, GAMINTOJO_PAV, GAMINTOJO_PAV_BAZ, TIPAS, VARIANTAS, VERSIJA, ES_TIPO_PATVIRTINIMO_NR, NAC_TIPO_PATVIRTINIMO_NR, 
    INDIVIDUAL_PATVIRTINIMO_NR, INTERPOLIACIJA, UZBAIGTUMO_PAKOPA, VAIRAS_DESINEJE, KATEGORIJA_PILNAI, KATEGORIJA_KLASE, KEB_KODAS, KEB_PAVADINIMAS, 
    SPEC_KODAS, SPEC_PAVADINIMAS, KEB_KODAS_ES, NUOSAVA_MASE, NUOSAVA_MASE_BAZ, MAKS_MASE, MAKS_MASE_F2, MAKS_MASE_F5, BANDOMOJI_MASE, DARBINIS_TURIS, 
    GALIA, SUKIU_SK, GALIA_ELEKTR, DEGALAI, DEGALU_REZIMAS, ELEKTRINE_TP, HIBRIDINES_TP_KATEGORIJA, PAVARU_DEZES_TIPAS, CO2_KIEKIS, CO2_KIEKIS_WLTP, 
    EKO_NAUJOVES_KODAS, CO2_SUMAZEJIMAS_NEDC, CO2_SUMAZEJIMAS_WLTP, ELEKTR_ENERG_SANAUD_NEDC, ELEKTR_ENERG_SANAUD_WLTP_E, ELEKTR_ENERG_SANAUD_WLTP_H, 
    ELEKTRINE_RIDA_NEDC, ELEKTRINE_RIDA_WLTP_E, ELEKTRINE_RIDA_WLTP_H, TERSALU_LYGIS, TERSALU_NORM_AKTO_NR, RATU_BAZE, TV_PLOTIS1, TV_PLOTIS2, 
    SPALVA, GALIOS_MASES_SANT, MAKS_GREITIS, SEDIMU_VIETU_SK, STOVIMU_VIETU_SK, GAMYBOS_METAI, MODELIO_METAI, RIDA, PIRM_REG_DATA, PIRM_REG_DATA_LT, 
    GALIOJIMO_LAIK, PASKUTINES_REG_DATA, DAE_STATUSAS, KILMES_SALIS, VALD_TIPAS, VALD_GIM_DAT_INT, SAVIVALDYBE, APSKRITIS
"""

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

create_table_query = f"CREATE TABLE {table_name} ({columns})"
cursor.execute(create_table_query)

with open(csv_file, 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        placeholders = ', '.join('?' for _ in row)
        cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)


conn.commit()
conn.close()