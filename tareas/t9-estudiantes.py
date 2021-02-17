# Nombre: Diego Eduardo Paz Letelier
# Paralelo: 211


siglas = {
    'LMA': 'Leucemia Mieloide Aguda',
    'IAM': 'Infarto Agudo al Miocardio',
    'C19': 'Coronavirus',
    'HCA': 'Hepatitis Cronica Activa',
    'FQ': 'Fibrosis Quistica',
    'ECV': 'Enfermedad Cerebro Vascular',
    'DBT': 'Diabetes',
    'IRA': 'Insuficiencia Renal Aguda',
    'TBC': 'Tuberculosis',
    'TQC': 'Taquicardia',
    'UG': 'Ulcera Gastrica',
    'EM': 'Esclerosis Multiple',
    'M': 'Meningitis',
    'OMA': 'Otitis Media Aguda',
    'PNF': 'Pielonefritis',
    'EA': 'Alzheimer',
    'NIH': 'Neumonia Intra-Hospitalaria',
    'IHO': 'Infeccion Herida Operatoria',
    'HPT': 'Hipertension Pulmonar',
    'EP': 'Embolismo Pulmonar',
    'CBP': 'Cirrosis Biliar Primaria',
    'ARJ': 'Artritis Reumatoidea Juvenil',
    'SLT': 'Sindrome de Lisis Tumoral',
    'VZV': 'Virus Varicela Zoster',
    'TVP': 'Trombosis Venosa Profunda',
    'EI': 'Endocarditis Infecciosa',
    'AE': 'Arterioesclerosis',
    'HEL': 'Hemorragia Exterior Leve',
    'RF': 'Resfriado Comun',
    'E1': 'Esquince Nivel 1',
    'D': 'Depresion',
    'ART': 'Artrosis',
    'MG': 'Migrania',
    'HL': 'Herpes Labial',
    'LG': 'Laringitis',
    'FG': 'Faringitis',
    'GMN': 'Glomerulonefritis'
}

triage = {
    'C1': ['GMN', 'IAM', 'PNF', 'TVP', 'ECV', 'EP', 'C19'],
    'C2': ['LMA', 'TBC', 'NIH', 'IHO', 'HPT', 'FQ', 'SLT', 'IRA', 'M'],
    'C3': ['HCA', 'UG', 'EM', 'TQC'],
    'C4': ['DBT', 'CBP', 'VZV', 'ART', 'OMA'],
    'C5': ['EA', 'ARJ', 'HEL', 'RF', 'E1', 'D', 'MG', 'HL', 'LG', 'FG', 'EI']
}

# Escriba aquí sus funciones


def siglas_x_categoria(triage, lista):
    cantidad = {'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0}
    for sigla in lista:
        for categoria in triage:
            if sigla in triage[categoria]:
                cantidad[categoria] += 1
    return cantidad


def priorizar(siglas, triage, lista):
    k = []
    for categoria in triage:
        for sigla in lista:
            if sigla in triage[categoria]:
                k.append(siglas[sigla])
    return k


# Casos de prueba de los ejemplos


lista = ['ARJ', 'OMA', 'GMN', 'NIH', 'HCA', 'C19']
print(siglas_x_categoria(triage, lista))
# Salida esperada: {'C5': 1, 'C4': 1, 'C1': 2, 'C2': 1, 'C3': 1}

lista = ['D', 'M', 'IAM', 'TBC', 'MG', 'ART', 'C19']
print(priorizar(siglas, triage, lista))
# Salida esperada:
# ['Infarto Agudo al Miocardio', 'Coronavirus', 'Meningitis', 'Tuberculosis',
# 'Artrosis', 'Depresion', 'Migrania']
