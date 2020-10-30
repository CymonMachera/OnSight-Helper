 """
Generate synthetic TB data

Most common symptoms occuring over 80% of the time (also halmark signs):
1. Cough for two weeks or more (productive)          99.5%
2. Night sweats                                      94%
3. Fever                                             93%
4. Weight loss                                       96%

Common symptoms occuring over 50% of the time
1. Chest pain                                        80%
2. Malaise                                           80%  
3. Difficulty                                        45%
4. Hemopysis                                         30%

Signs and their prevalences:
Malnourished -                                       80%
Increased Respiratory rate -                         45%
Reduced air entry/fluid filled lung -                50%            
Difficult Breathing                                  45%
Swell of Lymph nodes                                 25%

Risk Factors
1. Weakened immune system* (HIV) -                   62%
2. Having diabetes -                                 10%
3. Malnutrition (Low BMI) -                          58%
4. Recurrent infection of any kind -                 80%
5. Substance abuse                                   50%
6. Smoking                                           15% of female and 80% of male
7. Contact with TB                                   25%
8. History of TB in the family -                     80%   
9. Having Anaemia                                    88%   
10.Previous TB infection                             95%          

Gender distributions
Female -                                             31%
Male -                                               61%

Age distribution
< 2 years - 10%
2 - 16 years - 25%
16+ - 65%
---generary most of the TB patients are above the age of 16 years
   group the ages as : Age below 16 = 0, Age of 16+ = 1
   now Age below 16 =                                35%
        Age above 16 =                               65%
"""

# Import modules 
from scipy.stats import bernoulli, skewnorm, halfnorm
import csv
import random

random.seed(10)

#Make an assumption that the prevailance of TB is 50/50 to eliminate biasness
p = 0.5

#Generating ten thousand data points
N_records = 10000

#Generate Tb status
cases = bernoulli.rvs(p, size=N_records)


#A function to take the status of the patient and return the expected description of the patient
def generate_patients(status):

    """....most occuring sysmptoms........"""
    #coughing for more than two weeks
    cough_two_weeks = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.995)
   
    #Night sweats
    night_sweats = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.94)

    #Fever
    fever = bernoulli.rvs(0.4) if status == 0 else bernoulli.rvs(0.93)

    #Weight Loss
    weight_loss = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.96)

    """....common symptoms occuring .."""
    #chest pain
    chest_pain = bernoulli.rvs(0.2) if status == 0 else bernoulli.rvs(0.8)
    hemoptysis = bernoulli.rvs(0.05) if status == 0 else bernoulli.rvs(0.3)
    #Malaise
    malaise = bernoulli.rvs(0.2) if status == 0 else bernoulli.rvs(0.8)

    #difficult_breathing
    difficult_breathing = bernoulli.rvs(0.2) if status == 0 else bernoulli.rvs(0.45)

    swell_lymph_node = bernoulli.rvs(0.05) if status == 0 else bernoulli.rvs(0.25)

    
    """....signs and prevailence.."""
    reduced_air_entry = bernoulli.rvs(0.1) if status == 0 else bernoulli.rvs(0.5)

    Increased_respiratory_rate = bernoulli.rvs(0.2) if status == 0 else bernoulli.rvs(0.45)


    """....sex distribution..."""
    sex = bernoulli.rvs(0.31) if status == 0 else bernoulli.rvs(0.61)

    """...Age distribution.."""
    #The probability of having TB increases with an increase in age
    # Age below 16 = 0, Age of 16+ = 1
    age_above_16 = bernoulli.rvs(0.35) if status == 0 else bernoulli.rvs(0.65)
    """....Risk factors...."""
    # HIV status  positive = 1, negative = 0 
    hiv_status = bernoulli.rvs(0.05) if status == 0 else bernoulli.rvs(0.62)

    #Having anaemia
    anaemia_status = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.88)

    #diabetes status
    diabetes_status = bernoulli.rvs(0.8) if status == 0 else bernoulli.rvs(0.1)

    #Manutrition
    malnutrition = bernoulli.rvs(0.2) if status == 0 else bernoulli.rvs(0.58)
    
    #recurrent infections
    other_infection = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.8)

    #Substance abuse
    substance_abuse = bernoulli.rvs(0.2) if status == 0 else bernoulli.rvs(0.5)

    #smoking
    smoking = bernoulli.rvs(0.5) if sex == 1 else bernoulli.rvs(0.15) if status == 0 else bernoulli.rvs(0.8)

    #contact with tb patient before
    contact_tb_patient = bernoulli.rvs(0.1) if status == 0 else bernoulli.rvs(0.25)

    #family TB history
    family_tb = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.8)

    #Previous TB history
    previous_tb = bernoulli.rvs(0.3) if status == 0 else bernoulli.rvs(0.95)
    
    return [sex,age_above_16,previous_tb,contact_tb_patient,family_tb,smoking,substance_abuse,hiv_status,diabetes_status,anaemia_status,
    malnutrition,other_infection,cough_two_weeks,fever,hemoptysis,night_sweats,weight_loss,malaise,difficult_breathing,swell_lymph_node,
    reduced_air_entry,Increased_respiratory_rate,chest_pain,status]


print(f"Generating {N_records} synthetic patients ...")
# loop through the statuses and create new patients based on the status
patients = [generate_patients(x) for x in cases]


print("Patient genertion completed. Writing to file")
with open('sythentic_tb.csv', mode='w') as tb_file:
    tb_writer = csv.writer(tb_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    tb_writer.writerow(['sex','age_above_16','previous_tb','contact_tb_patient','family_tb','smoking','substance_abuse','hiv_status','diabetes_status',
    'anaemia_status','malnutrition','other_infection','cough_two_weeks','fever','hemoptysis','night_sweats','weight_loss','malaise',
    'difficult_breathing','swell_lymph_node','reduced_air_entry','Increased_respiratory_rate','chest_pain','status'])
    
    for patient in patients:
        tb_writer.writerow(patient)

print("Process completed")

