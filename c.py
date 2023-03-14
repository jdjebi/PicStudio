def jaydebeapi_data_converter(data):
    """ 
        jaydebeapi retourne des classes java : <java class 'java.lang.[type]'>
        Cette fonction Converti les classes java retournees par jaydebeapi en type python.
        En effet, on ne peut utiliser les classe java pour creer des Pandas Spark DataFrame.
        Mapping de type:
        <java class 'java.lang.String'>   => str
        <java class 'java.lang.Booleen'>  => bool
        <java class 'java.lang.Integer'>  => int
    """
    import java
    tmp = []
    for row in data:
        new_row = []
        for elm in row:
            if java.lang.String == type(elm):
                new_row.append(str(elm))
            elif java.lang.Integer == type(elm):
                new_row.append(int(elm))
            elif java.lang.Boolean == type(elm):
                new_row.append(bool(elm))
            else:
                raise f"Type {str(elm)} non pris en charge"
        tmp.append(new_row)
    return tmp

def jaydebeapi_exec_query():
    pass

catalogue_rows = jaydebeapi_exec_query('select * from catalogue_hive')
co2_rows = jaydebeapi_exec_query('select * from co2_hive_oraclenosql_ext')

import pandas as pd

catalogue_pdf:pd.DataFrame

catalogue_pdf.marque.unique()

catalogue_pdf.marque.unique().to_numpy()

array(['Volkswagen', 'Peugeot', 'Volvo', 'Saab', 'Seat', 'Renault',
       'Skoda', 'Nissan', 'Jaguar', 'Lancia', 'Mini', 'Kia', 'Honda',
       'Audi', 'Mercedes', 'BMW', 'Dacia', 'Daihatsu', 'Fiat', 'Ford',
       'Hyunda�'], dtype=object)

catalogue_pdf["occasion"] = catalogue_pdf["occasion"].astype(int)
catalogue_pdf.loc[catalogue_pdf.longueur == "tr�s longue","longueur"] = "très longue"
catalogue_pdf.loc[catalogue_pdf.marque== "Hyunda�","marque"] = "Hyundai"
co2_pdf["rejets_co2_gkm"] = co2_pdf["rejets_co2_gkm"].astype(int)

co2_pdf[["marque","nom"]] = co2_pdf['marque_modele'].str.split(' ', 1, expand=True)
co2_pdf.head(3)

co2_pdf = co2_pdf.spark.cache()