import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object


# Creating the Pharmacy node directly under the world node
pharmacy = Location("Pharmacy")

# Sections in the pharmacy
otc_section = Location("Over-the-Counter Medications", parent=pharmacy)
prescription_section = Location("Prescription Medications", parent=pharmacy)
personal_care_section = Location("Personal Care Products", parent=pharmacy)
vitamins_section = Location("Vitamins and Supplements", parent=pharmacy)

# Items in Over-the-Counter Medications Section
pain_relievers = Location("Pain Relievers", parent=otc_section)
aspirin = Object("Aspirin", status="Available", parent=pain_relievers)
ibuprofen = Object("Ibuprofen", status="Available", parent=pain_relievers)
acetaminophen = Object("Acetaminophen", status="Available", parent=pain_relievers)

cold_and_flu = Location("Cold and Flu", parent=otc_section)
cough_syrup = Object("Cough Syrup", status="Available", parent=cold_and_flu)
decongestant = Object("Decongestant", status="Available", parent=cold_and_flu)
antihistamine = Object("Antihistamine", status="Available", parent=cold_and_flu)

digestive_health = Location("Digestive Health", parent=otc_section)
antacid = Object("Antacid", status="Available", parent=digestive_health)
laxative = Object("Laxative", status="Available", parent=digestive_health)
probiotic = Object("Probiotic", status="Available", parent=digestive_health)

# Items in Prescription Medications Section
antibiotics = Location("Antibiotics", parent=prescription_section)
amoxicillin = Object("Amoxicillin", status="Prescription Required", parent=antibiotics)
ciprofloxacin = Object("Ciprofloxacin", status="Prescription Required", parent=antibiotics)

blood_pressure = Location("Blood Pressure Medications", parent=prescription_section)
lisinopril = Object("Lisinopril", status="Prescription Required", parent=blood_pressure)
amlodipine = Object("Amlodipine", status="Prescription Required", parent=blood_pressure)

diabetes = Location("Diabetes Medications", parent=prescription_section)
metformin = Object("Metformin", status="Prescription Required", parent=diabetes)
insulin = Object("Insulin", status="Prescription Required", parent=diabetes)

# Items in Personal Care Products Section
skincare = Location("Skincare", parent=personal_care_section)
moisturizer = Object("Moisturizer", status="Available", parent=skincare)
sunscreen = Object("Sunscreen", status="Available", parent=skincare)
cleanser = Object("Cleanser", status="Available", parent=skincare)

haircare = Location("Haircare", parent=personal_care_section)
shampoo = Object("Shampoo", status="Available", parent=haircare)
conditioner = Object("Conditioner", status="Available", parent=haircare)
hair_oil = Object("Hair Oil", status="Available", parent=haircare)

oral_care = Location("Oral Care", parent=personal_care_section)
toothpaste = Object("Toothpaste", status="Available", parent=oral_care)
mouthwash = Object("Mouthwash", status="Available", parent=oral_care)
toothbrush = Object("Toothbrush", status="Available", parent=oral_care)

# Items in Vitamins and Supplements Section
multivitamins = Location("Multivitamins", parent=vitamins_section)
adult_multivitamin = Object("Adult Multivitamin", status="Available", parent=multivitamins)
childrens_multivitamin = Object("Children's Multivitamin", status="Available", parent=multivitamins)

mineral_supplements = Location("Mineral Supplements", parent=vitamins_section)
calcium = Object("Calcium", status="Available", parent=mineral_supplements)
magnesium = Object("Magnesium", status="Available", parent=mineral_supplements)

herbal_supplements = Location("Herbal Supplements", parent=vitamins_section)
echinacea = Object("Echinacea", status="Available", parent=herbal_supplements)
ginseng = Object("Ginseng", status="Available", parent=herbal_supplements)


