from django import forms
#from . import choices_processor


# Below data structure is used for the reason of a particular html response
# Example for reference ::
## ('option_value','option_name') --> in HTML
## Refer to our machine learning data
## The input data there is in lower case and _ separated hence we are doing this

processed = [('itching', 'Itching'), ('skin_rash', 'Skin rash'), ('nodal_skin_eruptions', 'Nodal skin eruptions'), ('continuous_sneezing', 'Continuous sneezing'), ('shivering', 'Shivering'), ('chills', 'Chills'), ('joint_pain', 'Joint pain'), ('stomach_pain', 'Stomach pain'), ('acidity', 'Acidity'), ('ulcers_on_tongue', 'Ulcers on tongue'), ('muscle_wasting', 'Muscle wasting'), ('vomiting', 'Vomiting'), ('burning_micturition', 'Burning micturition'), ('spotting_urination', 'Spotting urination'), ('fatigue', 'Fatigue'), ('weight_gain', 'Weight gain'), ('anxiety', 'Anxiety'), ('cold_hands_and_feets', 'Cold hands and feets'), ('mood_swings', 'Mood swings'), ('weight_loss', 'Weight loss'), ('restlessness', 'Restlessness'), ('lethargy', 'Lethargy'), ('patches_in_throat', 'Patches in throat'), ('irregular_sugar_level', 'Irregular sugar level'), ('cough', 'Cough'), ('high_fever', 'High fever'), ('sunken_eyes', 'Sunken eyes'), ('breathlessness', 'Breathlessness'), ('sweating', 'Sweating'), ('dehydration', 'Dehydration'), ('indigestion', 'Indigestion'), ('headache', 'Headache'), ('yellowish_skin', 'Yellowish skin'), ('dark_urine', 'Dark urine'), ('nausea', 'Nausea'), ('loss_of_appetite', 'Loss of appetite'), ('pain_behind_the_eyes', 'Pain behind the eyes'), ('back_pain', 'Back pain'), ('constipation', 'Constipation'), ('abdominal_pain', 'Abdominal pain'), ('diarrhoea', 'Diarrhoea'), ('mild_fever', 'Mild fever'), ('yellow_urine', 'Yellow urine'), ('yellowing_of_eyes', 'Yellowing of eyes'), ('acute_liver_failure', 'Acute liver failure'), ('fluid_overload', 'Fluid overload'), ('swelling_of_stomach', 'Swelling of stomach'), ('swelled_lymph_nodes', 'Swelled lymph nodes'), ('malaise', 'Malaise'), ('blurred_and_distorted_vision', 'Blurred and distorted vision'), ('phlegm', 'Phlegm'), ('throat_irritation', 'Throat irritation'), ('redness_of_eyes', 'Redness of eyes'), ('sinus_pressure', 'Sinus pressure'), ('runny_nose', 'Runny nose'), ('congestion', 'Congestion'), ('chest_pain', 'Chest pain'), ('weakness_in_limbs', 'Weakness in limbs'), ('fast_heart_rate', 'Fast heart rate'), ('pain_during_bowel_movements', 'Pain during bowel movements'), ('pain_in_anal_region', 'Pain in anal region'), ('bloody_stool', 'Bloody stool'), ('irritation_in_anus', 'Irritation in anus'), ('neck_pain', 'Neck pain'), ('dizziness', 'Dizziness'), ('cramps', 'Cramps'), ('bruising', 'Bruising'), ('obesity', 'Obesity'), ('swollen_legs', 'Swollen legs'), ('swollen_blood_vessels', 'Swollen blood vessels'), ('puffy_face_and_eyes', 'Puffy face and eyes'), ('enlarged_thyroid', 'Enlarged thyroid'), ('brittle_nails', 'Brittle nails'), ('swollen_extremeties', 'Swollen extremeties'), ('excessive_hunger', 'Excessive hunger'), ('extra_marital_contacts', 'Extra marital contacts'), ('drying_and_tingling_lips', 'Drying and tingling lips'), ('slurred_speech', 'Slurred speech'), ('knee_pain', 'Knee pain'), ('hip_joint_pain', 'Hip joint pain'), ('muscle_weakness', 'Muscle weakness'), ('stiff_neck', 'Stiff neck'), ('swelling_joints', 'Swelling joints'), ('movement_stiffness', 'Movement stiffness'), ('spinning_movements', 'Spinning movements'), ('loss_of_balance', 'Loss of balance'), ('unsteadiness', 'Unsteadiness'), ('weakness_of_one_body_side', 'Weakness of one body side'), ('loss_of_smell', 'Loss of smell'), ('bladder_discomfort', 'Bladder discomfort'), ('foul_smell_ofurine', 'Foul smell ofurine'), ('continuous_feel_of_urine', 'Continuous feel of urine'), ('passage_of_gases', 'Passage of gases'), ('internal_itching', 'Internal itching'), ('toxic_look_(typhos)', 'Toxic look (typhos)'), ('depression', 'Depression'), ('irritability', 'Irritability'), ('muscle_pain', 'Muscle pain'), ('altered_sensorium', 'Altered sensorium'), ('red_spots_over_body', 'Red spots over body'), ('belly_pain', 'Belly pain'), ('abnormal_menstruation', 'Abnormal menstruation'), ('dischromic_patches', 'Dischromic patches'), ('watering_from_eyes', 'Watering from eyes'), ('increased_appetite', 'Increased appetite'), ('polyuria', 'Polyuria'), ('family_history', 'Family history'), ('mucoid_sputum', 'Mucoid sputum'), ('rusty_sputum', 'Rusty sputum'), ('lack_of_concentration', 'Lack of concentration'), ('visual_disturbances', 'Visual disturbances'), ('receiving_blood_transfusion', 'Receiving blood transfusion'), ('receiving_unsterile_injections', 'Receiving unsterile injections'), ('coma', 'Coma'), ('stomach_bleeding', 'Stomach bleeding'), ('distention_of_abdomen', 'Distention of abdomen'), ('history_of_alcohol_consumption', 'History of alcohol consumption'), ('blood_in_sputum', 'Blood in sputum'), ('prominent_veins_on_calf', 'Prominent veins on calf'), ('palpitations', 'Palpitations'), ('painful_walking', 'Painful walking'), ('pus_filled_pimples', 'Pus filled pimples'), ('blackheads', 'Blackheads'), ('scurring', 'Scurring'), ('skin_peeling', 'Skin peeling'), ('silver_like_dusting', 'Silver like dusting'), ('small_dents_in_nails', 'Small dents in nails'), ('inflammatory_nails', 'Inflammatory nails'), ('blister', 'Blister'), ('red_sore_around_nose', 'Red sore around nose'), ('yellow_crust_ooze', 'Yellow crust ooze'), ('prognosis', 'Prognosis')]
processed.sort()

## The first choice in our HTML front end would be 'Leave if None' and the custom value for that is 'None'

CHOICES = [('None','Leave if None')]
CHOICES.extend(processed)

# Symptom input form made ::
# Our custom form class is inheriting django's in-built form class

class SymptomsForm(forms.Form):
    Symptom_1 = forms.ChoiceField(widget=forms.Select,choices=CHOICES)
    Symptom_2 = forms.ChoiceField(widget=forms.Select,choices=CHOICES)
    Symptom_3 = forms.ChoiceField(widget=forms.Select,choices=CHOICES)
    Symptom_4 = forms.ChoiceField(widget=forms.Select,choices=CHOICES)
    Symptom_5 = forms.ChoiceField(widget=forms.Select,choices=CHOICES)


    