-- Updating Company_Email and Personal_Email columns

UPDATE Employee_Information 
SET 
    Company_Email = CONCAT(LOWER(LEFT(First_Name, 1)), 'x', LOWER(LEFT(Last_Name, 1)), RIGHT(EmployeeID, 3), '@dbmscorp.com');

UPDATE Employee_Information 
SET 
    Personal_Email = CONCAT(LOWER(First_Name), '.', LOWER(Last_Name), '@gmail.com');

-- Adding Punctuality column

UPDATE PerformanceMetrics 
SET Punctuality = Hours_Worked / (Days_in_cycle * 8);

-- Adding Efficiency column

UPDATE PerformanceMetrics 
SET Efficiency = Sales_Revenue / Hours_Worked;

-- Adding Norm_Efficiency column

UPDATE PerformanceMetrics AS pm
JOIN (SELECT MAX(Efficiency) AS max_efficiency FROM PerformanceMetrics) AS max_eff
SET pm.Norm_Efficiency = pm.Efficiency / max_eff.max_efficiency;

-- Adding Performance column

UPDATE PerformanceMetrics 
SET Performance = (Punctuality + Norm_Efficiency + Project_Completion_Rate) / 3;
