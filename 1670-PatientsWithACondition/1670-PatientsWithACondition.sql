-- Last updated: 10/11/2025, 9:50:42 AM
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'      
   OR conditions LIKE '% DIAB1%';  
