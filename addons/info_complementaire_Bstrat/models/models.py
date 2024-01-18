from odoo import models , fields

class Ttee(models.Model):
    _inherit = 'res.partner'
    date_creation = fields.Date(string="Date de creation")
    organisme_finance = fields.Selection([
        ("GIAC_TERTIARE", "GIAC TERTIARE"),
        ("GIAC_1", "GIAC 1"),
        ("GIAC_BTP", "GIAC BTP")
    ], string="Organisme de financement")

    activite = fields.Selection([
        ("Fourniture_de_bureau_et_fourniture_industrielle", "Fourniture de bureau et fourniture industrielle"),
        ("L'habilitation_de_la_famille_sur_le_plan_cognitif_éducatif_économique_et_social","L'habilitation de la famille sur le plan cognitif, éducatif, économique et social"),
        ( "Importation_et_distribution_des_dispositifs_médicaux","Importation et distribution des dispositifs médicaux"),
        ("Production_et_distribution_des_dispositifs_médicaux","Production et distribution des dispositifs médicaux"),
        ("Travaux_d_installation_et_d_entretien_des_systèmes_HVAC","Travaux d'installation et d'entretien des systèmes HVAC"),
        ("Fabrication_de_jouets_en_plastique","Fabrication de jouets en plastique"),
        ("Contrôle_inspection_livraison_de_marchandises_maritimes_transport","Contrôle, inspection, livraison de marchandises maritimes transport"),
        ("Négociant_marchand_importeur","Négociant marchand importeur"),
        ("Importation_et_distribution_du_materielet_consommable_dantaire","Importation et distribution du materielet consommable dantaire"),
        ("Travaux_divers_BTP","Travaux divers BTP"),
        ("Négoce_import_export","Négoce import export")
    ], string="Activité")
    secteur_activite = fields.Selection([
        ("Commerce","Commerce"),
        ("Humanitaire","Humanitaire"),
        ("Médical","Médical"),
        ("Achat_Vente_et_maintenance_des_dispositifs_médicaux","Achat, Vente et maintenance des dispositifs médicaux"),
        ("Santé","Santé"),
        ("Réfrigération_industrielle_&_commercial_traitement_d'air_ventilation_&_désenfumage","Réfrigération industrielle & commercial - traitement d'air  - ventilation & désenfumage"),
        ('Plastique',"Plastique"),
        ("Secteur_maritime","Secteur maritime"),
        ("BTP/Génie_civil","BTP/ Génie civil"),
        ("Article_pour_chaussures_et_maroquinerie","Article pour chaussures et maroquinerie")
    ], string="Secteur d'activite" )
    #nom_du_responsable = fields.Selection(related="res.partner.child_ids")
    x_fax=fields.Char(string="Fax")
    respo=fields.Many2one("res.partner",string="Nom du responsable",domain="[('parent_id','=',id),('is_company','=',False)]")


