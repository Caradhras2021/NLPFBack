from Flask_Api_MongoDB.apiMongo import db


class DateModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_mutation = db.Column(db.String(100), nullable=False)
    date_mutation = db.Column(db.String(100), nullable=False)
    numero_disposition = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Date(id_mutation = {id_mutation}, date_mutation = {date_mutation}, numero_disposition = {numero_disposition})"


class PrixModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valeur_fonciere = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Prix(valeur_fonciere = {valeur_fonciere})"

class LocalisationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adresse_numero = db.Column(db.String(100), nullable=False)
    adresse_suffixe = db.Column(db.String(100), nullable=False)
    adresse_code_voie = db.Column(db.String(100), nullable=False)
    adresse_nom_voie = db.Column(db.String(100), nullable=False)
    code_postal = db.Column(db.String(100), nullable=False)
    code_commune = db.Column(db.String(100), nullable=False)
    nom_commune = db.Column(db.String(100), nullable=False)
    ancien_code_commune = db.Column(db.String(100), nullable=False)
    ancien_nom_commune = db.Column(db.String(100), nullable=False)
    code_departement = db.Column(db.String(100), nullable=False)
    id_parcelle = db.Column(db.Integer, nullable=False)
    ancien_id_parcelle = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Float64, nullable=False)
    latitude = db.Column(db.Float64, nullable=False)

    def __repr__(self):
            return f"Localisation(adresse_numero = {adresse_numero}, adresse_suffixe = {adresse_suffixe}, \
                adresse_code_voie = {adresse_code_voie}, adresse_nom_voie = {adresse_nom_voie}, \
                code_postal = {code_postal}, code_commune= {code_commune}, nom_commune  {nom_commune}, \
                ancien_code_commune = {ancien_code_commune}, ancien_nom_commune = {ancien_nom_commune}, \
                code_departement = {code_departement}, id_parcelle = {id_parcelle}, ancien_id_parcelle = {ancien_id_parcelle}, \
                longitude = {longitude}, latitude = {latitude})"

class ParcelleHabitableModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_volume = db.Column(db.Integer, nullable=False)
    lot_1_numero = db.Column(db.Integer, nullable=False)
    lot_1_surface_carrez = db.Column(db.String(100), nullable=False)
    lot_2_numero = db.Column(db.Integer, nullable=False)
    lot_2_surface_carrez = db.Column(db.String(100), nullable=False)
    lot_3_numero = db.Column(db.Integer, nullable=False)
    lot_3_surface_carrez = db.Column(db.String(100), nullable=False)
    lot_4_numero = db.Column(db.Integer, nullable=False)
    lot_4_surface_carrez = db.Column(db.String(100), nullable=False)
    lot_5_numero = db.Column(db.Integer, nullable=False)
    lot_5_surface_carrez = db.Column(db.String(100), nullable=False)
    nombre_lots = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"ParcelleHabitable(numero_volume = {numero_volume}, lot_1_numero = {lot_1_numero}, \
                lot_1_surface_carrez = {lot_1_surface_carrez}, lot_2_numero = {lot_2_numero}, \
                lot_2_surface_carrez = {lot_2_surface_carrez}, lot_3_numero = {lot_3_numero}, lot_4_numero = {lot_4_numero}, \
                lot_4_surface_carrez = {lot_4_surface_carrez}, lot_5_numero = {lot_5_numero}, \
                lot_5_surface_carrez = {lot_5_surface_carrez}, nombre_lots = {nombre_lots})"

class TerrainModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_lots = db.Column(db.Integer, nullable=False)
    type_local = db.Column(db.String(100), nullable=False)
    surface_reelle_bati = db.Column(db.String(100), nullable=False)
    nombre_pieces_principales = db.Column(db.Integer, nullable=False)
    surface_terrain = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"TerrainModel(nombre_lots = {nombre_lots}, type_local = {type_local}, \
                surface_reelle_bati = {surface_reelle_bati}, nombre_pieces_principales = {nombre_pieces_principales}, \
                surface_terrain = {surface_terrain})"

class NatureModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_nature_culture = db.Column(db.String(100), nullable=False)
    nature_culture = db.Column(db.String(100), nullable=False)
    code_nature_culture_speciale = db.Column(db.String(100), nullable=False)
    nature_culture_speciale = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"NatureModel(code_nature_culture = {code_nature_culture}, nature_culture = {nature_culture}, \
                code_nature_culture_speciale = {code_nature_culture_speciale}, nature_culture_speciale = {nature_culture_speciale})"