-- creating the employee information table
drop database if exists salarymanagementsystemDB;
create database if not exists SalaryManagementSystemDB;
use SalaryManagementSystemDB;

-- in the find bar, use (1), (2), .... (15), to search for all the tables created
-- use Function #1,#2,... #5 for all the functions created
-- use Complex Query #1,#2,... #10 for all the Complex Queries Created
-- use Stored Procedure #1,#2,... #10 for all the Stored Procedures Created
-- use Trigger #1,#2,... #10 for all the Trigger Created


-- (1) Creation of Employee Information Table
CREATE table if not exists Employee_Information(
EmployeeID BIGINT NOT NULL, 
PRIMARY KEY (EmployeeID),
First_Name VARCHAR (255) NOT NULL,
Last_Name VARCHAR (255) NOT NULL,
DOB DATE NOT NULL,
Address VARCHAR (255) NOT NULL,
City VARCHAR (255) NOT NULL,
Zipcode INT NOT NULL,
Gender VARCHAR(255) NOT NULL,
Mobile VARCHAR(255) NOT NULL UNIQUE,
SSN BIGINT NOT NULL UNIQUE);


select * from Employee_Information;

-- adding records to the table
INSERT INTO Employee_Information VALUES (6320001500, 'Matthew', 'Pinkman', '1988-07-21', '7421, Frankford Road', 'Dallas', 75252, 'M', '+19724194308', 061263018);
INSERT INTO Employee_Information VALUES (6320001501, 'Bradley', 'Jesse', '1953-03-12', '7575, Frankford Road', 'Dallas', 75252, 'M', '+19724660382', 854577851);
INSERT INTO Employee_Information VALUES (6320001502, 'Vikas', 'Jain', '1972-10-25', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19729913129', 631157425);
INSERT INTO Employee_Information VALUES (6320001503, 'Kenny', 'Jacobs', '1988-02-21', '7650, McCallum Blvd', 'Dallas', 75252, 'M','+19724333343', 777407803);
INSERT INTO Employee_Information VALUES (6320001504, 'Anthony', 'Panthony', '1985-08-19', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19727609198', 316737348);
INSERT INTO Employee_Information VALUES (6320001505, 'Carol', 'Geller', '1997-04-21', '17817, Coit Road', 'Dallas', 75252, 'F','+19457992897', 637550444);
INSERT INTO Employee_Information VALUES (6320001506, 'Deepti', 'Singh', '1955-02-28', '430, Buckingham Road', 'Richardson', 75081, 'F','+19459102978', 255210843);
INSERT INTO Employee_Information VALUES (6320001507, 'Rahul', 'Dravid', '1963-08-18', '955 W President George Bush Hwy', 'Richardson', 75080,'M', '+19728878272', 151035862);
INSERT INTO Employee_Information VALUES (6320001508, 'Victor', 'Hughes', '1957-09-24', '800 W Renner Rd', 'Richardson', 75080, 'M','+19457539030', 758074466);
INSERT INTO Employee_Information VALUES (6320001509, 'Andrew', 'Pancholi', '1968-01-19', '430, Buckingham Road', 'Richardson', 75081, 'M','+19727113501', 354427067);
INSERT INTO Employee_Information VALUES (6320001510, 'Poonam', 'Sharma', '1985-07-05', '7720, McCallum Blvd', 'Dallas', 75252, 'F','+19450800157', 162421325);
INSERT INTO Employee_Information VALUES (6320001511, 'Priyanka', 'Jain', '1987-04-15', '430, Buckingham Road', 'Richardson', 75081, 'F','+19458233161', 104163176);
INSERT INTO Employee_Information VALUES (6320001512, 'Michelle', 'Hudat', '1970-01-25', '7421, Frankford Road', 'Dallas', 75080, 'F','+19722249471', 457448533);
INSERT INTO Employee_Information VALUES (6320001513, 'Moira', 'Rose', '1975-09-16', '3825, Mapleshade Ln', 'Plano', 75075, 'F','+19457346029', 241201418);
INSERT INTO Employee_Information VALUES (6320001514, 'Cranjis', 'McBasketball', '1967-04-23', '955 W President George Bush Hwy', 'Richardson', 75080, 'M','+19456302432', 616130660);
INSERT INTO Employee_Information VALUES (6320001515, 'Dr.Shrimp', 'Peurto Rico', '1996-10-24', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19724654009', 085887683);
INSERT INTO Employee_Information VALUES (6320001516, 'Sallu', 'Bhai', '1986-03-13', '955 W President George Bush Hwy', 'Richardson', 75080, 'M','+19726364092', 820253402);
INSERT INTO Employee_Information VALUES (6320001517, 'Ram', 'Lakhan', '1975-08-20', '7575, Frankford Road', 'Dallas', 75252, 'M','+19723312053', 544002401);
INSERT INTO Employee_Information VALUES (6320001518, 'Mota', 'Bhai', '1979-03-11', ' 7421, Frankford Road', 'Dallas', 75252, 'M','+19459781052', 850672025);
INSERT INTO Employee_Information VALUES (6320001519, 'Pablo', 'Escobar', '1958-02-13', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19452910731', 425684511);
INSERT INTO Employee_Information VALUES (6320001520, 'Vicky', 'Bhaiya', '1980-04-01', '430, Buckingham Road', 'Richardson', 75081, 'M','+19458432083', 133772062);
INSERT INTO Employee_Information VALUES (6320001521, 'Mark', 'Fischbach', '1997-05-28', '800 W Renner Rd', 'Richardson', 75080, 'M','+19453316831', 422045066);
INSERT INTO Employee_Information VALUES (6320001522, 'Dill', 'Funk', '1997-08-11', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19457171038', 880724382);
INSERT INTO Employee_Information VALUES (6320001523, 'Minty', 'Cherubandtug', '1980-03-17', '7575, Frankford Road', 'Dallas', 75252, 'F','+19457350905', 385680737);
INSERT INTO Employee_Information VALUES (6320001524, 'Mary', 'Beth Beth Beth', '1966-12-11', '17817, Coit Road', 'Dallas', 75252, 'F','+19455864296', 767667586);
INSERT INTO Employee_Information VALUES (6320001525, 'Helena', 'Bottom- Carter', '1954-10-24', '955 W President George Bush Hwy', 'Richardson', 75080, 'F','+19723009650', 350733572);
INSERT INTO Employee_Information VALUES (6320001526, 'Beefy', 'McWhatnow', '1996-01-20', '3825, Mapleshade Ln', 'Plano', 75075, 'F','+19727909333', 316827138);
INSERT INTO Employee_Information VALUES (6320001527, 'Captain', 'Melvin Seahorse', '1978-09-06', '17817, Coit Road', 'Dallas', 75252, 'M','+19451092867', 740175003);
INSERT INTO Employee_Information VALUES (6320001528, 'Simmy', 'Kantstandyourbitz', '1980-02-26', '7421, Frankford Road', 'Dallas', 75252, 'F','+19723315854', 801781388);
INSERT INTO Employee_Information VALUES (6320001529, 'Wandamian', 'Crucifixplate', '1981-06-05', '7421, Frankford Road', 'Dallas', 75252, 'M','+19720462109', 670641134);
INSERT INTO Employee_Information VALUES (6320001530, 'Denise', 'Fat', '1955-07-06', '955 W President George Bush Hwy', 'Richardson', 75080, 'F','+19458417102', 554516450);
INSERT INTO Employee_Information VALUES (6320001531, 'Jury', 'Prosciutto', '1953-08-13', '430, Buckingham Road', 'Richardson', 75081, 'M','+19450881439', 625771013);
INSERT INTO Employee_Information VALUES (6320001532, 'Rickyticky', 'Bobbywobbin', '1995-04-08', '800 W Renner Rd', 'Richardson', 75080, 'M','+19725840155', 851834861);
INSERT INTO Employee_Information VALUES (6320001533, 'Dadood', 'Frumcheers', '1992-07-08', '7650, McCallum Blvd', 'Dallas', 75252, 'M','+19454583523', 754524175);
INSERT INTO Employee_Information VALUES (6320001534, 'Avocarter', 'Hockey', '1980-08-10', '17817, Coit Road', 'Dallas', 75252, 'M','+19456379380', 306714500);
INSERT INTO Employee_Information VALUES (6320001535, 'Hungary', 'Denk', '1991-05-12', '7421, Frankford Road', 'Dallas', 75252, 'F','+19724476740', 280886874);
INSERT INTO Employee_Information VALUES (6320001536, 'Count', 'Ravioli', '1996-07-23', '7421, Frankford Road', 'Dallas', 75252, 'M','+19723988620', 417206012);
INSERT INTO Employee_Information VALUES (6320001537, 'Dungaresse', 'Weatherspoons', '1968-01-16', '7720, McCallum Blvd', 'Dallas', 75252, 'F','+19450735715', 112680632);
INSERT INTO Employee_Information VALUES (6320001538, 'Dusty', 'Shidiz', '1960-12-17', '800 W Renner Rd', 'Richardson', 75080, 'M','+19727783128', 144550405);
INSERT INTO Employee_Information VALUES (6320001539, 'Rachel', 'DaHubbahubba', '1950-01-12', '430, Buckingham Road', 'Richardson', 75081, 'F','+19456106005', 448508672);
INSERT INTO Employee_Information VALUES (6320001540, 'Tammy', 'Shehole', '1983-05-14', '7650, McCallum Blvd', 'Dallas', 75252, 'F','+19453512867', 515113828);
INSERT INTO Employee_Information VALUES (6320001541, 'Moist', 'Kite', '1960-06-18', '7575, Frankford Road', 'Dallas', 75252, 'F','+19455063608', 268887162);
INSERT INTO Employee_Information VALUES (6320001542, 'Chug-Chug', 'Pickles', '1986-07-14', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19454453144', 372817810);
INSERT INTO Employee_Information VALUES (6320001543, 'Stevia', 'Flunt', '1965-09-23', '3825, Mapleshade Ln', 'Plano', 75075, 'F','+19727708748', 422777671);
INSERT INTO Employee_Information VALUES (6320001544, 'Itmitebe', 'Decarbeurator', '1954-03-04', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19458811935', 386666667);
INSERT INTO Employee_Information VALUES (6320001545, 'Eyna', 'Mouthhole', '1985-11-14', '430, Buckingham Road', 'Richardson', 75081, 'F','+19727982979', 455834540);
INSERT INTO Employee_Information VALUES (6320001546, 'Melba', 'Moses Wolfenstein', '1982-09-07', '955 W President George Bush Hwy', 'Richardson', 75080, 'F','+19452785443', 634505740);
INSERT INTO Employee_Information VALUES (6320001547, 'Kiwi', 'Frankencop', '1960-06-13', '800 W Renner Rd', 'Richardson', 75080, 'F','+19455969957', 458811672);
INSERT INTO Employee_Information VALUES (6320001548, 'Glagadeen', 'Capisce', '1971-09-19', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19721843446', 740384805);
INSERT INTO Employee_Information VALUES (6320001549, 'Minty', 'Hummer', '1982-11-17', '3825, Mapleshade Ln', 'Plano', 75075, 'F','+19729623011', 202770821);
INSERT INTO Employee_Information VALUES (6320001550, 'Church', 'Pewpewpew', '1991-03-13', '17817, Coit Road', 'Dallas', 75252, 'M','+19721701409', 130622373);
INSERT INTO Employee_Information VALUES (6320001551, 'Coolie', 'Whistles', '1968-08-06', '955 W President George Bush Hwy', 'Richardson', 75080, 'M','+19725408847', 134534607);
INSERT INTO Employee_Information VALUES (6320001552, 'Disfatt', 'Bidge', '1996-07-14', '7421, Frankford Road', 'Dallas', 75252, 'F','+19724762155', 318025068);
INSERT INTO Employee_Information VALUES (6320001553, 'Diddy', 'Doodat', '1969-07-22', '7421, Frankford Road', 'Dallas', 75252, 'F','+19459261590', 711178825);
INSERT INTO Employee_Information VALUES (6320001554, 'Hummus', 'Queen', '1986-09-06', '7575, Frankford Road', 'Dallas', 75252, 'F','+19720640206', 625663260);
INSERT INTO Employee_Information VALUES (6320001555, 'Yanni', 'Van Halen', '1981-04-13', '7720, McCallum Blvd', 'Dallas', 75252, 'F','+19720586451', 645135567);
INSERT INTO Employee_Information VALUES (6320001556, 'Colonel', 'Hahahaha', '1958-03-07', '430, Buckingham Road', 'Richardson', 75081, 'M','+19728065340', 731365655);
INSERT INTO Employee_Information VALUES (6320001557, 'Jabreakit', 'Jubawdit', '1955-05-09', '800 W Renner Rd', 'Richardson', 75080, 'M','+19451448819', 825883635);
INSERT INTO Employee_Information VALUES (6320001558, 'Gregory', 'Popsicle', '1989-11-23', '17817, Coit Road', 'Dallas', 75252, 'M','+19728086543', 542342645);
INSERT INTO Employee_Information VALUES (6320001559, 'Stunk', 'Beagle', '1953-04-09', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19727845337', 052748671);
INSERT INTO Employee_Information VALUES (6320001560, 'Cowabunga', 'Peppermill', '1989-01-02', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19726375097', 420776844);
INSERT INTO Employee_Information VALUES (6320001561, 'Simmy', 'Kantstandyourbitz Jr.', '1959-09-19', '430, Buckingham Road', 'Richardson', 75081, 'F','+19724590166', 717483271);
INSERT INTO Employee_Information VALUES (6320001562, 'Henny', 'Cabbagehead', '1957-06-05', '800 W Renner Rd', 'Richardson', 75080, 'F','+19729391597', 120653367);
INSERT INTO Employee_Information VALUES (6320001563, 'Sharty', 'Waffles', '1973-04-16', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19450096461', 064638275);
INSERT INTO Employee_Information VALUES (6320001564, 'Secret Agent', 'Randy Beans', '1998-02-21', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19452345712', 422603242);
INSERT INTO Employee_Information VALUES (6320001565, 'Imafraid', 'Jumitbeeinnagang', '1980-12-18', '17817, Coit Road', 'Dallas', 75252, 'F','+19727805298', 613681023);
INSERT INTO Employee_Information VALUES (6320001566, 'Nabi', 'Cankles', '1990-12-23', '955 W President George Bush Hwy', 'Richardson', 75080, 'F','+19457653300', 717805213);
INSERT INTO Employee_Information VALUES (6320001567, 'Reverend', 'Donk Bonkers', '1956-09-22', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19721907275', 182018364);
INSERT INTO Employee_Information VALUES (6320001568, 'Real Hefty', 'Trout', '1992-08-13', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19455149253', 840540214);
INSERT INTO Employee_Information VALUES (6320001569, 'Eyeluvver', 'Butterdogsheds', '1961-04-14', '430, Buckingham Road', 'Richardson', 75081, 'M','+19724275450', 508555725);
INSERT INTO Employee_Information VALUES (6320001570, 'Jerry', 'Seinfeld', '1965-12-15', '800 W Renner Rd', 'Richardson', 75080, 'M','+19729169411', 216425844);
INSERT INTO Employee_Information VALUES (6320001571, 'Mark-Pat', 'Joe-Bill Dinosaur', '1950-08-22', '7421, Frankford Road', 'Dallas', 75252, 'M','+19720602579', 021254404);
INSERT INTO Employee_Information VALUES (6320001572, 'Wazda', 'Pocketchange', '1968-09-09', '3825, Mapleshade Ln', 'Plano', 75075, 'F','+19728295679', 308513288);
INSERT INTO Employee_Information VALUES (6320001573, 'Juanita', 'Indacaboosa', '1967-06-14', '7720, McCallum Blvd', 'Dallas', 75252, 'F','+19450502514', 027132843);
INSERT INTO Employee_Information VALUES (6320001574, 'Daniel Picnic Handsomes', 'US Coast Guard', '1961-05-04', '430, Buckingham Road', 'Richardson', 75081, 'M','+19728233196', 335746232);
INSERT INTO Employee_Information VALUES (6320001575, 'Heimlich', 'Manure', '1958-05-20', '800 W Renner Rd', 'Richardson', 75080, 'M','+19720133399', 342386473);
INSERT INTO Employee_Information VALUES (6320001576, 'Son', 'Ambulance', '1964-04-18', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19453868981', 468999999);
INSERT INTO Employee_Information VALUES (6320001577, 'Ita', 'Dapeeza', '1953-04-16', '955 W President George Bush Hwy', 'Richardson', 75080, 'F','+19452554289', 218111418);
INSERT INTO Employee_Information VALUES (6320001578, 'Old Fashioned', 'Handy', '1963-05-02', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19726348068', 645814066);
INSERT INTO Employee_Information VALUES (6320001579, 'Remo', 'Gatto', '1966-04-21', '7575, Frankford Road', 'Dallas', 75252, 'M','+19452658686', 115871772);
INSERT INTO Employee_Information VALUES (6320001580, 'Dusty', 'Scarole', '1992-10-07', '17817, Coit Road', 'Dallas', 75252, 'M','+19728286308', 832861620);
INSERT INTO Employee_Information VALUES (6320001581, 'High Priestess', 'Gabagool', '1976-01-05', '955 W President George Bush Hwy', 'Richardson', 75080, 'F','+19454880172', 500751484);
INSERT INTO Employee_Information VALUES (6320001582, 'Aunt', 'Tim', '1988-01-06', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19721169729', 238350635);
INSERT INTO Employee_Information VALUES (6320001583, 'Damn', 'Shawty', '1982-07-01', '3825, Mapleshade Ln', 'Plano', 75075, 'F','+19457122914', 100217102);
INSERT INTO Employee_Information VALUES (6320001584, 'Bicurious', 'George', '1995-07-19', '17817, Coit Road', 'Dallas', 75252, 'M','+19450569353', 307864371);
INSERT INTO Employee_Information VALUES (6320001585, 'Mort', 'Spandex', '1978-10-06', '7421, Frankford Road', 'Dallas', 75252, 'M','+19725515760', 048371606);
INSERT INTO Employee_Information VALUES (6320001586, 'Goose', 'Boils', '1982-11-21', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19729083617', 723757283);
INSERT INTO Employee_Information VALUES (6320001587, 'Cleo', 'Dookieslide', '1983-01-07', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19454855899', 513603365);
INSERT INTO Employee_Information VALUES (6320001588, 'Tristin', 'Mays', '1970-08-22', '955 W President George Bush Hwy', 'Richardson', 75080, 'M','+19451254833', 723255474);
INSERT INTO Employee_Information VALUES (6320001589, 'Fudgy', 'Perks', '1965-08-01', '3825, Mapleshade Ln', 'Plano', 75075, 'M','+19450900733', 850276325);
INSERT INTO Employee_Information VALUES (6320001590, 'Earl', 'Turlet', '1988-08-25', '7421, Frankford Road', 'Dallas', 75252, 'M','+19456900837', 786011232);
INSERT INTO Employee_Information VALUES (6320001591, 'Thighs', 'McPartland', '1993-10-10', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19723089409', 540474701);
INSERT INTO Employee_Information VALUES (6320001592, 'Flo', 'Jobb', '1999-02-09', '430, Buckingham Road', 'Richardson', 75081, 'F','+19452739159', 435355773);
INSERT INTO Employee_Information VALUES (6320001593, 'Keratine', 'Treatmentz', '1999-04-16', '7650, McCallum Blvd', 'Dallas', 75252, 'F','+19455916761', 770611545);
INSERT INTO Employee_Information VALUES (6320001594, 'Corky', 'Marinara', '1970-02-17', '430, Buckingham Road', 'Richardson', 75081, 'F','+19456895035', 414862275);
INSERT INTO Employee_Information VALUES (6320001595, 'Christine', 'Christina Whichizzit', '1973-07-25', '800 W Renner Rd', 'Richardson', 75080, 'F','+19454304503', 356573436);
INSERT INTO Employee_Information VALUES (6320001596, 'Professor Milk Duck', 'Ph.D', '1965-10-18', '7720, McCallum Blvd', 'Dallas', 75252, 'M','+19452691763', 518432268);
INSERT INTO Employee_Information VALUES (6320001597, 'Denzel', 'Washingmachine', '1972-01-17', '7575, Frankford Road', 'Dallas', 75252, 'M','+19454344268', 736610103);
INSERT INTO Employee_Information VALUES (6320001598, 'Tatianna', 'Ohnoyoudidnt', '1989-03-01', '7720, McCallum Blvd', 'Dallas', 75252, 'F','+19459030195', 101334165);
INSERT INTO Employee_Information VALUES (6320001599, 'Ono', 'Itscarl', '1997-08-23', '7575, Frankford Road', 'Dallas', 75252, 'M','+19729463965', 585468158);

-- SELECT COUNT(*) FROM Employee_Information;
SET SQL_SAFE_UPDATES = 0;


-- Complex Query #1
ALTER TABLE Employee_Information
ADD COLUMN Company_Email VARCHAR (255),
ADD COLUMN Personal_Email VARCHAR (255);

UPDATE Employee_Information 
SET Company_Email = CONCAT(LOWER(LEFT(First_Name, 1)), 'x', LOWER(LEFT(Last_Name, 1)), RIGHT(EmployeeID, 3), '@dbmscorp.com'),
Personal_Email = CONCAT(LOWER(First_Name), '.', LOWER(Last_Name), '@gmail.com');





SELECT * FROM Employee_Information;


-- (2) Schema for Performance Table
CREATE table if not exists PerformanceMetrics(
EmployeeID BIGINT NOT NULL, 
PerformanceID BIGINT NOT NULL,
Cycle_Start_Date Date NOT NULL,
Cycle_End_Date Date NOT NULL,
Days_in_cycle int NOT NULL,
Sales_Revenue INT,
Hours_Worked INT,
Project_Completion_Rate DECIMAL(3, 1) CHECK (Project_Completion_Rate >= 0 AND Project_Completion_Rate <= 1),
Milestones VARCHAR(255),
PRIMARY KEY (PerformanceID),
FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

INSERT INTO PerformanceMetrics(EmployeeID,PerformanceID,Cycle_Start_Date,Cycle_End_Date,Days_in_cycle,Sales_Revenue,Hours_Worked,Project_Completion_Rate,Milestones)
VALUES
(6320001500,1500008113,'2020-01-01','2020-03-31',90,30049,702,0.5,'Project kickoff meeting'),
(6320001500,1500381994,'2020-04-01','2020-06-30',90,39810,567,1,'Define project scope'),
(6320001500,1500357287,'2020-07-01','2020-09-30',91,30132,618.8,0.3,'Research target audience'),
(6320001500,1500279045,'2020-10-01','2020-12-31',91,40592,618.8,1,'Develop user personas'),
(6320001500,1500928137,'2021-01-01','2021-03-31',89,39100,676.4,0.8,'Conduct competitor analysis'),
(6320001500,1500860054,'2021-04-01','2021-06-30',90,38663,639,0.6,'Create content calendar'),
(6320001501,1501323043,'2020-01-01','2020-03-31',90,23089,621,1,'Design initial mockups'),
(6320001501,1501020412,'2020-04-01','2020-06-30',90,15406,612,1,'Write key website copy'),
(6320001501,1501804533,'2020-07-01','2020-09-30',91,28222,627.9,0.7,'Develop social media strategy'),
(6320001501,1501690405,'2020-10-01','2020-12-31',91,22856,655.2,1,'Secure project management tool'),
(6320001501,1501403169,'2021-01-01','2021-03-31',89,39260,676.4,1,'Schedule team brainstorming session'),
(6320001501,1501790081,'2021-04-01','2021-06-30',90,22986,585,0.5,'Finalize project timeline'),
(6320001502,1502287325,'2020-01-01','2020-03-31',90,23160,585,1,'Order necessary materials'),
(6320001502,1502493348,'2020-04-01','2020-06-30',90,33090,702,0.8,'Conduct market research survey'),
(6320001502,1502232364,'2020-07-01','2020-09-30',91,39873,637,0.6,'Book meeting with vendor'),
(6320001502,1502587780,'2020-10-01','2020-12-31',91,17312,627.9,0.8,'Develop training materials'),
(6320001502,1502375503,'2021-01-01','2021-03-31',89,48152,605.2,0.8,'Launch internal communication plan'),
(6320001502,1502542960,'2021-04-01','2021-06-30',90,35466,585,0.4,'Analyze competitor marketing strategy'),
(6320001503,1503139606,'2020-01-01','2020-03-31',90,28640,711,0.8,'Identify key performance indicators (KPIs)'),
(6320001503,1503010206,'2020-04-01','2020-06-30',90,30556,585,1,'Complete initial content draft'),
(6320001503,1503477027,'2020-07-01','2020-09-30',91,26527,728,1,'Gather stakeholder feedback'),
(6320001503,1503866825,'2020-10-01','2020-12-31',91,21204,682.5,0.2,'Refine design mockups'),
(6320001503,1503607623,'2021-01-01','2021-03-31',89,29370,649.7,0.5,'Schedule content creation meetings'),
(6320001503,1503631534,'2021-04-01','2021-06-30',90,20792,621,0.5,'Implement quality assurance checks'),
(6320001504,1504586029,'2020-01-01','2020-03-31',90,14295,657,0.6,'Prepare launch marketing campaign'),
(6320001504,1504172590,'2020-04-01','2020-06-30',90,43580,558,1,'Secure project budget approval'),
(6320001504,1504056312,'2020-07-01','2020-09-30',91,32475,664.3,0.8,'Onboard new team members'),
(6320001504,1504014415,'2020-10-01','2020-12-31',91,32532,564.2,1,'Develop risk management plan'),
(6320001504,1504668351,'2021-01-01','2021-03-31',89,21503,703.1,0.1,'Schedule client progress meeting'),
(6320001504,1504417184,'2021-04-01','2021-06-30',90,33480,549,1,'Conduct user testing sessions'),
(6320001505,1505725635,'2020-01-01','2020-03-31',90,25897,558,0.6,'Analyze user testing results'),
(6320001505,1505024339,'2020-01-01','2020-03-31',90,34529,711,0.5,'Revise content based on feedback'),
(6320001505,1505283944,'2020-04-01','2020-06-30',90,34526,648,0.3,'Finalize design for approval'),
(6320001505,1505012299,'2020-07-01','2020-09-30',91,11487,673.4,0.8,'Schedule content publishing dates'),
(6320001505,1505587780,'2020-10-01','2020-12-31',91,33357,700.7,0.4,'Set up social media automation tools'),
(6320001505,1505447366,'2021-01-01','2021-03-31',89,30102,560.7,0.9,'Monitor campaign performance'),
(6320001506,1506277238,'2021-04-01','2021-06-30',90,18468,720,1,'Track key performance indicators (KPIs)'),
(6320001506,1506673691,'2020-01-01','2020-03-31',90,41045,621,1,'Generate weekly status reports'),
(6320001506,1506162384,'2020-04-01','2020-06-30',90,18929,630,1,'Conduct team performance reviews'),
(6320001506,1506848546,'2020-07-01','2020-09-30',91,13157,728,1,'Resolve project roadblocks'),
(6320001506,1506513985,'2020-10-01','2020-12-31',91,13248,682.5,0.7,'Implement corrective actions'),
(6320001506,1506198715,'2021-01-01','2021-03-31',89,23654,560.7,0.2,'Celebrate project milestones'),
(6320001507,1507922942,'2021-04-01','2021-06-30',90,31950,657,0.3,'Finalize project deliverables'),
(6320001507,1507339269,'2020-01-01','2020-03-31',90,33993,567,0.4,'Conduct project post-mortem'),
(6320001507,1507304356,'2020-04-01','2020-06-30',90,37793,576,1,'Document lessons learned'),
(6320001507,1507904858,'2020-07-01','2020-09-30',91,30143,573.3,1,'Archive project materials'),
(6320001507,1507323150,'2020-10-01','2020-12-31',91,34864,573.3,0.3,'Develop client handover documentation'),
(6320001507,1507342441,'2021-01-01','2021-03-31',89,11395,605.2,0.8,'Schedule client training session'),
(6320001508,1508941543,'2021-04-01','2021-06-30',90,10756,630,0.5,'Secure client feedback and approval'),
(6320001508,1508120114,'2020-01-01','2020-03-31',90,29124,639,0.6,'Prepare final project invoice'),
(6320001508,1508030618,'2020-04-01','2020-06-30',90,42350,711,1,'Close out project files'),
(6320001508,1508760520,'2020-07-01','2020-09-30',91,43201,682.5,0.5,'Research industry trends'),
(6320001508,1508145870,'2020-10-01','2020-12-31',91,32376,673.4,1,'Identify new business opportunities'),
(6320001508,1508270578,'2021-01-01','2021-03-31',89,41694,605.2,0.1,'Develop new product concepts'),
(6320001509,1509284323,'2021-04-01','2021-06-30',90,19521,630,0.5,'Pitch ideas to decision makers'),
(6320001509,1509103888,'2020-01-01','2020-03-31',90,38219,621,0.7,'Secure funding for new projects'),
(6320001509,1509415710,'2020-04-01','2020-06-30',90,13912,720,0.3,'Recruit and hire top talent'),
(6320001509,1509300975,'2020-07-01','2020-09-30',91,30332,600.6,0.8,'Foster a positive work environment'),
(6320001509,1509058520,'2020-10-01','2020-12-31',91,35296,682.5,0.8,'Conduct employee engagement surveys'),
(6320001509,1509563426,'2021-01-01','2021-03-31',89,30308,667.5,0.5,'Invest in professional development'),
(6320001510,1510284323,'2021-04-01','2021-06-30',90,11246,612,0.3,'Implement continuous improvement processes'),
(6320001510,1510051944,'2020-01-01','2020-03-31',90,37143,594,0.3,'Streamline internal workflows'),
(6320001510,1510797071,'2020-01-01','2020-03-31',90,29846,558,0.3,'Develop communication best practices'),
(6320001510,1510469838,'2020-04-01','2020-06-30',90,27204,612,0.4,'Conduct team-building activities'),
(6320001510,1510672494,'2020-07-01','2020-09-30',91,41093,682.5,0.1,'Recognize and reward employee achievements'),
(6320001510,1510101765,'2020-10-01','2020-12-31',91,30948,673.4,0.3,'Host company social events'),
(6320001511,1511624154,'2021-01-01','2021-03-31',89,38852,694.2,0.7,'Track industry developments'),
(6320001511,1511771480,'2021-04-01','2021-06-30',90,34974,693,1,'Network with industry professionals'),
(6320001511,1511725635,'2020-01-01','2020-03-31',90,12645,594,0.7,'Attend relevant conferences and workshops'),
(6320001511,1511942774,'2020-04-01','2020-06-30',90,19895,558,0.5,'Stay informed on emerging technologies'),
(6320001511,1511565053,'2020-07-01','2020-09-30',91,13326,627.9,1,'Analyze market trends and data'),
(6320001511,1511969450,'2020-10-01','2020-12-31',91,41462,682.5,1,'Develop strategic business plans'),
(6320001512,1512270578,'2021-01-01','2021-03-31',89,34049,569.6,0.7,'Set clear and measurable goals'),
(6320001512,1512365812,'2021-04-01','2021-06-30',90,30802,720,0.3,'Delegate tasks effectively'),
(6320001512,1512884733,'2020-01-01','2020-03-31',90,23367,639,0.3,'Manage performance expectations'),
(6320001512,1512756880,'2020-04-01','2020-06-30',90,19367,567,0.6,'Provide constructive feedback'),
(6320001512,1512936572,'2020-07-01','2020-09-30',91,10195,582.4,0.7,'Motivate and inspire your team'),
(6320001512,1512690405,'2020-10-01','2020-12-31',91,15881,637,1,'Build strong client relationships'),
(6320001513,1513977730,'2021-01-01','2021-03-31',89,45303,712,1,'Exceed client expectations'),
(6320001513,1513162978,'2021-04-01','2021-06-30',90,10254,666,1,'Manage client expectations effectively'),
(6320001513,1513358761,'2020-01-01','2020-03-31',90,38106,666,1,'Resolve client concerns promptly'),
(6320001513,1513141972,'2020-04-01','2020-06-30',90,29206,675,0.6,'Communicate effectively with clients'),
(6320001513,1513212949,'2020-07-01','2020-09-30',91,11155,691.6,0.5,'Proactively address client needs'),
(6320001513,1513631885,'2020-10-01','2020-12-31',91,19459,618.8,1,'Foster long-term client relationships'),
(6320001514,1514104925,'2021-01-01','2021-03-31',89,23592,578.5,0.6,'Explore new market opportunities'),
(6320001514,1514930027,'2021-04-01','2021-06-30',90,10900,621,0.3,'Expand product and service offerings'),
(6320001514,1514534085,'2020-01-01','2020-03-31',90,31367,657,0.4,'Develop strategic partnerships'),
(6320001514,1514108256,'2020-04-01','2020-06-30',90,32856,639,1,'Negotiate contracts effectively'),
(6320001514,1514036897,'2020-07-01','2020-09-30',91,27462,673.4,1,'Increase brand awareness'),
(6320001514,1514631885,'2020-10-01','2020-12-31',91,40828,664.3,0.1,'Generate high-quality leads'),
(6320001515,1515386638,'2021-01-01','2021-03-31',89,37287,640.8,0.7,'Convert leads into paying customers'),
(6320001515,1515808682,'2021-04-01','2021-06-30',90,39924,675,1,'Improve customer retention rates'),
(6320001515,1515339269,'2020-01-01','2020-03-31',90,16576,558,0.5,'Optimize sales funnel processes'),
(6320001515,1515462649,'2020-01-01','2020-03-31',90,33455,675,0.7,'Increase return on investment (ROI)'),
(6320001515,1515327866,'2020-04-01','2020-06-30',90,32619,657,0.5,'Maintain a strong financial position'),
(6320001515,1515332689,'2020-07-01','2020-09-30',91,13890,609.7,0.3,'Manage cash flow effectively'),
(6320001516,1516984725,'2020-10-01','2020-12-31',91,38636,646.1,0.7,'Develop a sustainable business model'),
(6320001516,1516828608,'2021-01-01','2021-03-31',89,10391,667.5,0.5,'Adapt to changing market conditions'),
(6320001516,1516815767,'2021-04-01','2021-06-30',90,16774,711,1,'Make data-driven decisions'),
(6320001517,1517446423,'2020-01-01','2020-03-31',90,22907,585,0.5,'Embrace continuous learning'),
(6320001517,1517250228,'2020-04-01','2020-06-30',90,39076,675,0.3,'Foster a culture of innovation'),
(6320001517,1517672494,'2020-07-01','2020-09-30',91,24806,627.9,0.3,'Invest in research and development'),
(6320001517,1517690405,'2020-10-01','2020-12-31',91,37534,646.1,0.8,'Develop creative solutions to problems'),
(6320001517,1517491563,'2021-01-01','2021-03-31',89,18910,560.7,0.7,'Prototype development'),
(6320001517,1517897256,'2021-04-01','2021-06-30',90,10790,693,0.5,'User acceptance testing (UAT)'),
(6320001518,1518629860,'2020-01-01','2020-03-31',90,27255,576,0.3,'Secure domain name and hosting'),
(6320001518,1518865136,'2020-04-01','2020-06-30',90,41462,594,0.5,'Launch social media advertising campaign'),
(6320001518,1518848546,'2020-07-01','2020-09-30',91,18826,564.2,0.1,'Conduct influencer outreach'),
(6320001518,1518969450,'2020-10-01','2020-12-31',91,23922,691.6,1,'Onboard new clients'),
(6320001518,1518281713,'2021-01-01','2021-03-31',89,35770,605.2,1,'Designate project roles and responsibilities'),
(6320001518,1518170063,'2021-04-01','2021-06-30',90,32217,693,0.4,'Develop content style guide'),
(6320001519,1519586029,'2020-01-01','2020-03-31',90,22595,666,0.4,'Conduct keyword research'),
(6320001519,1519206306,'2020-04-01','2020-06-30',90,22767,666,1,'Optimize website for search engines (SEO)'),
(6320001519,1519269261,'2020-07-01','2020-09-30',91,19818,618.8,0.7,'Manage content distribution channels'),
(6320001519,1519175560,'2020-10-01','2020-12-31',91,32448,655.2,0.3,'Prepare for media outreach'),
(6320001519,1519961199,'2021-01-01','2021-03-31',89,32879,578.5,0.5,'Conduct internal knowledge-sharing session'),
(6320001519,1519727193,'2021-04-01','2021-06-30',90,11176,594,0.8,'Implement data security protocols'),
(6320001520,1520314930,'2020-01-01','2020-03-31',90,24840,684,0.5,'Conduct penetration testing'),
(6320001520,1520733370,'2020-04-01','2020-06-30',90,21968,657,0.3,'Prepare disaster recovery plan'),
(6320001520,1520433014,'2020-07-01','2020-09-30',91,16253,700.7,1,'Review legal contracts'),
(6320001520,1520690405,'2020-10-01','2020-12-31',91,46952,600.6,1,'Secure intellectual property rights'),
(6320001520,1520756745,'2021-01-01','2021-03-31',89,10651,587.4,0.5,'Conduct compliance audits'),
(6320001520,1520107175,'2021-04-01','2021-06-30',90,10624,612,0.6,'Negotiate vendor contracts'),
(6320001521,1521534085,'2020-01-01','2020-03-31',90,33775,702,0.5,'Manage project budget variances'),
(6320001521,1521374987,'2020-01-01','2020-03-31',90,11289,720,1,'Identify cost-saving opportunities'),
(6320001521,1521425916,'2020-04-01','2020-06-30',90,33874,612,0.7,'Prepare project budget reports'),
(6320001522,1522124923,'2020-07-01','2020-09-30',91,15220,591.5,1,'Streamline communication channels'),
(6320001522,1522323150,'2020-10-01','2020-12-31',91,33769,655.2,1,'Foster collaboration between teams'),
(6320001522,1522165653,'2021-01-01','2021-03-31',89,39385,685.3,1,'Manage stakeholder expectations'),
(6320001522,1522941543,'2021-04-01','2021-06-30',90,33788,621,1,'Conduct risk mitigation strategies'),
(6320001522,1522095775,'2020-01-01','2020-03-31',90,14650,684,1,'Prepare for project contingencies'),
(6320001522,1522996902,'2020-04-01','2020-06-30',90,14989,567,0.6,'Celebrate team wins'),
(6320001523,1523156637,'2020-07-01','2020-09-30',91,28581,664.3,0.3,'Host team appreciation events'),
(6320001523,1523925345,'2020-10-01','2020-12-31',91,43030,709.8,0.5,'Participate in industry awards programs'),
(6320001523,1523828608,'2021-01-01','2021-03-31',89,11927,578.5,0.6,'Develop thought leadership content'),
(6320001523,1523682906,'2021-04-01','2021-06-30',90,17514,567,0.3,'Publish industry white papers'),
(6320001523,1523112001,'2020-01-01','2020-03-31',90,27964,549,0.9,'Speak at industry events'),
(6320001523,1523240022,'2020-04-01','2020-06-30',90,15307,720,1,'Conduct market segmentation analysis'),
(6320001524,1524288676,'2020-07-01','2020-09-30',91,16576,609.7,1,'Identify customer pain points'),
(6320001524,1524058520,'2020-10-01','2020-12-31',91,40492,637,0.3,'Develop customer service protocols'),
(6320001524,1524696017,'2021-01-01','2021-03-31',89,38390,649.7,1,'Implement customer feedback loop'),
(6320001524,1524992915,'2021-04-01','2021-06-30',90,22061,585,1,'Analyze customer churn rate'),
(6320001524,1524849015,'2020-01-01','2020-03-31',90,20137,558,1,'Implement customer loyalty programs'),
(6320001524,1524361582,'2020-04-01','2020-06-30',90,21729,594,0.2,'Conduct competitor SWOT analysis (Strengths, Weaknesses, Opportunities, Threats)'),
(6320001525,1525049196,'2020-07-01','2020-09-30',91,16570,718.9,1,'Monitor social media sentiment'),
(6320001525,1525572505,'2020-10-01','2020-12-31',91,28515,591.5,0.8,'Analyze website traffic data'),
(6320001525,1525900471,'2021-01-01','2021-03-31',89,24289,640.8,0.8,'Develop A/B testing strategies'),
(6320001525,1525125776,'2021-04-01','2021-06-30',90,39602,711,1,'Refine user experience (UX) design'),
(6320001525,1525840902,'2020-01-01','2020-03-31',90,23285,639,0.8,'Implement accessibility features'),
(6320001525,1525952980,'2020-04-01','2020-06-30',90,46496,558,0.4,'Conduct website performance audits'),
(6320001526,1526728806,'2020-07-01','2020-09-30',91,34335,700.7,1,'Manage website uptime and performance'),
(6320001526,1526337565,'2020-10-01','2020-12-31',91,21985,618.8,0.4,'Integrate with third-party applications'),
(6320001526,1526535760,'2021-01-01','2021-03-31',89,15140,676.4,0.7,'Secure copyright for creative assets'),
(6320001527,1527657220,'2021-04-01','2021-06-30',90,16713,684,0.5,'Conduct copyright infringement check'),
(6320001527,1527358761,'2020-01-01','2020-03-31',90,15645,666,0.6,'Develop brand voice and messaging'),
(6320001527,1527725635,'2020-01-01','2020-03-31',90,37080,711,0.3,'Design brand style guide'),
(6320001527,1527327866,'2020-04-01','2020-06-30',90,40257,621,1,'Order promotional materials'),
(6320001527,1527068611,'2020-07-01','2020-09-30',91,29074,646.1,0.8,'Launch email marketing campaign'),
(6320001527,1527926205,'2020-10-01','2020-12-31',91,38995,728,0.7,'Design sales presentations'),
(6320001528,1528110321,'2021-01-01','2021-03-31',89,26452,560.7,0.8,'Conduct sales training sessions'),
(6320001528,1528834368,'2021-04-01','2021-06-30',90,24466,558,0.8,'Develop customer onboarding process'),
(6320001528,1528506480,'2020-01-01','2020-03-31',90,11472,639,0.7,' Manage customer support tickets'),
(6320001528,1528581192,'2020-04-01','2020-06-30',90,18806,576,0.6,' Conduct customer satisfaction surveys'),
(6320001528,1528961170,'2020-07-01','2020-09-30',91,14631,618.8,0.7,' Implement customer self-service options'),
(6320001528,1528146730,'2020-10-01','2020-12-31',91,37176,582.4,1,' Develop content for different platforms (e.g., blog, social media)'),
(6320001529,1529579957,'2021-01-01','2021-03-31',89,15362,640.8,1,' Schedule guest blog posts on industry publications'),
(6320001529,1529587247,'2021-04-01','2021-06-30',90,37118,675,0.2,' Manage online reputation'),
(6320001529,1529725635,'2020-01-01','2020-03-31',90,12810,576,1,' Respond to online reviews'),
(6320001529,1529800802,'2020-04-01','2020-06-30',90,14872,603,0.8,' Develop crisis communication plan'),
(6320001529,1529225248,'2020-07-01','2020-09-30',91,25811,564.2,0.3,' Conduct social media listening'),
(6320001529,1529646300,'2020-10-01','2020-12-31',91,28060,573.3,0.3,' Track brand mentions online'),
(6320001530,1530342441,'2021-01-01','2021-03-31',89,36297,605.2,0.8,' Develop social media community guidelines'),
(6320001530,1530347211,'2021-04-01','2021-06-30',90,32311,567,0.3,' Host live Q&A sessions on social media'),
(6320001530,1530550311,'2020-01-01','2020-03-31',90,47366,693,0.5,' Manage social media calendar'),
(6320001530,1530557682,'2020-04-01','2020-06-30',90,19952,684,0.8,' Create engaging social media content'),
(6320001530,1530376702,'2020-07-01','2020-09-30',91,10063,555.1,0.3,' Analyze social media engagement metrics'),
(6320001530,1530587780,'2020-10-01','2020-12-31',91,14904,637,0.3,' Optimize social media ad campaigns'),
(6320001531,1531696017,'2021-01-01','2021-03-31',89,27348,703.1,1,' Conduct competitor social media analysis'),
(6320001531,1531524359,'2021-04-01','2021-06-30',90,36205,693,0.4,' Develop sales pipeline management strategy'),
(6320001531,1531446423,'2020-01-01','2020-03-31',90,42516,576,0.7,' Qualify potential sales leads'),
(6320001532,1532811008,'2020-04-01','2020-06-30',90,36209,675,1,' Conduct sales demos and product presentations'),
(6320001532,1532420715,'2020-07-01','2020-09-30',91,13813,673.4,0.3,' Close sales deals and contracts'),
(6320001532,1532528400,'2020-10-01','2020-12-31',91,24189,709.8,0.5,' Secure customer testimonials'),
(6320001532,1532149122,'2021-01-01','2021-03-31',89,30814,694.2,1,' Develop case studies showcasing successful projects'),
(6320001532,1532011516,'2021-04-01','2021-06-30',90,11015,684,0.5,' Conduct competitor pricing analysis'),
(6320001532,1532024339,'2020-01-01','2020-03-31',90,11966,693,0.8,' Develop competitive pricing strategy'),
(6320001533,1533024339,'2020-01-01','2020-03-31',90,22759,657,0.5,' Implement financial reporting processes'),
(6320001533,1533767086,'2020-04-01','2020-06-30',90,23247,675,1,' Conduct financial forecasting and budgeting'),
(6320001533,1533980585,'2020-07-01','2020-09-30',91,10792,564.2,1,' Manage accounts payable and receivable'),
(6320001533,1533323150,'2020-10-01','2020-12-31',91,22309,682.5,1,' Streamline invoicing and payment processing'),
(6320001533,1533519229,'2021-01-01','2021-03-31',89,33389,703.1,1,' Conduct tax planning and compliance'),
(6320001533,1533188664,'2021-04-01','2021-06-30',90,35243,648,0.3,' Secure business insurance coverage'),
(6320001534,1534227268,'2020-01-01','2020-03-31',90,41899,648,0.7,' Conduct employee onboarding and training'),
(6320001534,1534844724,'2020-04-01','2020-06-30',90,39256,720,1,' Develop employee performance management system'),
(6320001534,1534200650,'2020-07-01','2020-09-30',91,42210,637,1,' Conduct performance reviews and evaluations'),
(6320001534,1534822720,'2020-10-01','2020-12-31',91,18196,700.7,0.4,' Implement employee wellness programs'),
(6320001534,1534137987,'2021-01-01','2021-03-31',89,25843,542.9,1,' Foster diversity and inclusion initiatives'),
(6320001534,1534391498,'2021-04-01','2021-06-30',90,24093,576,0.1,' Develop internal communication strategy'),
(6320001535,1535665578,'2020-01-01','2020-03-31',90,35815,594,1,' Conduct company-wide meetings'),
(6320001535,1535513760,'2020-04-01','2020-06-30',90,32622,720,0.3,' Implement internal communication tools (e.g., messaging app)'),
(6320001535,1535992884,'2020-07-01','2020-09-30',91,30687,637,0.7,' Host company retreats and team-building activities'),
(6320001535,1535881240,'2020-10-01','2020-12-31',91,43977,718.9,0.3,' Develop employee recognition programs'),
(6320001535,1535900471,'2021-01-01','2021-03-31',89,45403,623,0.2,' Conduct employee satisfaction surveys'),
(6320001535,1535594332,'2021-04-01','2021-06-30',90,24005,675,0.8,' Implement employee referral program'),
(6320001536,1536024339,'2020-01-01','2020-03-31',90,31744,693,0.5,' Conduct competitor product analysis'),
(6320001536,1536942774,'2020-04-01','2020-06-30',90,32124,711,0.7,' Identify product development opportunities'),
(6320001536,1536760520,'2020-07-01','2020-09-30',91,37780,637,1,' Develop product roadmap and development plan'),
(6320001537,1537704820,'2020-10-01','2020-12-31',91,33701,637,1,' Conduct product testing and iteration cycles'),
(6320001537,1537961199,'2021-01-01','2021-03-31',89,27274,569.6,0.3,' Gather user feedback on product prototypes'),
(6320001537,1537878655,'2021-04-01','2021-06-30',90,18056,693,1,' Implement product quality assurance processes'),
(6320001537,1537199663,'2020-01-01','2020-03-31',90,23707,711,0.4,' Develop product launch strategy'),
(6320001537,1537054128,'2020-04-01','2020-06-30',90,18341,702,0.1,' Launch new product or service offering'),
(6320001537,1537936572,'2020-07-01','2020-09-30',91,40714,673.4,0.8,' Conduct product training for sales and support teams'),
(6320001538,1538910930,'2020-10-01','2020-12-31',91,19387,700.7,0.6,' Develop product marketing materials'),
(6320001538,1538314775,'2021-01-01','2021-03-31',89,43465,694.2,0.3,' Analyze product performance and user adoption'),
(6320001538,1538461471,'2021-04-01','2021-06-30',90,42851,549,1,' Implement product bug fixes and updates'),
(6320001538,1538339269,'2020-01-01','2020-03-31',90,24192,693,1,' Develop customer support knowledge base'),
(6320001538,1538051944,'2020-01-01','2020-03-31',90,22210,585,0.8,' Conduct live chat support with customers'),
(6320001538,1538821214,'2020-04-01','2020-06-30',90,19227,711,0.7,' Offer phone and email support options'),
(6320001539,1539036897,'2020-07-01','2020-09-30',91,20044,618.8,0.5,' Develop self-service troubleshooting guides'),
(6320001539,1539513985,'2020-10-01','2020-12-31',91,16066,700.7,1,' Analyze customer support data to identify trends'),
(6320001539,1539988865,'2021-01-01','2021-03-31',89,42715,551.8,0.5,' Implement customer support escalation procedures'),
(6320001539,1539251552,'2021-04-01','2021-06-30',90,16202,585,1,' Conduct competitor sales analysis'),
(6320001539,1539964282,'2020-01-01','2020-03-31',90,20762,621,0.6,' Identify new sales channels and opportunities'),
(6320001539,1539361582,'2020-04-01','2020-06-30',90,37871,630,0.3,' Develop sales forecasting models'),
(6320001540,1540924273,'2020-07-01','2020-09-30',91,22006,591.5,0.8,' Analyze sales funnel performance'),
(6320001540,1540367255,'2020-10-01','2020-12-31',91,35759,682.5,0.3,' Implement sales automation tools'),
(6320001540,1540651820,'2021-01-01','2021-03-31',89,15883,560.7,0.7,' Conduct competitor marketing analysis'),
(6320001540,1540162978,'2021-04-01','2021-06-30',90,42829,567,0.4,' Identify new marketing channels and opportunities'),
(6320001540,1540884733,'2020-01-01','2020-03-31',90,18688,612,0.3,' Develop content marketing strategy'),
(6320001540,1540240022,'2020-04-01','2020-06-30',90,32775,639,1,' Partner with industry influencers'),
(6320001541,1541232364,'2020-07-01','2020-09-30',91,22763,664.3,1,' Analyze marketing campaign performance'),
(6320001541,1541014415,'2020-10-01','2020-12-31',91,11648,582.4,0.5,' Implement marketing attribution strategy'),
(6320001541,1541226381,'2021-01-01','2021-03-31',89,41769,712,0.7,' Conduct competitor customer service analysis'),
(6320001542,1542240036,'2021-04-01','2021-06-30',90,42194,594,0.7,' Identify new customer service channels'),
(6320001542,1542900959,'2020-01-01','2020-03-31',90,30879,657,0.3,' Develop customer service training programs'),
(6320001542,1542712958,'2020-04-01','2020-06-30',90,31466,702,0.7,' Conduct customer service call monitoring'),
(6320001542,1542628481,'2020-07-01','2020-09-30',91,39090,700.7,0.3,' Implement customer service performance metrics'),
(6320001542,1542072935,'2020-10-01','2020-12-31',91,36302,728,0.2,' Conduct competitor financial analysis'),
(6320001542,1542635289,'2021-01-01','2021-03-31',89,37669,649.7,1,' Identify new revenue streams'),
(6320001543,1543852969,'2021-04-01','2021-06-30',90,31121,702,1,' Develop cost reduction strategies'),
(6320001543,1543051944,'2020-01-01','2020-03-31',90,45879,621,0.3,' Implement financial controls'),
(6320001543,1543625114,'2020-04-01','2020-06-30',90,36951,657,0.7,' Conduct financial risk assessments'),
(6320001543,1543464728,'2020-07-01','2020-09-30',91,12814,627.9,0.8,' Develop contingency plans for financial disruptions'),
(6320001543,1543748925,'2020-10-01','2020-12-31',91,29135,728,0.5,' Conduct legal compliance audits'),
(6320001543,1543193319,'2021-01-01','2021-03-31',89,23420,605.2,0.5,' Develop data privacy policies and procedures'),
(6320001544,1544682906,'2021-04-01','2021-06-30',90,44840,720,0.5,' Implement data security measures'),
(6320001544,1544314930,'2020-01-01','2020-03-31',90,31431,612,0.2,' Conduct data breach response planning'),
(6320001544,1544769466,'2020-01-01','2020-03-31',90,29871,549,0.7,' Develop disaster recovery plan for IT infrastructure'),
(6320001544,1544767086,'2020-04-01','2020-06-30',90,17972,549,0.1,' Conduct regular IT infrastructure backups'),
(6320001544,1544056312,'2020-07-01','2020-09-30',91,40952,682.5,0.7,' Implement software updates and security patches'),
(6320001544,1544528400,'2020-10-01','2020-12-31',91,38996,664.3,0.7,' Conduct employee training on cybersecurity best practices'),
(6320001545,1545784411,'2021-01-01','2021-03-31',89,18575,712,1,'Conduct market validation surveys'),
(6320001545,1545284323,'2021-04-01','2021-06-30',90,26030,594,0.8,'Develop brand mascot and character design'),
(6320001545,1545076283,'2020-01-01','2020-03-31',90,15621,666,0.1,'Design user interface (UI) mockups'),
(6320001545,1545591398,'2020-04-01','2020-06-30',90,15921,549,1,'Develop user onboarding tutorials'),
(6320001545,1545804533,'2020-07-01','2020-09-30',91,28988,609.7,0.6,'Conduct accessibility audits'),
(6320001545,1545587780,'2020-10-01','2020-12-31',91,27521,682.5,0.8,'Prepare for search engine penalties'),
(6320001546,1546889336,'2021-01-01','2021-03-31',89,36352,614.1,0.2,'Manage online communities and forums'),
(6320001546,1546657220,'2021-04-01','2021-06-30',90,40475,666,1,'Partner with industry associations'),
(6320001546,1546506480,'2020-01-01','2020-03-31',90,29283,684,1,'Secure sponsorships for relevant events'),
(6320001547,1547361582,'2020-04-01','2020-06-30',90,15223,639,1,'Develop a content repurposing strategy'),
(6320001547,1547080910,'2020-07-01','2020-09-30',91,11767,609.7,0.2,'Schedule podcast interviews and guest appearances'),
(6320001547,1547234080,'2020-10-01','2020-12-31',91,23427,682.5,1,'Conduct competitive content analysis'),
(6320001547,1547651820,'2021-01-01','2021-03-31',89,42687,560.7,1,'Implement content performance tracking metrics'),
(6320001547,1547568646,'2021-04-01','2021-06-30',90,14894,693,0.4,'Design gated content for lead generation'),
(6320001547,1547944790,'2020-01-01','2020-03-31',90,36539,585,0.3,'Develop an email marketing automation strategy'),
(6320001548,1548723164,'2020-04-01','2020-06-30',90,15741,639,0.9,'Conduct A/B testing on email campaigns'),
(6320001548,1548005183,'2020-07-01','2020-09-30',91,29000,627.9,1,'Analyze email click-through and open rates'),
(6320001548,1548690405,'2020-10-01','2020-12-31',91,28843,637,0.3,'Implement email deliverability best practices'),
(6320001548,1548872805,'2021-01-01','2021-03-31',89,26563,640.8,0.6,'Conduct competitor sales training analysis'),
(6320001548,1548568646,'2021-04-01','2021-06-30',90,11943,630,0.3,'Develop objection handling strategies for sales calls'),
(6320001548,1548410705,'2020-01-01','2020-03-31',90,25130,630,0.3,'Implement sales lead nurturing campaigns'),
(6320001549,1549898852,'2020-04-01','2020-06-30',90,13501,594,0.8,'Track sales team performance metrics'),
(6320001549,1549344988,'2020-07-01','2020-09-30',91,18078,709.8,1,'Develop sales compensation plans'),
(6320001549,1549720095,'2020-10-01','2020-12-31',91,23090,646.1,1,'Conduct competitor marketing automation analysis'),
(6320001549,1549314775,'2021-01-01','2021-03-31',89,34586,658.6,0.3,'Implement marketing automation workflows'),
(6320001549,1549321525,'2021-04-01','2021-06-30',90,36588,702,0.3,'Develop retargeting campaigns for website visitors'),
(6320001549,1549139606,'2020-01-01','2020-03-31',90,42336,702,1,'Conduct social media sentiment analysis by region'),
(6320001550,1550068170,'2020-01-01','2020-03-31',90,17164,666,0.5,'Analyze website traffic sources'),
(6320001550,1550196100,'2020-04-01','2020-06-30',90,36634,684,0.4,'Develop user journey maps'),
(6320001550,1550508741,'2020-07-01','2020-09-30',91,13306,600.6,0.7,'Conduct website heatmap analysis'),
(6320001550,1550969450,'2020-10-01','2020-12-31',91,33349,673.4,1,'Implement website personalization strategies'),
(6320001550,1550209850,'2021-01-01','2021-03-31',89,42213,569.6,0.3,'Conduct competitor customer loyalty program analysis'),
(6320001550,1550480072,'2021-04-01','2021-06-30',90,13870,594,1,'Develop customer loyalty program tiers and rewards'),
(6320001551,1551076283,'2020-01-01','2020-03-31',90,25450,585,0.9,'Partner with other businesses for cross-promotions'),
(6320001551,1551338072,'2020-04-01','2020-06-30',90,36502,648,0.7,'Implement customer segmentation strategies'),
(6320001551,1551225248,'2020-07-01','2020-09-30',91,25874,627.9,0.5,'Develop targeted marketing campaigns based on segments'),
(6320001552,1552279045,'2020-10-01','2020-12-31',91,23279,673.4,1,'Conduct competitor financial reporting analysis'),
(6320001552,1552723683,'2021-01-01','2021-03-31',89,25361,551.8,0.7,'Implement financial controls for expense management'),
(6320001552,1552321525,'2021-04-01','2021-06-30',90,17872,603,1,'Develop budgeting variance analysis reports'),
(6320001552,1552446423,'2020-01-01','2020-03-31',90,14563,549,0.2,'Conduct cash flow forecasting'),
(6320001552,1552844724,'2020-04-01','2020-06-30',90,13276,594,1,'Implement financial stress testing'),
(6320001552,1552924273,'2020-07-01','2020-09-30',91,30603,573.3,0.7,'Participate in industry research studies'),
(6320001553,1553057660,'2020-10-01','2020-12-31',91,24967,600.6,1,'Conduct competitor legal compliance analysis'),
(6320001553,1553137987,'2021-01-01','2021-03-31',89,41797,712,0.5,'Develop data governance policies'),
(6320001553,1553435785,'2021-04-01','2021-06-30',90,27434,558,1,'Conduct employee exit interviews'),
(6320001553,1553936677,'2020-01-01','2020-03-31',90,32975,720,0.3,'Implement employee retention strategies'),
(6320001553,1553712958,'2020-04-01','2020-06-30',90,28255,621,1,'Conduct competitor product testing analysis'),
(6320001553,1553068611,'2020-07-01','2020-09-30',91,22858,618.8,0.5,'Implement product user experience (UX) testing'),
(6320001554,1554117040,'2020-10-01','2020-12-31',91,37202,555.1,1,'Develop a product feedback loop system'),
(6320001554,1554314775,'2021-01-01','2021-03-31',89,45368,649.7,0.8,'Analyze product usage data to identify trends'),
(6320001554,1554790081,'2021-04-01','2021-06-30',90,30910,720,0.3,'Implement product roadmap adjustments based on feedback'),
(6320001554,1554928564,'2020-01-01','2020-03-31',90,36140,567,1,'Conduct market research for new product features'),
(6320001554,1554317660,'2020-04-01','2020-06-30',90,33422,711,0.8,'Develop product explainer videos'),
(6320001554,1554244663,'2020-07-01','2020-09-30',91,27168,682.5,0.5,'Prepare sales collateral for different product offerings'),
(6320001555,1555793030,'2020-10-01','2020-12-31',91,15157,700.7,0.5,'Analyze product return on investment (ROI)'),
(6320001555,1555254047,'2021-01-01','2021-03-31',89,43827,551.8,1,'Implement a product lifecycle management strategy'),
(6320001555,1555295839,'2021-04-01','2021-06-30',90,14931,558,1,'Conduct competitor customer support training analysis'),
(6320001555,1555060057,'2020-01-01','2020-03-31',90,25564,603,0.3,'Develop customer support escalation procedures for complex issues'),
(6320001555,1555665578,'2020-01-01','2020-03-31',90,30557,603,0.5,'Implement customer self-service knowledge base search functionality'),
(6320001555,1555074540,'2020-04-01','2020-06-30',90,22959,603,0.2,'Conduct customer service agent training on empathy and communication skills'),
(6320001556,1556697092,'2020-07-01','2020-09-30',91,34826,564.2,0.9,'Analyze customer support call recordings to identify improvement areas'),
(6320001556,1556970310,'2020-10-01','2020-12-31',91,29254,609.7,0.9,'Develop a knowledge sharing program for customer support agents'),
(6320001556,1556563426,'2021-01-01','2021-03-31',89,29625,596.3,0.1,'Conduct competitor financial risk assessment analysis'),
(6320001557,1557985830,'2021-04-01','2021-06-30',90,11218,648,0.3,'Implement cybersecurity awareness training programs for employees'),
(6320001557,1557051944,'2020-01-01','2020-03-31',90,28527,675,0.5,'Conduct penetration testing of internal systems'),
(6320001557,1557689448,'2020-04-01','2020-06-30',90,29644,576,0.1,'Develop a vendor risk management strategy'),
(6320001557,1557005183,'2020-07-01','2020-09-30',91,23267,718.9,1,'Conduct business continuity planning for operational disruptions'),
(6320001557,1557558090,'2020-10-01','2020-12-31',91,23638,564.2,0.5,'Implement data encryption protocols'),
(6320001557,1557370107,'2021-01-01','2021-03-31',89,30882,578.5,1,'Conduct regular data backups across multiple locations'),
(6320001558,1558542960,'2021-04-01','2021-06-30',90,41339,621,1,'Update employee handbooks and policies'),
(6320001558,1558498367,'2020-01-01','2020-03-31',90,13851,630,1,'Conduct performance management training for team leaders'),
(6320001558,1558327866,'2020-04-01','2020-06-30',90,36506,702,0.5,'Organize team-building activities based on employee interests'),
(6320001558,1558181235,'2020-07-01','2020-09-30',91,43979,709.8,0.5,'Implement employee recognition programs for specific achievements'),
(6320001558,1558161145,'2020-10-01','2020-12-31',91,11677,718.9,1,'Conduct employee engagement surveys throughout the year'),
(6320001558,1558651820,'2021-01-01','2021-03-31',89,28199,667.5,0.3,'Host employee appreciation lunches or dinners'),
(6320001559,1559498673,'2021-04-01','2021-06-30',90,40071,612,1,'Conduct competitor industry trends analysis'),
(6320001559,1559418818,'2020-01-01','2020-03-31',90,20633,684,1,'Identify emerging technologies relevant to the industry'),
(6320001559,1559932568,'2020-04-01','2020-06-30',90,33690,621,1,'Develop a future-of-work strategy'),
(6320001559,1559408416,'2020-07-01','2020-09-30',91,26435,646.1,0.8,'Conduct scenario planning for potential market disruptions'),
(6320001559,1559381670,'2020-10-01','2020-12-31',91,38406,655.2,0.1,'Analyze the impact of social, economic, political, technological (SEPT) factors'),
(6320001559,1559077259,'2021-01-01','2021-03-31',89,18829,703.1,0.5,'Develop a company social responsibility (CSR) program'),
(6320001560,1560302924,'2021-04-01','2021-06-30',90,20282,648,0.9,'Partner with charitable organizations for community outreach'),
(6320001560,1560490254,'2020-01-01','2020-03-31',90,10495,666,0.7,'Develop a sustainability strategy for environmental impact reduction'),
(6320001560,1560405504,'2020-04-01','2020-06-30',90,17242,594,0.5,'Track and report on key sustainability metrics'),
(6320001560,1560433014,'2020-07-01','2020-09-30',91,38245,664.3,0.7,'Conduct employee training on sustainable practices'),
(6320001560,1560925345,'2020-10-01','2020-12-31',91,40277,573.3,0.5,'Develop brand storytelling elements'),
(6320001560,1560961199,'2021-01-01','2021-03-31',89,44157,685.3,0.3,'Design social media profile graphics'),
(6320001561,1561100090,'2021-04-01','2021-06-30',90,32920,612,0.4,'Optimize website loading speed'),
(6320001561,1561227268,'2020-01-01','2020-03-31',90,49532,711,0.5,'Conduct competitor link-building strategies analysis'),
(6320001561,1561016226,'2020-01-01','2020-03-31',90,11773,630,0.4,'Implement guest blogging outreach program'),
(6320001562,1562986696,'2020-04-01','2020-06-30',90,13511,666,0.3,'Manage online reputation during crisis situations'),
(6320001562,1562256962,'2020-07-01','2020-09-30',91,44497,700.7,0.1,'Monitor brand mentions in news articles'),
(6320001562,1562646300,'2020-10-01','2020-12-31',91,29304,673.4,0.3,'Develop social media community management guidelines'),
(6320001562,1562519229,'2021-01-01','2021-03-31',89,32818,703.1,0.5,'Host live product demonstrations on social media'),
(6320001562,1562030117,'2021-04-01','2021-06-30',90,20282,594,0.2,'Manage social media content calendar for different platforms'),
(6320001562,1562199663,'2020-01-01','2020-03-31',90,33468,639,0.7,'Create visually appealing infographics and data visualizations'),
(6320001563,1563844724,'2020-04-01','2020-06-30',90,32146,621,0.3,'Analyze social media engagement metrics across platforms'),
(6320001563,1563056312,'2020-07-01','2020-09-30',91,14167,618.8,0.4,'Develop social media influencer marketing campaigns'),
(6320001563,1563455465,'2020-10-01','2020-12-31',91,10449,582.4,0.3,'Conduct competitor sales pipeline management analysis'),
(6320001563,1563430835,'2021-01-01','2021-03-31',89,32467,605.2,1,'Qualify leads based on budget and buying stage'),
(6320001563,1563207265,'2021-04-01','2021-06-30',90,41121,702,0.5,'Develop sales scripts for different customer segments'),
(6320001563,1563797071,'2020-01-01','2020-03-31',90,21636,666,0.8,'Close up-sell and cross-sell opportunities'),
(6320001564,1564250228,'2020-04-01','2020-06-30',90,40841,702,0.4,'Secure customer referrals through incentive programs'),
(6320001564,1564640780,'2020-07-01','2020-09-30',91,24144,627.9,0.2,'Develop case studies showcasing successful customer implementations'),
(6320001564,1564351980,'2020-10-01','2020-12-31',91,40447,573.3,1,'Analyze competitor pricing strategies across product tiers'),
(6320001564,1564563426,'2021-01-01','2021-03-31',89,30348,605.2,0.7,'Implement dynamic pricing strategies based on market demand'),
(6320001564,1564542960,'2021-04-01','2021-06-30',90,15217,648,1,'Conduct financial ratio analysis for business health assessment'),
(6320001564,1564032452,'2020-01-01','2020-03-31',90,26322,639,0.6,'Generate financial statements for stakeholders'),
(6320001565,1565976490,'2020-04-01','2020-06-30',90,37713,648,0.7,'Manage accounts payable and receivable reconciliation'),
(6320001565,1565968286,'2020-07-01','2020-09-30',91,24630,627.9,1,'Automate repetitive financial tasks through software'),
(6320001565,1565808305,'2020-10-01','2020-12-31',91,19067,655.2,0.4,'Conduct tax compliance reviews'),
(6320001565,1565226381,'2021-01-01','2021-03-31',89,33576,685.3,0.7,'Secure intellectual property rights for inventions or designs'),
(6320001565,1565144377,'2021-04-01','2021-06-30',90,31910,657,0.5,'Develop onboarding program for new hires by department'),
(6320001565,1565147719,'2020-01-01','2020-03-31',90,12113,702,0.3,'Implement mentorship programs for employee development'),
(6320001566,1566821214,'2020-04-01','2020-06-30',90,45570,612,0.7,'Conduct leadership training programs for managers'),
(6320001566,1566256962,'2020-07-01','2020-09-30',91,26378,573.3,0.3,'Organize employee wellness workshops (e.g., stress management)'),
(6320001566,1566145870,'2020-10-01','2020-12-31',91,24731,655.2,1,'Foster a culture of open communication and feedback'),
(6320001567,1567298244,'2021-01-01','2021-03-31',89,42761,631.9,0.3,'Develop internal communication channels for specific teams'),
(6320001567,1567542960,'2021-04-01','2021-06-30',90,25791,621,0.6,'Conduct department-specific meetings'),
(6320001567,1567717522,'2020-01-01','2020-03-31',90,39574,621,0.3,'Implement employee recognition programs for teamwork'),
(6320001568,1568155832,'2020-01-01','2020-03-31',90,22006,657,1,'Analyze employee satisfaction survey results and address concerns'),
(6320001568,1568669036,'2020-04-01','2020-06-30',90,15998,657,0.2,'Develop employee engagement initiatives based on survey feedback'),
(6320001568,1568256962,'2020-07-01','2020-09-30',91,24222,582.4,1,'Conduct competitor product development analysis by feature'),
(6320001568,1568513985,'2020-10-01','2020-12-31',91,10911,637,0.1,'Partner with universities or research institutions for innovation'),
(6320001568,1568740214,'2021-01-01','2021-03-31',89,40640,703.1,1,'Develop product minimum viable product (MVP) for initial testing'),
(6320001568,1568100090,'2021-04-01','2021-06-30',90,20350,585,0.4,'Conduct user interviews to gather product feedback'),
(6320001569,1569068170,'2020-01-01','2020-03-31',90,25004,684,1,'Develop product user guides and documentation'),
(6320001569,1569425916,'2020-04-01','2020-06-30',90,27361,693,0.5,'Implement bug bounty program for security researchers'),
(6320001569,1569093209,'2020-07-01','2020-09-30',91,45602,655.2,0.6,'Develop product launch marketing campaign materials'),
(6320001569,1569513985,'2020-10-01','2020-12-31',91,40186,637,0.3,'Conduct product training webinars for customers'),
(6320001569,1569237516,'2021-01-01','2021-03-31',89,39691,596.3,0.8,'Analyze product performance metrics across user segments'),
(6320001569,1569505758,'2021-04-01','2021-06-30',90,14023,630,0.2,'Implement product A/B testing for feature optimization'),
(6320001570,1570279212,'2020-01-01','2020-03-31',90,39264,639,1,'Develop customer support knowledge base search optimization'),
(6320001570,1570074540,'2020-04-01','2020-06-30',90,28227,702,1,'Offer live chat support with personalized greetings'),
(6320001570,1570056312,'2020-07-01','2020-09-30',91,16025,600.6,0.5,'Provide multilingual customer support options'),
(6320001570,1570249355,'2020-10-01','2020-12-31',91,17243,673.4,1,'Conduct customer satisfaction surveys after support interactions'),
(6320001570,1570430835,'2021-01-01','2021-03-31',89,18829,676.4,1,'Analyze customer support data to identify pain points'),
(6320001570,1570384413,'2021-04-01','2021-06-30',90,37811,720,0.1,'Develop self-service troubleshooting guides with visuals'),
(6320001571,1571542198,'2020-01-01','2020-03-31',90,48847,594,1,'Conduct competitor sales channel analysis'),
(6320001571,1571898852,'2020-04-01','2020-06-30',90,26943,639,0.4,'Identify new sales opportunities through strategic partnerships'),
(6320001571,1571584468,'2020-07-01','2020-09-30',91,13095,673.4,0.7,'Develop sales forecasting models by product or region'),
(6320001571,1571014415,'2020-10-01','2020-12-31',91,32975,718.9,0.8,'Analyze sales funnel conversion rates at each stage'),
(6320001571,1571475032,'2021-01-01','2021-03-31',89,32957,667.5,0.8,'Implement lead scoring system for prioritizing leads'),
(6320001571,1571480072,'2021-04-01','2021-06-30',90,11152,558,0.6,'Conduct competitor marketing channel analysis by platform'),
(6320001572,1572964282,'2020-01-01','2020-03-31',90,22907,612,1,'Implement content marketing strategy for different buyer personas'),
(6320001572,1572909058,'2020-04-01','2020-06-30',90,34884,567,1,'Develop co-branded marketing campaigns with industry partners'),
(6320001572,1572376702,'2020-07-01','2020-09-30',91,31488,609.7,0.3,'Conduct influencer marketing outreach program targeting relevant niches'),
(6320001573,1573925345,'2020-10-01','2020-12-31',91,40053,718.9,0.7,'Analyze marketing campaign performance across channels'),
(6320001573,1573723683,'2021-01-01','2021-03-31',89,45115,649.7,0.7,'Develop marketing attribution model to track campaign effectiveness'),
(6320001573,1573834368,'2021-04-01','2021-06-30',90,27393,639,0.1,'Conduct competitor customer service channel analysis'),
(6320001573,1573103888,'2020-01-01','2020-03-31',90,18180,612,0.7,'Implement live chat support with wait time estimates'),
(6320001573,1573813297,'2020-01-01','2020-03-31',90,22120,639,0.3,'Develop customer service training programs on product knowledge'),
(6320001573,1573260434,'2020-04-01','2020-06-30',90,27050,666,0.2,'Conduct customer service call quality monitoring'),
(6320001574,1574521040,'2020-07-01','2020-09-30',91,32658,618.8,1,'Implement customer service satisfaction surveys'),
(6320001574,1574690405,'2020-10-01','2020-12-31',91,33902,564.2,0.5,'Conduct competitor financial risk management analysis'),
(6320001574,1574237516,'2021-01-01','2021-03-31',89,42190,676.4,1,'Develop risk mitigation strategies for potential financial threats'),
(6320001574,1574030117,'2021-04-01','2021-06-30',90,23405,558,0.7,'Implement internal controls for expense approval processes'),
(6320001574,1574446423,'2020-01-01','2020-03-31',90,11635,558,1,'Conduct financial stress testing for different economic scenarios'),
(6320001574,1574601604,'2020-04-01','2020-06-30',90,17250,594,0.5,'Develop contingency plans for currency fluctuations'),
(6320001575,1575420715,'2020-07-01','2020-09-30',91,35344,709.8,0.4,'Conduct market research for emerging technologies'),
(6320001575,1575146730,'2020-10-01','2020-12-31',91,11094,564.2,0.2,'Conduct competitor legal compliance training analysis'),
(6320001575,1575298244,'2021-01-01','2021-03-31',89,11907,667.5,0.5,'Develop data breach notification protocols'),
(6320001575,1575498673,'2021-04-01','2021-06-30',90,22803,720,1,'Conduct employee background checks for security purposes'),
(6320001575,1575016226,'2020-01-01','2020-03-31',90,25697,558,1,'Develop a disaster recovery plan for employee data'),
(6320001575,1575557682,'2020-04-01','2020-06-30',90,12021,639,1,'Implement physical security measures for IT equipment'),
(6320001576,1576968286,'2020-07-01','2020-09-30',91,41764,673.4,0.2,'Conduct data encryption for sensitive customer information'),
(6320001576,1576367255,'2020-10-01','2020-12-31',91,22798,627.9,0.8,'Automate data backups with version control'),
(6320001576,1576331306,'2021-01-01','2021-03-31',89,34251,712,1,'Develop employee training programs on data privacy regulations'),
(6320001576,1576657220,'2021-04-01','2021-06-30',90,16125,684,0.7,'Conduct employee training on social media best practices'),
(6320001576,1576717522,'2020-01-01','2020-03-31',90,22600,639,0.6,' Identify new customer service channels'),
(6320001576,1576800802,'2020-04-01','2020-06-30',90,25955,693,0.8,' Develop customer service training programs'),
(6320001577,1577848546,'2020-07-01','2020-09-30',91,45525,700.7,1,' Conduct customer service call monitoring'),
(6320001577,1577881240,'2020-10-01','2020-12-31',91,30577,637,0.6,' Implement customer service performance metrics'),
(6320001577,1577226381,'2021-01-01','2021-03-31',89,25857,685.3,0.5,' Conduct competitor financial analysis'),
(6320001578,1578897256,'2021-04-01','2021-06-30',90,35166,702,1,' Identify new revenue streams'),
(6320001578,1578155832,'2020-01-01','2020-03-31',90,24620,585,0.6,' Develop cost reduction strategies'),
(6320001578,1578601604,'2020-04-01','2020-06-30',90,17001,558,0.3,' Implement financial controls'),
(6320001578,1578137222,'2020-07-01','2020-09-30',91,29640,564.2,0.5,' Conduct financial risk assessments'),
(6320001578,1578778615,'2020-10-01','2020-12-31',91,36970,682.5,0.8,' Develop contingency plans for financial disruptions'),
(6320001578,1578430835,'2021-01-01','2021-03-31',89,12013,658.6,0.6,' Conduct legal compliance audits'),
(6320001579,1579612933,'2021-04-01','2021-06-30',90,18679,675,0.5,' Develop data privacy policies and procedures'),
(6320001579,1579147719,'2020-01-01','2020-03-31',90,39847,675,0.5,' Implement data security measures'),
(6320001579,1579279212,'2020-01-01','2020-03-31',90,13747,567,0.3,' Conduct data breach response planning'),
(6320001579,1579283944,'2020-04-01','2020-06-30',90,10243,630,0.5,' Develop disaster recovery plan for IT infrastructure'),
(6320001579,1579225248,'2020-07-01','2020-09-30',91,42748,691.6,1,' Conduct regular IT infrastructure backups'),
(6320001579,1579190835,'2020-10-01','2020-12-31',91,36829,646.1,0.7,' Implement software updates and security patches'),
(6320001580,1580242912,'2021-01-01','2021-03-31',89,29147,623,0.3,' Conduct employee training on cybersecurity best practices'),
(6320001580,1580384413,'2021-04-01','2021-06-30',90,25766,675,0.9,'Conduct market validation surveys'),
(6320001580,1580534085,'2020-01-01','2020-03-31',90,31916,567,0.6,'Develop brand mascot and character design'),
(6320001580,1580020412,'2020-04-01','2020-06-30',90,39860,639,0.3,'Design user interface (UI) mockups'),
(6320001580,1580565053,'2020-07-01','2020-09-30',91,13090,564.2,0.3,'Develop user onboarding tutorials'),
(6320001580,1580146730,'2020-10-01','2020-12-31',91,13343,618.8,0.7,'Conduct accessibility audits'),
(6320001581,1581767880,'2021-01-01','2021-03-31',89,34606,685.3,1,'Prepare for search engine penalties'),
(6320001581,1581107175,'2021-04-01','2021-06-30',90,17670,612,0.5,'Manage online communities and forums'),
(6320001581,1581366874,'2020-01-01','2020-03-31',90,21688,693,0.5,'Partner with industry associations'),
(6320001581,1581537270,'2020-04-01','2020-06-30',90,33220,621,0.3,'Secure sponsorships for relevant events'),
(6320001581,1581464728,'2020-07-01','2020-09-30',91,34027,609.7,1,'Develop a content repurposing strategy'),
(6320001581,1581984725,'2020-10-01','2020-12-31',91,15618,709.8,0.8,'Schedule podcast interviews and guest appearances'),
(6320001582,1582237516,'2021-01-01','2021-03-31',89,10906,667.5,1,'Conduct competitive content analysis'),
(6320001582,1582790081,'2021-04-01','2021-06-30',90,37001,657,1,'Implement content performance tracking metrics'),
(6320001582,1582076283,'2020-01-01','2020-03-31',90,45966,621,0.7,'Design gated content for lead generation'),
(6320001583,1583756880,'2020-04-01','2020-06-30',90,20750,675,0.7,'Develop an email marketing automation strategy'),
(6320001583,1583596767,'2020-07-01','2020-09-30',91,26589,682.5,0.3,'Conduct A/B testing on email campaigns'),
(6320001583,1583013555,'2020-10-01','2020-12-31',91,41366,718.9,0.5,'Analyze email click-through and open rates'),
(6320001583,1583370107,'2021-01-01','2021-03-31',89,20890,623,0.9,'Implement email deliverability best practices'),
(6320001583,1583170063,'2021-04-01','2021-06-30',90,46935,594,0.7,'Conduct competitor sales training analysis'),
(6320001583,1583498367,'2020-01-01','2020-03-31',90,16674,603,0.2,'Develop objection handling strategies for sales calls'),
(6320001584,1584304356,'2020-04-01','2020-06-30',90,32547,666,0.5,'Implement sales lead nurturing campaigns'),
(6320001584,1584156637,'2020-07-01','2020-09-30',91,19907,700.7,0.3,'Track sales team performance metrics'),
(6320001584,1584631885,'2020-10-01','2020-12-31',91,33597,709.8,0.1,'Develop sales compensation plans'),
(6320001584,1584767880,'2021-01-01','2021-03-31',89,15415,623,1,'Conduct competitor marketing automation analysis'),
(6320001584,1584852969,'2021-04-01','2021-06-30',90,11126,720,1,'Implement marketing automation workflows'),
(6320001584,1584462649,'2020-01-01','2020-03-31',90,30001,558,0.5,'Develop retargeting campaigns for website visitors'),
(6320001585,1585183437,'2020-01-01','2020-03-31',90,15276,720,0.3,'Conduct social media sentiment analysis by region'),
(6320001585,1585283944,'2020-04-01','2020-06-30',90,17177,657,0.3,'Analyze website traffic sources'),
(6320001585,1585980585,'2020-07-01','2020-09-30',91,36233,682.5,0.6,'Develop user journey maps'),
(6320001585,1585866825,'2020-10-01','2020-12-31',91,23411,627.9,0.8,'Conduct website heatmap analysis'),
(6320001585,1585767880,'2021-01-01','2021-03-31',89,39256,596.3,0.8,'Implement website personalization strategies'),
(6320001585,1585428700,'2021-04-01','2021-06-30',90,44495,639,0.9,'Conduct competitor customer loyalty program analysis'),
(6320001586,1586964282,'2020-01-01','2020-03-31',90,21100,702,0.5,'Develop customer loyalty program tiers and rewards'),
(6320001586,1586327866,'2020-04-01','2020-06-30',90,21110,549,0.9,'Partner with other businesses for cross-promotions'),
(6320001586,1586112624,'2020-07-01','2020-09-30',91,22766,627.9,1,'Implement customer segmentation strategies'),
(6320001586,1586234080,'2020-10-01','2020-12-31',91,13101,673.4,1,'Develop targeted marketing campaigns based on segments'),
(6320001586,1586845139,'2021-01-01','2021-03-31',89,24664,712,0.5,'Conduct competitor financial reporting analysis'),
(6320001586,1586062888,'2021-04-01','2021-06-30',90,29845,693,1,'Implement financial controls for expense management'),
(6320001587,1587051944,'2020-01-01','2020-03-31',90,35489,585,0.6,'Develop budgeting variance analysis reports'),
(6320001587,1587459632,'2020-04-01','2020-06-30',90,34357,585,0.4,'Conduct cash flow forecasting'),
(6320001587,1587829131,'2020-07-01','2020-09-30',91,45058,673.4,0.8,'Implement financial stress testing'),
(6320001588,1588351980,'2020-10-01','2020-12-31',91,36376,682.5,0.5,'Participate in industry research studies'),
(6320001588,1588165653,'2021-01-01','2021-03-31',89,26276,694.2,0.9,'Conduct competitor legal compliance analysis'),
(6320001588,1588480072,'2021-04-01','2021-06-30',90,15160,666,0.8,'Develop data governance policies'),
(6320001588,1588594142,'2020-01-01','2020-03-31',90,42269,666,0.8,'Conduct employee exit interviews'),
(6320001588,1588294150,'2020-04-01','2020-06-30',90,16545,549,0.9,'Implement employee retention strategies'),
(6320001588,1588640780,'2020-07-01','2020-09-30',91,39725,609.7,0.8,'Conduct competitor product testing analysis'),
(6320001589,1589455465,'2020-10-01','2020-12-31',91,48284,673.4,0.3,'Implement product user experience (UX) testing'),
(6320001589,1589121456,'2021-01-01','2021-03-31',89,29243,631.9,0.5,'Develop a product feedback loop system'),
(6320001589,1589391498,'2021-04-01','2021-06-30',90,16294,675,0.8,'Analyze product usage data to identify trends'),
(6320001589,1589383100,'2020-01-01','2020-03-31',90,14275,711,1,'Implement product roadmap adjustments based on feedback'),
(6320001589,1589294150,'2020-04-01','2020-06-30',90,10506,567,0.3,'Conduct market research for new product features'),
(6320001589,1589917157,'2020-07-01','2020-09-30',91,40856,700.7,1,'Develop product explainer videos'),
(6320001590,1590616610,'2020-10-01','2020-12-31',91,30006,555.1,0.4,'Prepare sales collateral for different product offerings'),
(6320001590,1590104925,'2021-01-01','2021-03-31',89,42648,694.2,1,'Analyze product return on investment (ROI)'),
(6320001590,1590727193,'2021-04-01','2021-06-30',90,48003,675,0.2,'Implement a product lifecycle management strategy'),
(6320001590,1590884733,'2020-01-01','2020-03-31',90,19577,720,0.7,'Conduct competitor customer support training analysis'),
(6320001590,1590227268,'2020-01-01','2020-03-31',90,39139,612,0.8,'Develop customer support escalation procedures for complex issues'),
(6320001590,1590381994,'2020-04-01','2020-06-30',90,37513,657,0.7,'Implement customer self-service knowledge base search functionality'),
(6320001591,1591376702,'2020-07-01','2020-09-30',91,32380,555.1,1,'Conduct customer service agent training on empathy and communication skills'),
(6320001591,1591926205,'2020-10-01','2020-12-31',91,27734,664.3,1,'Analyze customer support call recordings to identify improvement areas'),
(6320001591,1591447366,'2021-01-01','2021-03-31',89,13812,542.9,0.1,'Develop a knowledge sharing program for customer support agents'),
(6320001591,1591985830,'2021-04-01','2021-06-30',90,15921,666,0.4,'Conduct competitor financial risk assessment analysis'),
(6320001591,1591383100,'2020-01-01','2020-03-31',90,32658,621,0.5,'Implement cybersecurity awareness training programs for employees'),
(6320001591,1591821214,'2020-04-01','2020-06-30',90,25357,657,0.3,'Conduct penetration testing of internal systems'),
(6320001592,1592344988,'2020-07-01','2020-09-30',91,21805,627.9,0.8,'Develop a vendor risk management strategy'),
(6320001592,1592469880,'2020-10-01','2020-12-31',91,15590,655.2,0.8,'Conduct business continuity planning for operational disruptions'),
(6320001592,1592563426,'2021-01-01','2021-03-31',89,38693,551.8,0.5,'Implement data encryption protocols'),
(6320001593,1593808682,'2021-04-01','2021-06-30',90,26764,630,0.5,'Conduct regular data backups across multiple locations'),
(6320001593,1593717522,'2020-01-01','2020-03-31',90,31613,576,0.3,'Update employee handbooks and policies'),
(6320001593,1593922362,'2020-04-01','2020-06-30',90,48811,585,0.5,'Conduct performance management training for team leaders'),
(6320001593,1593005183,'2020-07-01','2020-09-30',91,24414,646.1,1,'Organize team-building activities based on employee interests'),
(6320001593,1593543675,'2020-10-01','2020-12-31',91,45291,564.2,1,'Implement employee recognition programs for specific achievements'),
(6320001593,1593242912,'2021-01-01','2021-03-31',89,42251,542.9,1,'Conduct employee engagement surveys throughout the year'),
(6320001594,1594941543,'2021-04-01','2021-06-30',90,36127,684,0.4,'Host employee appreciation lunches or dinners'),
(6320001594,1594207776,'2020-01-01','2020-03-31',90,17924,675,0.7,'Conduct competitor industry trends analysis'),
(6320001594,1594152178,'2020-04-01','2020-06-30',90,12985,693,1,'Identify emerging technologies relevant to the industry'),
(6320001594,1594137222,'2020-07-01','2020-09-30',91,32015,573.3,0.3,'Develop a future-of-work strategy'),
(6320001594,1594910930,'2020-10-01','2020-12-31',91,17514,728,0.6,'Conduct scenario planning for potential market disruptions'),
(6320001594,1594077259,'2021-01-01','2021-03-31',89,35206,560.7,0.6,'Analyze the impact of social, economic, political, technological (SEPT) factors'),
(6320001595,1595568646,'2021-04-01','2021-06-30',90,43139,720,0.3,'Develop a company social responsibility (CSR) program'),
(6320001595,1595155832,'2020-01-01','2020-03-31',90,35069,684,1,'Finalize project timeline'),
(6320001595,1595625114,'2020-04-01','2020-06-30',90,39837,693,1,'Order necessary materials'),
(6320001595,1595684793,'2020-07-01','2020-09-30',91,28328,618.8,1,'Conduct market research survey'),
(6320001595,1595013555,'2020-10-01','2020-12-31',91,41883,637,0.3,'Book meeting with vendor'),
(6320001595,1595972334,'2021-01-01','2021-03-31',89,12379,658.6,0.6,'Develop training materials'),
(6320001596,1596081489,'2021-04-01','2021-06-30',90,20627,657,0.3,'Launch internal communication plan'),
(6320001596,1596972395,'2020-01-01','2020-03-31',90,16093,720,0.4,'Analyze competitor marketing strategy'),
(6320001596,1596900959,'2020-01-01','2020-03-31',90,32163,675,0.6,'Identify key performance indicators (KPIs)'),
(6320001596,1596966284,'2020-04-01','2020-06-30',90,33159,558,0.8,'Complete initial content draft'),
(6320001596,1596357287,'2020-07-01','2020-09-30',91,23307,664.3,0.4,'Gather stakeholder feedback'),
(6320001596,1596101765,'2020-10-01','2020-12-31',91,17137,618.8,1,'Refine design mockups'),
(6320001597,1597331306,'2021-01-01','2021-03-31',89,33639,640.8,1,'Schedule content creation meetings'),
(6320001597,1597347211,'2021-04-01','2021-06-30',90,34768,648,1,'Implement quality assurance checks'),
(6320001597,1597884733,'2020-01-01','2020-03-31',90,24493,720,0.5,'Prepare launch marketing campaign'),
(6320001598,1598635320,'2020-04-01','2020-06-30',90,15693,558,0.6,'Secure project budget approval'),
(6320001598,1598401300,'2020-07-01','2020-09-30',91,43016,646.1,0.8,'Onboard new team members'),
(6320001598,1598955035,'2020-10-01','2020-12-31',91,33255,637,0.8,'Develop risk management plan'),
(6320001598,1598961199,'2021-01-01','2021-03-31',89,16619,578.5,0.5,'Schedule client progress meeting'),
(6320001598,1598985830,'2021-04-01','2021-06-30',90,30245,693,0.6,'Conduct user testing sessions'),
(6320001598,1598717522,'2020-01-01','2020-03-31',90,36185,657,1,'Analyze user testing results'),
(6320001599,1599898852,'2020-04-01','2020-06-30',90,27129,567,0.5,'Revise content based on feedback'),
(6320001599,1599332689,'2020-07-01','2020-09-30',91,43072,564.2,0.3,'Finalize design for approval'),
(6320001599,1599720095,'2020-10-01','2020-12-31',91,49607,600.6,0.5,'Schedule content publishing dates'),
(6320001599,1599049593,'2021-01-01','2021-03-31',89,14927,631.9,0.5,'Set up social media automation tools'),
(6320001599,1599897256,'2021-04-01','2021-06-30',90,28470,558,1,'Monitor campaign performance'),
(6320001599,1599542198,'2020-01-01','2020-03-31',90,18826,657,0.8,'Track key performance indicators (KPIs)');

Select * from performancemetrics;
-- drop table performancemetrics;

-- Complex Query #2
ALTER TABLE performancemetrics
ADD COLUMN Punctuality Decimal(3,2),
ADD COLUMN efficiency Decimal(4,2),
ADD COLUMN norm_efficiency Decimal(3,2),
ADD COLUMN performance Decimal(3,2);

UPDATE performancemetrics
SET punctuality = Hours_Worked/(Days_in_cycle*8),
efficiency = Sales_Revenue/Hours_Worked;
UPDATE performancemetrics as pm
JOIN (SELECT MAX(efficiency) AS max_efficiency FROM performancemetrics) AS max_eff
SET pm.norm_efficiency = pm.efficiency / max_eff.max_efficiency;
update performancemetrics set performance=(punctuality+norm_efficiency+project_completion_rate)/3;


-- (3) Schema for Review Table
-- drop table Review;
CREATE table if not exists Review(
ReviewID BIGINT NOT NULL PRIMARY KEY,
EmployeeID BIGINT NOT NULL,
 ReviewerID BIGINT NOT NULL,
 ReviewDate DATE NOT NULL,
 ReviewPeriod VARCHAR(255),
 PerformanceRatings DECIMAL (5,2),
 GoalsTargets VARCHAR(255), 
 Strengths VARCHAR(255),
 AreasForImprovement VARCHAR(255),
 ActionableSteps VARCHAR(255),
 TrainingDevelopmentNeeds VARCHAR(255),
 CareerAspirations VARCHAR(255),
 OverallAssessment VARCHAR(255),
FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);



INSERT INTO Review (ReviewID,EmployeeID, ReviewerID,ReviewDate, ReviewPeriod, PerformanceRatings, GoalsTargets, Strengths, AreasForImprovement, ActionableSteps, TrainingDevelopmentNeeds, CareerAspirations, OverallAssessment)
VALUES
(565,6320001500,6320001867,'2021-11-14','2021 Annual Review',4.6,'Exceeds Expectations','Leadership Skills','Time Management','Set clear and achievable performance goals with the employee.','Leadership skills development','Obtain a leadership role within the company.','Exceeds expectations in all key performance areas.'),
(739,6320001501,6320001731,'2021-10-08','2021 Annual Review',2.8,'Below Expectations','Team Collaboration','Communication Skills (Written/Verbal)','Provide regular feedback on their performance.','Effective communication training','Lead a cross-functional team on a major project.','Demonstrates exceptional leadership qualities.'),
(471,6320001502,6320001810,'2021-10-03','2021 Annual Review',4,'Meets Expectations','Problem-Solving Abilities','Leadership Development','Recognize and celebrate their achievements.','Conflict resolution techniques','Attain proficiency in a new technology or skill.','Consistently delivers high-quality work.'),
(775,6320001503,6320001799,'2021-11-23','2021 Annual Review',4.8,'Exceeds Expectations','Adaptability','Conflict Resolution','Identify areas for improvement and create action plans to address them.','Emotional intelligence enhancement','Become a subject matter expert in a specific area.','Effectively collaborates with team members.'),
(696,6320001504,6320001738,'2021-12-13','2021 Annual Review',3.1,'Below Expectations','Time Management','Emotional Intelligence','Encourage ongoing learning and development opportunities.','Time management workshops','Earn a promotion to a higher level position.','Displays strong problem-solving skills.'),
(547,6320001505,6320001882,'2021-09-14','2021 Annual Review',5,'Exceeds Expectations','Decision Making','Adaptability to Change','Offer mentorship and coaching to support their growth.','Project management training','Manage a department or division within the organization.','Communicates effectively with colleagues and stakeholders.'),
(474,6320001506,6320001768,'2021-10-06','2021 Annual Review',4.9,'Exceeds Expectations','Creativity','Stress Management','Conduct performance evaluations based on predefined criteria.','Decision-making skills refinement','Represent the company at industry conferences or events.','Shows a high level of adaptability to change.'),
(758,6320001507,6320001878,'2021-11-08','2021 Annual Review',2.5,'Below Expectations','Strategic Thinking','Networking Abilities','Discuss career aspirations and provide guidance on advancement opportunities.','Team building and collaboration workshops','Spearhead a company-wide initiative or program.','Takes initiative to drive positive outcomes.'),
(792,6320001508,6320001748,'2021-11-06','2021 Annual Review',4.4,'Meets Expectations','Communication Skills','Decision-Making Skills','Provide resources and support to help them succeed in their role.','Adaptability to change training','Transition into a different department or role.','Provides valuable insights and innovative ideas.'),
(518,6320001509,6320001832,'2021-10-08','2021 Annual Review',2.7,'Below Expectations','Conflict Resolution','Presentation Skills','Foster a positive work environment that promotes collaboration and innovation.','Stress management seminars','Gain international work experience.','Maintains a positive and professional attitude.'),
(677,6320001510,6320001828,'2021-11-18','2021 Annual Review',2.8,'Below Expectations','Innovation','Problem-Solving Techniques','Encourage participation in training programs and workshops.','Technical skills enhancement programs','Complete advanced education or certification.','Exemplifies the companys core values in actions.'),
(419,6320001511,6320001887,'2021-12-01','2021 Annual Review',3,'Below Expectations','Project Management','Technical Proficiency Enhancement','Establish regular check-ins to track progress and address any concerns.','Sales and negotiation training','Develop and launch a new product or service.','Successfully meets or exceeds all performance targets.'),
(793,6320001512,6320001749,'2021-12-12','2021 Annual Review',4.8,'Exceeds Expectations','Attention to Detail','Team Collaboration','Encourage self-reflection and goal-setting.','Customer service excellence workshops','Secure a mentorship or coaching relationship with a senior leader.','Demonstrates excellent time management skills.'),
(737,6320001513,6320001773,'2021-11-21','2021 Annual Review',2.2,'Below Expectations','Analytical Thinking','Attention to Detail','Recognize and address any barriers to their success.','Presentation and public speaking skills development','Receive recognition as an industry thought leader.','Shows a commitment to ongoing learning and development.'),
(455,6320001514,6320001694,'2021-09-20','2021 Annual Review',4.7,'Exceeds Expectations','Customer Focus','Strategic Planning','Provide constructive feedback on specific tasks and projects.','Problem-solving techniques refinement','Lead a successful merger or acquisition project.','Builds strong relationships with clients and customers.'),
(779,6320001515,6320001847,'2021-12-18','2021 Annual Review',4.7,'Exceeds Expectations','Technical Proficiency','Project Management Techniques','Encourage peer feedback and collaboration.','Strategic planning and execution training','Start a mentorship program within the organization.','Displays resilience in challenging situations.'),
(619,6320001516,6320001776,'2021-11-25','2021 Annual Review',4.6,'Exceeds Expectations','Emotional Intelligence','Creativity and Innovation','Offer opportunities for cross-functional training and projects.','Financial literacy and budgeting workshops','Establish a strong personal brand within the industry.','Successfully manages and resolves conflicts.'),
(606,6320001517,6320001771,'2021-10-05','2021 Annual Review',4.1,'Meets Expectations','Negotiation Skills','Professional Development Training','Provide access to resources for personal and professional development.','Innovation and creativity training','Attain a leadership position in a professional association.','Consistently meets deadlines and deliverables.'),
(507,6320001518,6320001868,'2021-09-18','2021 Annual Review',2.7,'Below Expectations','Critical Thinking','Critical Thinking Skills','Encourage participation in industry conferences and networking events.','Cross-cultural competence workshops','Expand the companys market reach into new regions.','Takes ownership of projects and tasks.'),
(703,6320001519,6320001869,'2021-10-06','2021 Annual Review',4.5,'Exceeds Expectations','Resilience','Sales and Negotiation Techniques','Support work-life balance initiatives.','Feedback giving and receiving training','Create and implement a sustainability program.','Displays strong attention to detail.'),
(613,6320001520,6320002010,'2021-10-11','2021 Annual Review',4.8,'Exceeds Expectations','Initiative','Customer Relationship Management','Recognize and address burnout or stress-related issues.','Conflict prevention strategies workshops','Develop a reputation for innovative problem-solving.','Exhibits a high level of integrity and ethics.'),
(534,6320001521,6320001824,'2021-09-04','2021 Annual Review',2.6,'Below Expectations','Organizational Skills','Delegation and Empowerment','Provide opportunities for leadership development and skill-building.','Delegation and empowerment training','Lead diversity and inclusion initiatives within the company.','Actively seeks feedback and acts upon it constructively.'),
(742,6320001522,6320001692,'2021-12-20','2021 Annual Review',5,'Exceeds Expectations','Integrity','Cross-Cultural Competence','Offer incentives for achieving performance goals.','Coaching and mentoring programs','Serve on the board of directors for a non-profit organization.','Demonstrates effective decision-making abilities.'),
(495,6320001523,6320001736,'2021-10-23','2021 Annual Review',2.1,'Below Expectations','Flexibility','Feedback Receptiveness','Support diversity and inclusion initiatives.','Diversity and inclusion training','Become a published author or speaker on industry topics.','Shows a willingness to take on new challenges.'),
(748,6320001524,6320001838,'2021-09-17','2021 Annual Review',3.1,'Below Expectations','Resourcefulness','Conflict Management Strategies','Encourage a growth mindset and willingness to take on new challenges.','Networking and relationship-building workshops','Lead a major organizational change initiative.','Works well independently and as part of a team.'),
(564,6320001525,6320001736,'2021-09-19','2021 Annual Review',4.5,'Exceeds Expectations','Risk Management','Self-Motivation and Initiative','Provide opportunities for skill assessments and career planning.','Performance management techniques training','Establish a successful side business or entrepreneurial venture.','Successfully mentors and develops junior colleagues.'),
(620,6320001526,6320001735,'2021-10-09','2021 Annual Review',2.2,'Below Expectations','Coaching and Mentoring','Financial Acumen and Budgeting','Support health and wellness initiatives.','Change management strategies workshops','Obtain an executive leadership position within the organization.','Proactively identifies and addresses areas for improvement.'),
(440,6320001527,6320001713,'2021-12-02','2021 Annual Review',4.8,'Exceeds Expectations','Networking','Organizational Skills','Encourage participation in community service and volunteer opportunities.','Goal setting and achievement training','Drive significant cost savings or revenue growth for the company.','Acts as a role model for other employees.'),
(532,6320001528,6320001898,'2021-11-20','2021 Annual Review',4.7,'Exceeds Expectations','Financial Acumen','Goal Setting and Achievement','Provide opportunities for job shadowing and cross-training.','Assertiveness and self-confidence workshops','Develop and execute a successful strategic plan.','Maintains a strong focus on customer satisfaction.'),
(501,6320001529,6320001729,'2021-12-08','2021 Annual Review',2.4,'Below Expectations','Interpersonal Skills','Interpersonal Communication','Offer flexible work arrangements when possible.','Critical thinking and analytical skills development','Secure funding for a new business unit or project.','Demonstrates strong analytical and critical thinking skills.'),
(456,6320001530,6320001757,'2021-11-20','2021 Annual Review',3,'Below Expectations','Drive for Results','Risk Assessment and Management','Support employee-led initiatives and projects.','Career development planning sessions','Lead a successful product launch or rebranding effort.','Displays a high level of emotional intelligence.'),
(747,6320001531,6320001686,'2021-11-19','2021 Annual Review',3.2,'Below Expectations','Dependability','Continuous Learning and Skill Enhancement','Encourage participation in professional associations and industry groups.','Technology adoption and proficiency training','Advocate for employee development and advancement opportunities.','Successfully leads and manages projects.'),
(475,6320001532,6320001817,'2021-11-10','2021 Annual Review',4.5,'Exceeds Expectations','Multitasking','Prioritization and Time Allocation','Provide opportunities for rotational assignments.','Public relations and media management training','Lead a successful digital transformation initiative.','Consistently demonstrates professionalism in all interactions.'),
(427,6320001533,6320001788,'2021-09-27','2021 Annual Review',2.7,'Below Expectations','Presentation Skills','Technology Adoption and Proficiency','Offer financial assistance for further education or certifications.','Crisis management simulation exercises','Create and implement a successful corporate social responsibility program.','Shows a commitment to continuous improvement.'),
(630,6320001534,6320001729,'2021-10-12','2021 Annual Review',4.7,'Exceeds Expectations','Conflict Management','Networking and Relationship Building','Support mental health awareness and resources.','Ethical decision-making workshops','Secure funding for a major research and development project.','Successfully adapts to changing business needs.'),
(541,6320001535,6320001774,'2021-10-23','2021 Annual Review',3.9,'Meets Expectations','Adaptation to Change','Resilience and Grit','Recognize and reward innovation and creativity.','Regulatory compliance training','Develop and implement a successful talent acquisition strategy.','Exhibits strong problem-solving abilities under pressure.'),
(628,6320001536,6320001690,'2021-09-16','2021 Annual Review',2.3,'Below Expectations','Empathy','Team Leadership and Management','Provide access to networking and mentorship programs.','Supply chain management workshops','Lead a successful organizational restructuring effort.','Effectively manages time and priorities.'),
(421,6320001537,6320001790,'2021-11-16','2021 Annual Review',2.5,'Below Expectations','Goal Setting and Achievement','Public Speaking','Offer opportunities for special projects or task forces.','Market research and analysis training','Establish a reputation for exceptional customer service.','Builds strong partnerships across departments.'),
(506,6320001538,6320001709,'2021-11-24','2021 Annual Review',2.6,'Below Expectations','Diplomacy','Work-Life Balance','Support skill-building workshops and seminars.','Talent acquisition and retention strategies workshops','Become a recognized expert in a niche market or industry segment.','Consistently achieves positive feedback from peers and managers.'),
(604,6320001539,6320001836,'2021-11-06','2021 Annual Review',4.7,'Exceeds Expectations','Sales and Marketing Skills','Change Management','Provide access to online learning platforms.','Remote work and virtual collaboration training','Develop and implement a successful employee engagement program.','Takes responsibility for personal and professional growth.'),
(483,6320001540,6320001799,'2021-10-22','2021 Annual Review',3.5,'Meets Expectations','Attention Management','Ethics and Integrity','Encourage participation in leadership development programs.','Personal branding and professional image development','Attain recognition as a top performer within the organization.','Demonstrates a strong commitment to company goals and objectives.'),
(582,6320001541,6320001754,'2021-12-24','2021 Annual Review',3,'Below Expectations','Professionalism','Sales and Marketing Strategies','Offer opportunities for public speaking and presentation skills training.','Health and wellness initiatives and workshops','Lead a successful corporate culture transformation effort.','Effectively communicates complex information to diverse audiences.'),
(464,6320001542,6320001859,'2021-09-11','2021 Annual Review',4.8,'Exceeds Expectations','Self-Motivation','Feedback Implementation','Provide access to career counseling and coaching services.','Entrepreneurial mindset development programs','Become a sought-after speaker or presenter at industry events.','Successfully navigates ambiguity and uncertainty.'),
(783,6320001543,6320001774,'2021-09-18','2021 Annual Review',2.2,'Below Expectations','Continuous Learning','Professionalism and Etiquette','Encourage participation in industry-specific training programs.','Sustainability and corporate social responsibility training','Develop and implement a successful employer branding strategy.','Builds and maintains a strong network of professional contacts.'),
(786,6320001544,6320001731,'2021-11-27','2021 Annual Review',3,'Below Expectations','Cross-Cultural Competence','Conflict Prevention','Support employee-driven innovation initiatives.','Succession planning and talent development','Lead a successful corporate rebranding effort.','Demonstrates a strong understanding of industry trends and best practices.'),
(782,6320001545,6320001813,'2021-10-03','2021 Annual Review',2.3,'Below Expectations','Feedback Receptiveness','Conflict Resolution Techniques','Provide opportunities for job rotations or temporary assignments.','Performance appraisal and feedback training','Obtain recognition as a top employer in the industry.','Shows a commitment to promoting diversity and inclusion in the workplace.'),
(466,6320001546,6320001775,'2021-09-05','2021 Annual Review',2.8,'Below Expectations','Delegation','Cross-Functional Collaboration','Offer opportunities for participation in industry conferences and events.','Conflict resolution through mediation training','Create and implement a sustainability program.','Effectively manages and resolves customer complaints.'),
(538,6320001547,6320001731,'2021-09-05','2021 Annual Review',4.4,'Meets Expectations','Crisis Management','Career Development Planning','Support employee resource groups and affinity networks.','Data analysis and interpretation workshops','Develop and implement a successful talent acquisition strategy.','Successfully leads and motivates team members to achieve goals.'),
(741,6320001548,6320001842,'2021-12-25','2021 Annual Review',3.2,'Below Expectations','Compliance Adherence','Stress Reduction Techniques','Recognize and reward teamwork and collaboration.','Resilience and mental toughness training','Serve on the board of directors for a non-profit organization.','Effectively manages time and priorities.'),
(439,6320001549,6320001760,'2021-11-12','2021 Annual Review',4.9,'Exceeds Expectations','Stakeholder Management','Personal Branding and Visibility','Foster a culture of continuous improvement and learning.','Continuous learning and self-directed development encouragement','Obtain an executive leadership position within the organization.','Acts as a role model for other employees.'),
(586,6320001550,6320001684,'2021-10-01','2021 Annual Review',2.3,'Below Expectations','Feedback Receptiveness','Cross-Functional Collaboration','Support employee resource groups and affinity networks.','Continuous learning and self-directed development encouragement','Become a published author or speaker on industry topics.','Takes initiative to drive positive outcomes.'),
(504,6320001551,6320001732,'2021-09-05','2021 Annual Review',4.3,'Meets Expectations','Resilience','Attention to Detail','Recognize and reward teamwork and collaboration.','Health and wellness initiatives and workshops','Lead a major organizational change initiative.','Demonstrates effective decision-making abilities.'),
(478,6320001552,6320001746,'2021-09-01','2021 Annual Review',2.5,'Below Expectations','Conflict Management','Feedback Receptiveness','Discuss career aspirations and provide guidance on advancement opportunities.','Remote work and virtual collaboration training','Lead a cross-functional team on a major project.','Demonstrates effective decision-making abilities.'),
(403,6320001553,6320001871,'2021-09-18','2021 Annual Review',3,'Below Expectations','Coaching and Mentoring','Attention to Detail','Support employee-driven innovation initiatives.','Goal setting and achievement training','Serve on the board of directors for a non-profit organization.','Effectively manages time and priorities.'),
(484,6320001554,6320001700,'2021-10-03','2021 Annual Review',2.6,'Below Expectations','Interpersonal Skills','Feedback Implementation','Foster a positive work environment that promotes collaboration and innovation.','Technology adoption and proficiency training','Transition into a different department or role.','Consistently demonstrates professionalism in all interactions.'),
(797,6320001555,6320001760,'2021-10-28','2021 Annual Review',2.6,'Below Expectations','Continuous Learning','Conflict Resolution Techniques','Offer mentorship and coaching to support their growth.','Goal setting and achievement training','Lead a major organizational change initiative.','Effectively collaborates with team members.'),
(536,6320001556,6320001841,'2021-12-05','2021 Annual Review',2.3,'Below Expectations','Flexibility','Critical Thinking Skills','Foster a positive work environment that promotes collaboration and innovation.','Market research and analysis training','Become a sought-after speaker or presenter at industry events.','Successfully leads and manages projects.'),
(720,6320001557,6320001762,'2021-11-05','2021 Annual Review',3.9,'Meets Expectations','Continuous Learning','Conflict Management Strategies','Conduct performance evaluations based on predefined criteria.','Data analysis and interpretation workshops','Obtain an executive leadership position within the organization.','Displays strong attention to detail.'),
(503,6320001558,6320001866,'2021-11-27','2021 Annual Review',4.3,'Meets Expectations','Diplomacy','Emotional Intelligence','Conduct performance evaluations based on predefined criteria.','Sales and negotiation training','Establish a strong personal brand within the industry.','Successfully meets or exceeds all performance targets.'),
(480,6320001559,6320001721,'2021-11-22','2021 Annual Review',4,'Meets Expectations','Conflict Management','Cross-Cultural Competence','Support work-life balance initiatives.','Resilience and mental toughness training','Develop and implement a successful employee engagement program.','Takes initiative to drive positive outcomes.'),
(470,6320001560,6320001817,'2021-12-17','2021 Annual Review',4.2,'Meets Expectations','Technical Proficiency','Cross-Functional Collaboration','Encourage participation in industry-specific training programs.','Market research and analysis training','Become a sought-after speaker or presenter at industry events.','Maintains a positive and professional attitude.'),
(765,6320001561,6320001801,'2021-12-08','2021 Annual Review',3.6,'Meets Expectations','Innovation','Communication Skills (Written/Verbal)','Provide access to resources for personal and professional development.','Networking and relationship-building workshops','Obtain an executive leadership position within the organization.','Displays resilience in challenging situations.'),
(525,6320001562,6320001845,'2021-09-06','2021 Annual Review',2.7,'Below Expectations','Flexibility','Work-Life Balance','Support employee resource groups and affinity networks.','Effective communication training','Become a sought-after speaker or presenter at industry events.','Demonstrates exceptional leadership qualities.'),
(725,6320001563,6320001871,'2021-10-19','2021 Annual Review',2.9,'Below Expectations','Emotional Intelligence','Personal Branding and Visibility','Encourage participation in industry conferences and networking events.','Entrepreneurial mindset development programs','Become a sought-after speaker or presenter at industry events.','Displays strong attention to detail.'),
(402,6320001564,6320001689,'2021-12-25','2021 Annual Review',3.4,'Below Expectations','Conflict Resolution','Public Speaking','Recognize and reward innovation and creativity.','Data analysis and interpretation workshops','Attain recognition as a top performer within the organization.','Takes ownership of projects and tasks.'),
(542,6320001565,6320001764,'2021-10-04','2021 Annual Review',3.4,'Below Expectations','Communication Skills','Sales and Negotiation Techniques','Encourage self-reflection and goal-setting.','Technical skills enhancement programs','Advocate for employee development and advancement opportunities.','Effectively communicates complex information to diverse audiences.'),
(489,6320001566,6320001814,'2021-10-01','2021 Annual Review',4,'Meets Expectations','Time Management','Feedback Implementation','Support diversity and inclusion initiatives.','Sales and negotiation training','Advocate for employee development and advancement opportunities.','Displays resilience in challenging situations.'),
(655,6320001567,6320001737,'2021-11-07','2021 Annual Review',4.5,'Exceeds Expectations','Analytical Thinking','Self-Motivation and Initiative','Support mental health awareness and resources.','Data analysis and interpretation workshops','Spearhead a company-wide initiative or program.','Takes responsibility for personal and professional growth.'),
(669,6320001568,6320001803,'2021-09-04','2021 Annual Review',4,'Meets Expectations','Flexibility','Cross-Cultural Competence','Provide resources and support to help them succeed in their role.','Data analysis and interpretation workshops','Obtain recognition as a top employer in the industry.','Provides valuable insights and innovative ideas.'),
(660,6320001569,6320001834,'2021-10-23','2021 Annual Review',2.9,'Below Expectations','Conflict Resolution','Decision-Making Skills','Foster a positive work environment that promotes collaboration and innovation.','Innovation and creativity training','Spearhead a company-wide initiative or program.','Maintains a positive and professional attitude.'),
(734,6320001570,6320001704,'2021-10-16','2021 Annual Review',3.9,'Meets Expectations','Adaptability','Team Leadership and Management','Support skill-building workshops and seminars.','Strategic planning and execution training','Obtain a leadership role within the company.','Builds strong partnerships across departments.'),
(710,6320001571,6320001863,'2021-12-09','2021 Annual Review',5,'Exceeds Expectations','Creativity','Customer Relationship Management','Conduct performance evaluations based on predefined criteria.','Emotional intelligence enhancement','Develop and implement a successful talent acquisition strategy.','Actively seeks feedback and acts upon it constructively.'),
(750,6320001572,6320001887,'2021-09-16','2021 Annual Review',4.6,'Exceeds Expectations','Networking','Networking and Relationship Building','Recognize and reward innovation and creativity.','Customer service excellence workshops','Establish a strong personal brand within the industry.','Exhibits a high level of integrity and ethics.'),
(601,6320001573,6320001826,'2021-12-23','2021 Annual Review',2.6,'Below Expectations','Networking','Decision-Making Skills','Discuss career aspirations and provide guidance on advancement opportunities.','Delegation and empowerment training','Create and implement a successful corporate social responsibility program.','Consistently achieves positive feedback from peers and managers.'),
(788,6320001574,6320001750,'2021-12-21','2021 Annual Review',2.2,'Below Expectations','Innovation','Team Collaboration','Support employee-driven innovation initiatives.','Supply chain management workshops','Advocate for employee development and advancement opportunities.','Displays resilience in challenging situations.'),
(531,6320001575,6320001797,'2021-12-22','2021 Annual Review',2.2,'Below Expectations','Analytical Thinking','Technology Adoption and Proficiency','Recognize and address burnout or stress-related issues.','Performance management techniques training','Obtain a leadership role within the company.','Successfully mentors and develops junior colleagues.'),
(493,6320001576,6320001772,'2021-09-24','2021 Annual Review',4.4,'Meets Expectations','Sales and Marketing Skills','Time Management','Support work-life balance initiatives.','Presentation and public speaking skills development','Represent the company at industry conferences or events.','Shows a commitment to continuous improvement.'),
(715,6320001577,6320001720,'2021-12-26','2021 Annual Review',2.5,'Below Expectations','Self-Motivation','Feedback Receptiveness','Provide access to career counseling and coaching services.','Ethical decision-making workshops','Lead a successful product launch or rebranding effort.','Shows a commitment to continuous improvement.'),
(432,6320001578,6320001798,'2021-09-05','2021 Annual Review',3.4,'Below Expectations','Creativity','Feedback Implementation','Foster a positive work environment that promotes collaboration and innovation.','Technology adoption and proficiency training','Create and implement a sustainability program.','Takes responsibility for personal and professional growth.'),
(656,6320001579,6320001758,'2021-11-20','2021 Annual Review',2.4,'Below Expectations','Risk Management','Work-Life Balance','Encourage peer feedback and collaboration.','Goal setting and achievement training','Lead a successful digital transformation initiative.','Consistently delivers high-quality work.'),
(646,6320001580,6320001896,'2021-12-07','2021 Annual Review',4.5,'Exceeds Expectations','Problem-Solving Abilities','Project Management Techniques','Encourage participation in leadership development programs.','Feedback giving and receiving training','Create and implement a sustainability program.','Successfully adapts to changing business needs.'),
(490,6320001581,6320001783,'2021-10-28','2021 Annual Review',3.1,'Below Expectations','Negotiation Skills','Project Management Techniques','Encourage participation in training programs and workshops.','Supply chain management workshops','Lead a successful organizational restructuring effort.','Exhibits a high level of integrity and ethics.'),
(738,6320001582,6320001754,'2021-11-11','2021 Annual Review',4.5,'Exceeds Expectations','Multitasking','Adaptability to Change','Support mental health awareness and resources.','Technology adoption and proficiency training','Secure a mentorship or coaching relationship with a senior leader.','Displays strong attention to detail.'),
(445,6320001583,6320001867,'2021-11-16','2021 Annual Review',2.6,'Below Expectations','Technical Proficiency','Self-Motivation and Initiative','Foster a culture of continuous improvement and learning.','Stress management seminars','Complete advanced education or certification.','Effectively manages time and priorities.'),
(561,6320001584,6320001766,'2021-10-16','2021 Annual Review',3.8,'Meets Expectations','Leadership Skills','Team Leadership and Management','Provide regular feedback on their performance.','Market research and analysis training','Attain proficiency in a new technology or skill.','Exemplifies the companys core values in actions.'),
(611,6320001585,6320001846,'2021-12-01','2021 Annual Review',4.2,'Meets Expectations','Adaptability','Attention to Detail','Support work-life balance initiatives.','Conflict resolution techniques','Attain proficiency in a new technology or skill.','Builds strong partnerships across departments.'),
(781,6320001586,6320001698,'2021-11-06','2021 Annual Review',4.5,'Exceeds Expectations','Innovation','Sales and Negotiation Techniques','Support mental health awareness and resources.','Regulatory compliance training','Receive recognition as an industry thought leader.','Consistently meets deadlines and deliverables.'),
(411,6320001587,6320001892,'2021-09-03','2021 Annual Review',3.3,'Below Expectations','Critical Thinking','Risk Assessment and Management','Provide constructive feedback on specific tasks and projects.','Team building and collaboration workshops','Become a sought-after speaker or presenter at industry events.','Displays resilience in challenging situations.'),
(488,6320001588,6320001896,'2021-12-09','2021 Annual Review',4.9,'Exceeds Expectations','Critical Thinking','Conflict Resolution Techniques','Recognize and reward innovation and creativity.','Stress management seminars','Develop and implement a successful employee engagement program.','Takes initiative to drive positive outcomes.'),
(657,6320001589,6320001840,'2021-09-01','2021 Annual Review',2.8,'Below Expectations','Attention to Detail','Cross-Cultural Competence','Offer incentives for achieving performance goals.','Stress management seminars','Secure funding for a major research and development project.','Takes initiative to drive positive outcomes.'),
(594,6320001590,6320001839,'2021-09-16','2021 Annual Review',3.9,'Meets Expectations','Attention to Detail','Customer Relationship Management','Offer flexible work arrangements when possible.','Financial literacy and budgeting workshops','Develop a reputation for innovative problem-solving.','Exhibits strong problem-solving abilities under pressure.'),
(597,6320001591,6320001894,'2021-10-06','2021 Annual Review',4,'Meets Expectations','Attention to Detail','Critical Thinking Skills','Foster a positive work environment that promotes collaboration and innovation.','Delegation and empowerment training','Establish a reputation for exceptional customer service.','Takes ownership of projects and tasks.'),
(749,6320001592,6320001778,'2021-11-14','2021 Annual Review',2.5,'Below Expectations','Attention Management','Change Management','Provide constructive feedback on specific tasks and projects.','Delegation and empowerment training','Receive recognition as an industry thought leader.','Maintains a strong focus on customer satisfaction.'),
(746,6320001593,6320001770,'2021-10-03','2021 Annual Review',2.6,'Below Expectations','Communication Skills','Emotional Intelligence','Provide regular feedback on their performance.','Technology adoption and proficiency training','Manage a department or division within the organization.','Maintains a positive and professional attitude.'),
(713,6320001594,6320001755,'2021-09-18','2021 Annual Review',3.3,'Below Expectations','Attention to Detail','Professionalism and Etiquette','Support employee resource groups and affinity networks.','Strategic planning and execution training','Attain recognition as a top performer within the organization.','Shows a commitment to ongoing learning and development.'),
(510,6320001595,6320001824,'2021-09-28','2021 Annual Review',2.9,'Below Expectations','Communication Skills','Professionalism and Etiquette','Conduct performance evaluations based on predefined criteria.','Continuous learning and self-directed development encouragement','Secure a mentorship or coaching relationship with a senior leader.','Consistently delivers high-quality work.'),
(603,6320001596,6320001703,'2021-10-10','2021 Annual Review',2.2,'Below Expectations','Creativity','Problem-Solving Techniques','Encourage participation in professional associations and industry groups.','Sustainability and corporate social responsibility training','Start a mentorship program within the organization.','Exceeds expectations in all key performance areas.'),
(774,6320001597,6320001730,'2021-12-17','2021 Annual Review',3.2,'Below Expectations','Risk Management','Customer Relationship Management','Provide access to networking and mentorship programs.','Presentation and public speaking skills development','Spearhead a company-wide initiative or program.','Maintains a positive and professional attitude.'),
(462,6320001598,6320001849,'2021-12-11','2021 Annual Review',2.6,'Below Expectations','Team Collaboration','Stress Reduction Techniques','Foster a positive work environment that promotes collaboration and innovation.','Financial literacy and budgeting workshops','Lead a successful product launch or rebranding effort.','Successfully meets or exceeds all performance targets.'),
(438,6320001599,6320001693,'2021-11-07','2021 Annual Review',3.7,'Meets Expectations','Empathy','Change Management','Conduct performance evaluations based on predefined criteria.','Technology adoption and proficiency training','Lead a successful corporate culture transformation effort.','Successfully navigates ambiguity and uncertainty.'),
(633,6320001500,6320001747,'2020-11-13','2020 Annual Review',3.2,'Below Expectations','Leadership Skills','Conflict Resolution','Provide opportunities for job rotations or temporary assignments.','Performance management techniques training','Become a sought-after speaker or presenter at industry events.','Effectively collaborates with team members.'),
(401,6320001501,6320001875,'2020-11-17','2020 Annual Review',4.3,'Meets Expectations','Flexibility','Ethics and Integrity','Establish regular check-ins to track progress and address any concerns.','Team building and collaboration workshops','Develop and execute a successful strategic plan.','Successfully navigates ambiguity and uncertainty.'),
(430,6320001502,6320001705,'2020-10-01','2020 Annual Review',2.3,'Below Expectations','Interpersonal Skills','Work-Life Balance','Encourage participation in leadership development programs.','Cross-cultural competence workshops','Secure funding for a major research and development project.','Successfully mentors and develops junior colleagues.'),
(789,6320001503,6320001792,'2020-11-04','2020 Annual Review',4.8,'Exceeds Expectations','Integrity','Work-Life Balance','Support skill-building workshops and seminars.','Emotional intelligence enhancement','Lead a cross-functional team on a major project.','Takes initiative to drive positive outcomes.'),
(692,6320001504,6320001708,'2020-12-13','2020 Annual Review',4,'Meets Expectations','Adaptation to Change','Networking Abilities','Support employee resource groups and affinity networks.','Adaptability to change training','Lead a successful corporate culture transformation effort.','Effectively communicates complex information to diverse audiences.'),
(579,6320001505,6320001693,'2020-11-20','2020 Annual Review',4.9,'Exceeds Expectations','Adaptability','Goal Setting and Achievement','Encourage peer feedback and collaboration.','Performance appraisal and feedback training','Develop and implement a successful employer branding strategy.','Successfully mentors and develops junior colleagues.'),
(450,6320001506,6320001752,'2020-10-23','2020 Annual Review',4.7,'Exceeds Expectations','Analytical Thinking','Resilience and Grit','Provide regular feedback on their performance.','Market research and analysis training','Complete advanced education or certification.','Maintains a strong focus on customer satisfaction.'),
(420,6320001507,6320001689,'2020-12-01','2020 Annual Review',2.5,'Below Expectations','Conflict Management','Emotional Intelligence','Recognize and reward teamwork and collaboration.','Goal setting and achievement training','Develop and implement a successful employee engagement program.','Demonstrates exceptional leadership qualities.'),
(574,6320001508,6320001762,'2020-10-16','2020 Annual Review',4.3,'Meets Expectations','Attention to Detail','Customer Relationship Management','Discuss career aspirations and provide guidance on advancement opportunities.','Conflict resolution through mediation training','Attain proficiency in a new technology or skill.','Shows a commitment to continuous improvement.'),
(513,6320001509,6320001804,'2020-12-02','2020 Annual Review',3.4,'Below Expectations','Interpersonal Skills','Professional Development Training','Recognize and address any barriers to their success.','Conflict prevention strategies workshops','Establish a successful side business or entrepreneurial venture.','Builds strong partnerships across departments.'),
(759,6320001510,6320001788,'2020-09-25','2020 Annual Review',2.5,'Below Expectations','Sales and Marketing Skills','Adaptability to Change','Encourage participation in industry conferences and networking events.','Time management workshops','Develop and implement a successful employee engagement program.','Builds strong relationships with clients and customers.'),
(635,6320001511,6320001817,'2020-12-07','2020 Annual Review',4.1,'Meets Expectations','Initiative','Sales and Marketing Strategies','Recognize and celebrate their achievements.','Project management training','Create and implement a sustainability program.','Effectively manages time and priorities.'),
(632,6320001512,6320001688,'2020-09-01','2020 Annual Review',4.6,'Exceeds Expectations','Self-Motivation','Feedback Implementation','Encourage participation in professional associations and industry groups.','Career development planning sessions','Attain a leadership position in a professional association.','Communicates effectively with colleagues and stakeholders.'),
(414,6320001513,6320001836,'2020-11-15','2020 Annual Review',2.2,'Below Expectations','Coaching and Mentoring','Stress Management','Support diversity and inclusion initiatives.','Project management training','Start a mentorship program within the organization.','Demonstrates strong analytical and critical thinking skills.'),
(404,6320001514,6320001852,'2020-09-20','2020 Annual Review',3.7,'Meets Expectations','Communication Skills','Decision-Making Skills','Provide access to online learning platforms.','Stress management seminars','Establish a strong personal brand within the industry.','Successfully navigates ambiguity and uncertainty.'),
(529,6320001515,6320001807,'2020-10-03','2020 Annual Review',3.2,'Below Expectations','Risk Management','Organizational Skills','Recognize and celebrate their achievements.','Health and wellness initiatives and workshops','Advocate for employee development and advancement opportunities.','Shows a high level of adaptability to change.'),
(609,6320001516,6320001832,'2020-12-17','2020 Annual Review',2.8,'Below Expectations','Professionalism','Delegation and Empowerment','Offer opportunities for public speaking and presentation skills training.','Decision-making skills refinement','Receive recognition as an industry thought leader.','Effectively communicates complex information to diverse audiences.'),
(693,6320001517,6320001855,'2020-12-27','2020 Annual Review',3.2,'Below Expectations','Delegation','Feedback Receptiveness','Offer opportunities for cross-functional training and projects.','Talent acquisition and retention strategies workshops','Lead a successful organizational restructuring effort.','Successfully leads and manages projects.'),
(794,6320001518,6320001808,'2020-11-22','2020 Annual Review',2.5,'Below Expectations','Coaching and Mentoring','Emotional Intelligence','Encourage participation in community service and volunteer opportunities.','Cross-cultural competence workshops','Attain a leadership position in a professional association.','Provides valuable insights and innovative ideas.'),
(492,6320001519,6320001706,'2020-09-12','2020 Annual Review',4.5,'Exceeds Expectations','Attention Management','Adaptability to Change','Encourage participation in leadership development programs.','Succession planning and talent development','Lead a successful merger or acquisition project.','Effectively collaborates with team members.'),
(800,6320001520,6320001772,'2020-10-26','2020 Annual Review',3.2,'Below Expectations','Presentation Skills','Public Speaking','Provide opportunities for job rotations or temporary assignments.','Health and wellness initiatives and workshops','Obtain a leadership role within the company.','Shows a commitment to continuous improvement.'),
(702,6320001521,6320001814,'2020-10-13','2020 Annual Review',3.1,'Below Expectations','Technical Proficiency','Continuous Learning and Skill Enhancement','Support employee-led initiatives and projects.','Feedback giving and receiving training','Develop a reputation for innovative problem-solving.','Consistently delivers high-quality work.'),
(560,6320001522,6320001691,'2020-12-23','2020 Annual Review',3.8,'Meets Expectations','Adaptability','Prioritization and Time Allocation','Support diversity and inclusion initiatives.','Conflict resolution through mediation training','Establish a reputation for exceptional customer service.','Takes responsibility for personal and professional growth.'),
(589,6320001523,6320001896,'2020-09-16','2020 Annual Review',4.6,'Exceeds Expectations','Conflict Resolution','Stress Management','Offer flexible work arrangements when possible.','Innovation and creativity training','Spearhead a company-wide initiative or program.','Exhibits a high level of integrity and ethics.'),
(499,6320001524,6320001767,'2020-11-19','2020 Annual Review',4.9,'Exceeds Expectations','Conflict Management','Attention to Detail','Encourage participation in industry-specific training programs.','Data analysis and interpretation workshops','Lead a successful product launch or rebranding effort.','Maintains a positive and professional attitude.'),
(754,6320001525,6320001820,'2020-12-07','2020 Annual Review',2.5,'Below Expectations','Dependability','Conflict Management Strategies','Offer opportunities for public speaking and presentation skills training.','Networking and relationship-building workshops','Expand the companys market reach into new regions.','Consistently delivers high-quality work.'),
(771,6320001526,6320001739,'2020-12-21','2020 Annual Review',4.1,'Meets Expectations','Coaching and Mentoring','Leadership Development','Provide opportunities for job rotations or temporary assignments.','Remote work and virtual collaboration training','Receive recognition as an industry thought leader.','Successfully manages and resolves conflicts.'),
(784,6320001527,6320001692,'2020-12-17','2020 Annual Review',4.6,'Exceeds Expectations','Sales and Marketing Skills','Public Speaking','Offer flexible work arrangements when possible.','Financial literacy and budgeting workshops','Establish a successful side business or entrepreneurial venture.','Effectively manages time and priorities.'),
(796,6320001528,6320001688,'2020-09-01','2020 Annual Review',3,'Below Expectations','Technical Proficiency','Risk Assessment and Management','Identify areas for improvement and create action plans to address them.','Data analysis and interpretation workshops','Become a recognized expert in a niche market or industry segment.','Successfully leads and manages projects.'),
(659,6320001529,6320001828,'2020-12-08','2020 Annual Review',3.1,'Below Expectations','Strategic Thinking','Networking and Relationship Building','Provide constructive feedback on specific tasks and projects.','Team building and collaboration workshops','Lead diversity and inclusion initiatives within the company.','Shows a willingness to take on new challenges.'),
(590,6320001530,6320001889,'2020-11-08','2020 Annual Review',4.4,'Meets Expectations','Empathy','Conflict Prevention','Offer financial assistance for further education or certifications.','Effective communication training','Become a subject matter expert in a specific area.','Displays resilience in challenging situations.'),
(698,6320001531,6320001787,'2020-11-05','2020 Annual Review',5,'Exceeds Expectations','Technical Proficiency','Project Management Techniques','Recognize and reward teamwork and collaboration.','Regulatory compliance training','Complete advanced education or certification.','Demonstrates effective decision-making abilities.'),
(642,6320001532,6320001705,'2020-11-21','2020 Annual Review',3.6,'Meets Expectations','Customer Focus','Career Development Planning','Encourage participation in industry-specific training programs.','Emotional intelligence enhancement','Lead diversity and inclusion initiatives within the company.','Displays strong attention to detail.'),
(535,6320001533,6320001725,'2020-09-09','2020 Annual Review',3.9,'Meets Expectations','Resourcefulness','Feedback Implementation','Provide access to resources for personal and professional development.','Innovation and creativity training','Create and implement a sustainability program.','Exemplifies the companys core values in actions.'),
(467,6320001534,6320001787,'2020-10-22','2020 Annual Review',2.2,'Below Expectations','Networking','Leadership Development','Recognize and reward innovation and creativity.','Assertiveness and self-confidence workshops','Drive significant cost savings or revenue growth for the company.','Shows a commitment to continuous improvement.'),
(688,6320001535,6320001866,'2020-10-18','2020 Annual Review',3.3,'Below Expectations','Leadership Skills','Prioritization and Time Allocation','Offer opportunities for participation in industry conferences and events.','Presentation and public speaking skills development','Lead diversity and inclusion initiatives within the company.','Actively seeks feedback and acts upon it constructively.'),
(711,6320001536,6320001888,'2020-10-03','2020 Annual Review',4.1,'Meets Expectations','Attention Management','Networking Abilities','Encourage participation in community service and volunteer opportunities.','Presentation and public speaking skills development','Lead a cross-functional team on a major project.','Shows a commitment to ongoing learning and development.'),
(686,6320001537,6320001835,'2020-11-22','2020 Annual Review',3.1,'Below Expectations','Critical Thinking','Feedback Implementation','Recognize and celebrate their achievements.','Data analysis and interpretation workshops','Lead a successful merger or acquisition project.','Displays strong problem-solving skills.'),
(544,6320001538,6320001702,'2020-12-24','2020 Annual Review',3.5,'Meets Expectations','Adaptation to Change','Feedback Implementation','Support mental health awareness and resources.','Personal branding and professional image development','Develop a reputation for innovative problem-solving.','Communicates effectively with colleagues and stakeholders.'),
(751,6320001539,6320001797,'2020-10-20','2020 Annual Review',4.9,'Exceeds Expectations','Professionalism','Presentation Skills','Encourage ongoing learning and development opportunities.','Stress management seminars','Lead a successful digital transformation initiative.','Takes ownership of projects and tasks.'),
(615,6320001540,6320001725,'2020-12-20','2020 Annual Review',4.2,'Meets Expectations','Feedback Receptiveness','Professional Development Training','Identify areas for improvement and create action plans to address them.','Continuous learning and self-directed development encouragement','Secure a mentorship or coaching relationship with a senior leader.','Demonstrates effective decision-making abilities.'),
(761,6320001541,6320001754,'2020-09-23','2020 Annual Review',3.3,'Below Expectations','Risk Management','Self-Motivation and Initiative','Support diversity and inclusion initiatives.','Decision-making skills refinement','Become a sought-after speaker or presenter at industry events.','Effectively manages time and priorities.'),
(694,6320001542,6320001895,'2020-12-20','2020 Annual Review',2.3,'Below Expectations','Problem-Solving Abilities','Critical Thinking Skills','Provide access to networking and mentorship programs.','Goal setting and achievement training','Secure a mentorship or coaching relationship with a senior leader.','Demonstrates excellent time management skills.'),
(486,6320001543,6320001875,'2020-09-03','2020 Annual Review',3.3,'Below Expectations','Conflict Resolution','Project Management Techniques','Provide opportunities for rotational assignments.','Market research and analysis training','Drive significant cost savings or revenue growth for the company.','Demonstrates a strong understanding of industry trends and best practices.'),
(516,6320001544,6320001729,'2020-11-22','2020 Annual Review',2.2,'Below Expectations','Resourcefulness','Creativity and Innovation','Offer financial assistance for further education or certifications.','Innovation and creativity training','Drive significant cost savings or revenue growth for the company.','Shows a high level of adaptability to change.'),
(517,6320001545,6320001758,'2020-10-27','2020 Annual Review',3.6,'Meets Expectations','Goal Setting and Achievement','Attention to Detail','Encourage participation in industry-specific training programs.','Stress management seminars','Obtain an executive leadership position within the organization.','Consistently meets deadlines and deliverables.'),
(680,6320001546,6320001784,'2020-12-05','2020 Annual Review',2.7,'Below Expectations','Feedback Receptiveness','Career Development Planning','Encourage participation in training programs and workshops.','Adaptability to change training','Become a published author or speaker on industry topics.','Consistently meets deadlines and deliverables.'),
(766,6320001547,6320001867,'2020-10-27','2020 Annual Review',4.7,'Exceeds Expectations','Sales and Marketing Skills','Goal Setting and Achievement','Provide constructive feedback on specific tasks and projects.','Strategic planning and execution training','Establish a successful side business or entrepreneurial venture.','Proactively identifies and addresses areas for improvement.'),
(662,6320001548,6320001755,'2020-11-04','2020 Annual Review',3.4,'Below Expectations','Analytical Thinking','Team Collaboration','Encourage participation in professional associations and industry groups.','Supply chain management workshops','Create and implement a successful corporate social responsibility program.','Takes ownership of projects and tasks.'),
(699,6320001549,6320001736,'2020-11-16','2020 Annual Review',4,'Meets Expectations','Feedback Receptiveness','Time Management','Provide constructive feedback on specific tasks and projects.','Time management workshops','Represent the company at industry conferences or events.','Effectively manages time and priorities.'),
(498,6320001550,6320001746,'2020-12-13','2020 Annual Review',4.1,'Meets Expectations','Feedback Receptiveness','Technology Adoption and Proficiency','Encourage a growth mindset and willingness to take on new challenges.','Continuous learning and self-directed development encouragement','Secure a mentorship or coaching relationship with a senior leader.','Successfully manages and resolves conflicts.'),
(610,6320001551,6320001833,'2020-11-13','2020 Annual Review',4.5,'Exceeds Expectations','Professionalism','Conflict Resolution Techniques','Set clear and achievable performance goals with the employee.','Conflict prevention strategies workshops','Attain proficiency in a new technology or skill.','Builds strong relationships with clients and customers.'),
(458,6320001552,6320001791,'2020-11-14','2020 Annual Review',2.6,'Below Expectations','Dependability','Leadership Development','Support employee-driven innovation initiatives.','Assertiveness and self-confidence workshops','Serve on the board of directors for a non-profit organization.','Displays a high level of emotional intelligence.'),
(767,6320001553,6320001734,'2020-10-19','2020 Annual Review',2.4,'Below Expectations','Negotiation Skills','Self-Motivation and Initiative','Support employee-led initiatives and projects.','Sales and negotiation training','Become a published author or speaker on industry topics.','Maintains a strong focus on customer satisfaction.'),
(666,6320001554,6320001792,'2020-11-22','2020 Annual Review',3.5,'Meets Expectations','Coaching and Mentoring','Organizational Skills','Recognize and reward teamwork and collaboration.','Succession planning and talent development','Attain recognition as a top performer within the organization.','Consistently achieves positive feedback from peers and managers.'),
(512,6320001555,6320001849,'2020-12-18','2020 Annual Review',4.1,'Meets Expectations','Organizational Skills','Professionalism and Etiquette','Offer incentives for achieving performance goals.','Performance management techniques training','Earn a promotion to a higher level position.','Displays a high level of emotional intelligence.'),
(500,6320001556,6320001882,'2020-12-19','2020 Annual Review',4.2,'Meets Expectations','Resourcefulness','Presentation Skills','Provide access to networking and mentorship programs.','Time management workshops','Earn a promotion to a higher level position.','Consistently meets deadlines and deliverables.'),
(637,6320001557,6320001784,'2020-12-03','2020 Annual Review',2.3,'Below Expectations','Sales and Marketing Skills','Professional Development Training','Provide opportunities for leadership development and skill-building.','Coaching and mentoring programs','Receive recognition as an industry thought leader.','Exceeds expectations in all key performance areas.'),
(665,6320001558,6320001711,'2020-09-11','2020 Annual Review',4.7,'Exceeds Expectations','Team Collaboration','Risk Assessment and Management','Support work-life balance initiatives.','Performance appraisal and feedback training','Become a sought-after speaker or presenter at industry events.','Demonstrates a strong understanding of industry trends and best practices.'),
(543,6320001559,6320001726,'2020-11-23','2020 Annual Review',3.8,'Meets Expectations','Decision Making','Presentation Skills','Encourage a growth mindset and willingness to take on new challenges.','Health and wellness initiatives and workshops','Develop and implement a successful employee engagement program.','Successfully adapts to changing business needs.'),
(799,6320001560,6320001813,'2020-09-03','2020 Annual Review',4.4,'Meets Expectations','Self-Motivation','Professionalism and Etiquette','Support mental health awareness and resources.','Project management training','Lead a major organizational change initiative.','Demonstrates a strong understanding of industry trends and best practices.'),
(753,6320001561,6320001873,'2020-12-03','2020 Annual Review',2.3,'Below Expectations','Negotiation Skills','Networking and Relationship Building','Provide access to career counseling and coaching services.','Cross-cultural competence workshops','Manage a department or division within the organization.','Shows a high level of adaptability to change.'),
(780,6320001562,6320001769,'2020-12-12','2020 Annual Review',4,'Meets Expectations','Networking','Networking and Relationship Building','Provide resources and support to help them succeed in their role.','Market research and analysis training','Develop and execute a successful strategic plan.','Successfully manages and resolves conflicts.'),
(409,6320001563,6320001860,'2020-09-09','2020 Annual Review',3.8,'Meets Expectations','Communication Skills','Sales and Marketing Strategies','Recognize and reward innovation and creativity.','Innovation and creativity training','Obtain an executive leadership position within the organization.','Proactively identifies and addresses areas for improvement.'),
(723,6320001564,6320001754,'2020-10-05','2020 Annual Review',2.7,'Below Expectations','Goal Setting and Achievement','Customer Relationship Management','Encourage participation in industry conferences and networking events.','Customer service excellence workshops','Manage a department or division within the organization.','Consistently delivers high-quality work.'),
(549,6320001565,6320001813,'2020-10-14','2020 Annual Review',2.3,'Below Expectations','Attention Management','Self-Motivation and Initiative','Support work-life balance initiatives.','Adaptability to change training','Create and implement a successful corporate social responsibility program.','Demonstrates a strong understanding of industry trends and best practices.'),
(454,6320001566,6320001708,'2020-12-02','2020 Annual Review',4,'Meets Expectations','Innovation','Career Development Planning','Support employee resource groups and affinity networks.','Decision-making skills refinement','Represent the company at industry conferences or events.','Consistently meets deadlines and deliverables.'),
(554,6320001567,6320001772,'2020-10-17','2020 Annual Review',3.4,'Below Expectations','Attention to Detail','Professionalism and Etiquette','Provide regular feedback on their performance.','Adaptability to change training','Spearhead a company-wide initiative or program.','Demonstrates exceptional leadership qualities.'),
(641,6320001568,6320001764,'2020-09-05','2020 Annual Review',4.8,'Exceeds Expectations','Resilience','Interpersonal Communication','Recognize and reward teamwork and collaboration.','Presentation and public speaking skills development','Develop a reputation for innovative problem-solving.','Exhibits a high level of integrity and ethics.'),
(451,6320001569,6320001714,'2020-12-22','2020 Annual Review',2.4,'Below Expectations','Project Management','Technical Proficiency Enhancement','Offer opportunities for public speaking and presentation skills training.','Delegation and empowerment training','Manage a department or division within the organization.','Actively seeks feedback and acts upon it constructively.'),
(744,6320001570,6320001682,'2020-12-03','2020 Annual Review',3.2,'Below Expectations','Coaching and Mentoring','Feedback Implementation','Encourage participation in industry conferences and networking events.','Delegation and empowerment training','Lead a major organizational change initiative.','Provides valuable insights and innovative ideas.'),
(667,6320001571,6320001781,'2020-11-04','2020 Annual Review',3.3,'Below Expectations','Flexibility','Prioritization and Time Allocation','Provide regular feedback on their performance.','Talent acquisition and retention strategies workshops','Establish a strong personal brand within the industry.','Effectively collaborates with team members.'),
(726,6320001572,6320001693,'2020-12-19','2020 Annual Review',2.9,'Below Expectations','Self-Motivation','Communication Skills (Written/Verbal)','Offer financial assistance for further education or certifications.','Health and wellness initiatives and workshops','Lead a successful merger or acquisition project.','Effectively communicates complex information to diverse audiences.'),
(558,6320001573,6320001809,'2020-10-04','2020 Annual Review',2.7,'Below Expectations','Feedback Receptiveness','Networking Abilities','Support health and wellness initiatives.','Market research and analysis training','Expand the companys market reach into new regions.','Consistently meets deadlines and deliverables.'),
(599,6320001574,6320001773,'2020-10-26','2020 Annual Review',3.3,'Below Expectations','Negotiation Skills','Cross-Cultural Competence','Recognize and address burnout or stress-related issues.','Performance appraisal and feedback training','Expand the companys market reach into new regions.','Builds strong relationships with clients and customers.'),
(431,6320001575,6320001724,'2020-11-25','2020 Annual Review',2.9,'Below Expectations','Compliance Adherence','Attention to Detail','Recognize and reward innovation and creativity.','Crisis management simulation exercises','Gain international work experience.','Displays strong problem-solving skills.'),
(581,6320001576,6320001753,'2020-10-04','2020 Annual Review',4.9,'Exceeds Expectations','Integrity','Risk Assessment and Management','Encourage participation in training programs and workshops.','Continuous learning and self-directed development encouragement','Create and implement a sustainability program.','Successfully adapts to changing business needs.'),
(689,6320001577,6320001752,'2020-10-03','2020 Annual Review',2.9,'Below Expectations','Decision Making','Presentation Skills','Provide opportunities for job rotations or temporary assignments.','Entrepreneurial mindset development programs','Become a recognized expert in a niche market or industry segment.','Demonstrates a strong commitment to company goals and objectives.'),
(441,6320001578,6320001737,'2020-10-20','2020 Annual Review',2.3,'Below Expectations','Time Management','Adaptability to Change','Encourage participation in industry-specific training programs.','Critical thinking and analytical skills development','Start a mentorship program within the organization.','Communicates effectively with colleagues and stakeholders.'),
(650,6320001579,6320001765,'2020-09-20','2020 Annual Review',4.8,'Exceeds Expectations','Strategic Thinking','Problem-Solving Techniques','Recognize and address any barriers to their success.','Sustainability and corporate social responsibility training','Develop and implement a successful employer branding strategy.','Successfully leads and manages projects.'),
(706,6320001580,6320001727,'2020-12-04','2020 Annual Review',2.1,'Below Expectations','Multitasking','Technology Adoption and Proficiency','Provide opportunities for job rotations or temporary assignments.','Sales and negotiation training','Become a published author or speaker on industry topics.','Shows a commitment to continuous improvement.'),
(424,6320001581,6320001767,'2020-10-26','2020 Annual Review',3.9,'Meets Expectations','Financial Acumen','Conflict Management Strategies','Identify areas for improvement and create action plans to address them.','Personal branding and professional image development','Obtain a leadership role within the company.','Successfully manages and resolves conflicts.'),
(468,6320001582,6320001823,'2020-12-06','2020 Annual Review',2.4,'Below Expectations','Innovation','Interpersonal Communication','Provide access to resources for personal and professional development.','Career development planning sessions','Obtain an executive leadership position within the organization.','Displays resilience in challenging situations.'),
(587,6320001583,6320001878,'2020-09-01','2020 Annual Review',4.1,'Meets Expectations','Team Collaboration','Interpersonal Communication','Support health and wellness initiatives.','Coaching and mentoring programs','Develop and implement a successful employer branding strategy.','Communicates effectively with colleagues and stakeholders.'),
(728,6320001584,6320001896,'2020-11-17','2020 Annual Review',4.5,'Exceeds Expectations','Attention Management','Risk Assessment and Management','Support work-life balance initiatives.','Cross-cultural competence workshops','Gain international work experience.','Demonstrates a strong understanding of industry trends and best practices.'),
(563,6320001585,6320001825,'2020-11-13','2020 Annual Review',2.7,'Below Expectations','Emotional Intelligence','Conflict Resolution Techniques','Provide opportunities for leadership development and skill-building.','Effective communication training','Lead a successful digital transformation initiative.','Takes responsibility for personal and professional growth.'),
(469,6320001586,6320001801,'2020-11-10','2020 Annual Review',2.6,'Below Expectations','Resourcefulness','Goal Setting and Achievement','Support employee resource groups and affinity networks.','Change management strategies workshops','Obtain recognition as a top employer in the industry.','Displays a high level of emotional intelligence.'),
(705,6320001587,6320001898,'2020-09-14','2020 Annual Review',3.1,'Below Expectations','Continuous Learning','Continuous Learning and Skill Enhancement','Encourage participation in industry conferences and networking events.','Remote work and virtual collaboration training','Complete advanced education or certification.','Exemplifies the companys core values in actions.'),
(405,6320001588,6320001763,'2020-12-06','2020 Annual Review',3.6,'Meets Expectations','Continuous Learning','Creativity and Innovation','Provide opportunities for rotational assignments.','Public relations and media management training','Develop and implement a successful talent acquisition strategy.','Consistently demonstrates professionalism in all interactions.'),
(743,6320001589,6320001754,'2020-10-27','2020 Annual Review',2.5,'Below Expectations','Innovation','Career Development Planning','Foster a culture of continuous improvement and learning.','Career development planning sessions','Lead diversity and inclusion initiatives within the company.','Successfully meets or exceeds all performance targets.'),
(653,6320001590,6320001693,'2020-09-22','2020 Annual Review',3.1,'Below Expectations','Conflict Management','Emotional Intelligence','Provide access to career counseling and coaching services.','Supply chain management workshops','Lead a successful corporate rebranding effort.','Shows a high level of adaptability to change.'),
(300,6320001591,6320001685,'2020-10-22','2020 Annual Review',3,'Below Expectations','Sales and Marketing Skills','Continuous Learning and Skill Enhancement','Conduct performance evaluations based on predefined criteria.','Market research and analysis training','Obtain an executive leadership position within the organization.','Actively seeks feedback and acts upon it constructively.'),
(383,6320001592,6320001887,'2020-11-16','2020 Annual Review',3.2,'Below Expectations','Integrity','Resilience and Grit','Encourage participation in industry-specific training programs.','Technical skills enhancement programs','Obtain an executive leadership position within the organization.','Exemplifies the companys core values in actions.'),
(372,6320001593,6320001698,'2020-12-07','2020 Annual Review',3.3,'Below Expectations','Stakeholder Management','Stress Reduction Techniques','Offer incentives for achieving performance goals.','Sustainability and corporate social responsibility training','Create and implement a sustainability program.','Shows a high level of adaptability to change.'),
(367,6320001594,6320001729,'2020-12-02','2020 Annual Review',4.3,'Meets Expectations','Attention Management','Critical Thinking Skills','Support mental health awareness and resources.','Cross-cultural competence workshops','Drive significant cost savings or revenue growth for the company.','Effectively collaborates with team members.'),
(338,6320001595,6320001720,'2020-09-26','2020 Annual Review',4.3,'Meets Expectations','Customer Focus','Delegation and Empowerment','Establish regular check-ins to track progress and address any concerns.','Entrepreneurial mindset development programs','Lead a successful merger or acquisition project.','Actively seeks feedback and acts upon it constructively.'),
(370,6320001596,6320001751,'2020-11-18','2020 Annual Review',2.5,'Below Expectations','Organizational Skills','Networking and Relationship Building','Support employee-driven innovation initiatives.','Talent acquisition and retention strategies workshops','Lead a successful corporate rebranding effort.','Displays a high level of emotional intelligence.'),
(375,6320001597,6320001895,'2020-11-04','2020 Annual Review',4.5,'Exceeds Expectations','Adaptation to Change','Conflict Prevention','Encourage participation in training programs and workshops.','Time management workshops','Secure funding for a new business unit or project.','Exhibits a high level of integrity and ethics.'),
(343,6320001598,6320001789,'2020-10-21','2020 Annual Review',3.2,'Below Expectations','Empathy','Self-Motivation and Initiative','Support diversity and inclusion initiatives.','Supply chain management workshops','Lead diversity and inclusion initiatives within the company.','Builds and maintains a strong network of professional contacts.'),
(400,6320001599,6320001753,'2020-11-13','2020 Annual Review',4.5,'Exceeds Expectations','Cross-Cultural Competence','Continuous Learning and Skill Enhancement','Offer incentives for achieving performance goals.','Decision-making skills refinement','Establish a reputation for exceptional customer service.','Actively seeks feedback and acts upon it constructively.');


select * from review;

-- (4) ProbationEmployeesTable Creation
CREATE TABLE IF NOT EXISTS ProbationEmployeesTraining (
    TrainingID INT PRIMARY KEY,
    EmployeeID BIGINT,
    TrainingType VARCHAR(100),
    TrainingDate DATE,
    CompletionStatus VARCHAR(20),
    FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

INSERT INTO ProbationEmployeesTraining (TrainingID,EmployeeID,TrainingType,TrainingDate,CompletionStatus)
VALUES
(5437955,6320001500,'Leadership Development Workshops','2020-06-19','Completed'),
(5716484,6320001501,'Communication Skills Training','2020-02-01','Pending'),
(5978902,6320001502,'Conflict Resolution Seminars','2020-06-01','Completed'),
(5957408,6320001503,'Emotional Intelligence Workshops','2020-03-06','Pending'),
(5985911,6320001504,'Time Management Courses','2020-01-19','Pending'),
(5228456,6320001505,'Project Management Training Programs','2020-02-02','Pending'),
(5906963,6320001506,'Decision-Making Skills Workshops','2020-03-05','Completed'),
(5950647,6320001507,'Team Building Retreats','2020-05-23','Completed'),
(5271435,6320001508,'Change Management Workshops','2020-05-14','Completed'),
(5815676,6320001509,'Diversity and Inclusion Training','2020-03-26','Completed'),
(5705443,6320001510,'Sales and Negotiation Workshops','2020-03-15','Completed'),
(5541692,6320001511,'Customer Service Excellence Training','2020-03-14','Pending'),
(5235222,6320001512,'Presentation Skills Workshops','2020-06-12','Pending'),
(5845655,6320001513,'Problem-Solving Techniques Training','2020-04-11','Pending'),
(5655361,6320001514,'Strategic Planning Seminars','2020-01-04','Pending'),
(5964772,6320001515,'Financial Literacy Workshops','2020-04-03','Pending'),
(5257822,6320001516,'Innovation and Creativity Training','2020-05-13','Completed'),
(5927262,6320001517,'Technical Skills Enhancement Programs','2020-01-15','Completed'),
(5100689,6320001518,'Cross-Cultural Competence Training','2020-05-07','Pending'),
(5705496,6320001519,'Feedback Giving and Receiving Workshops','2020-05-01','Pending'),
(5557268,6320001520,'Resilience Building Seminars','2020-06-19','Pending'),
(5376864,6320001521,'Leadership Coaching Programs','2020-02-10','Pending'),
(5827618,6320001522,'Networking and Relationship Building Workshops','2020-04-16','Pending'),
(5739998,6320001523,'Performance Management Training','2020-03-17','Completed'),
(5744643,6320001524,'Change Leadership Workshops','2020-04-25','Completed'),
(5975754,6320001525,'Goal Setting and Achievement Training','2020-02-10','Completed'),
(5828103,6320001526,'Assertiveness Training','2020-06-08','Completed'),
(5387169,6320001527,'Critical Thinking Skills Workshops','2020-04-21','Completed'),
(5686175,6320001528,'Career Development Planning Sessions','2020-06-18','Completed'),
(5723709,6320001529,'Technology Adoption Workshops','2020-06-22','Pending'),
(5338223,6320001530,'Public Relations and Media Management Training','2020-03-17','Completed'),
(5203751,6320001531,'Crisis Management Simulations','2020-01-27','Completed'),
(5807351,6320001532,'Ethical Decision-Making Workshops','2020-01-26','Pending'),
(5181466,6320001533,'Regulatory Compliance Training','2020-01-17','Pending'),
(5009590,6320001534,'Supply Chain Management Workshops','2020-04-21','Pending'),
(5355752,6320001535,'Market Research and Analysis Training','2020-05-05','Pending'),
(5114585,6320001536,'Talent Acquisition Strategies Workshops','2020-03-19','Completed'),
(5567985,6320001537,'Remote Work and Virtual Collaboration Training','2020-05-11','Pending'),
(5384297,6320001538,'Health and Wellness Initiatives','2020-06-01','Completed'),
(5309424,6320001539,'Entrepreneurial Mindset Development Programs','2020-04-15','Completed'),
(5176744,6320001540,'Sustainability and Corporate Social Responsibility Training','2020-03-06','Completed'),
(5752911,6320001541,'Succession Planning Workshops','2020-02-06','Pending'),
(5855279,6320001542,'Performance Appraisal and Feedback Training','2020-01-09','Pending'),
(5922637,6320001543,'Conflict Resolution Through Mediation Workshops','2020-01-22','Pending'),
(5826399,6320001544,'Data Analysis and Interpretation Training','2020-06-06','Completed'),
(5294996,6320001545,'Continuous Learning Programs','2020-01-09','Pending'),
(5855589,6320001546,'Personal Branding and Visibility Workshops','2020-03-22','Pending'),
(5011760,6320001547,'Entrepreneurial Mindset Development Programs','2020-02-25','Completed'),
(5439811,6320001548,'Remote Work and Virtual Collaboration Training','2020-03-08','Completed'),
(5659190,6320001549,'Market Research and Analysis Training','2020-06-05','Completed'),
(5042775,6320001550,'Time Management Courses','2020-01-13','Completed'),
(5076822,6320001551,'Cross-Cultural Competence Training','2020-04-02','Pending'),
(5038434,6320001552,'Sustainability and Corporate Social Responsibility Training','2020-04-28','Completed'),
(5056359,6320001553,'Critical Thinking Skills Workshops','2020-01-08','Pending'),
(5271499,6320001554,'Project Management Training Programs','2020-06-05','Pending'),
(5151136,6320001555,'Conflict Resolution Seminars','2020-05-21','Completed'),
(5012818,6320001556,'Goal Setting and Achievement Training','2020-05-04','Completed'),
(5939684,6320001557,'Continuous Learning Programs','2020-02-02','Completed'),
(5326524,6320001558,'Goal Setting and Achievement Training','2020-01-01','Pending'),
(5970578,6320001559,'Remote Work and Virtual Collaboration Training','2020-06-02','Completed'),
(5049915,6320001560,'Resilience Building Seminars','2020-05-06','Completed'),
(5874315,6320001561,'Market Research and Analysis Training','2020-06-04','Pending'),
(5651740,6320001562,'Cross-Cultural Competence Training','2020-01-02','Pending'),
(5149100,6320001563,'Strategic Planning Seminars','2020-04-08','Completed'),
(5066197,6320001564,'Communication Skills Training','2020-06-17','Completed'),
(5064896,6320001565,'Customer Service Excellence Training','2020-03-21','Pending'),
(5653640,6320001566,'Career Development Planning Sessions','2020-04-17','Completed'),
(5239680,6320001567,'Conflict Resolution Seminars','2020-06-19','Completed'),
(5161562,6320001568,'Ethical Decision-Making Workshops','2020-04-07','Completed'),
(5255950,6320001569,'Change Management Workshops','2020-05-02','Completed'),
(5313341,6320001570,'Technology Adoption Workshops','2020-01-25','Completed'),
(5808876,6320001571,'Communication Skills Training','2020-04-02','Completed'),
(5500109,6320001572,'Change Management Workshops','2020-05-21','Pending'),
(5974507,6320001573,'Performance Appraisal and Feedback Training','2020-06-15','Pending'),
(5325168,6320001574,'Communication Skills Training','2020-01-25','Completed'),
(5202313,6320001575,'Change Leadership Workshops','2020-05-13','Completed'),
(5568238,6320001576,'Health and Wellness Initiatives','2020-05-10','Pending'),
(5512910,6320001577,'Strategic Planning Seminars','2020-03-04','Pending'),
(5585709,6320001578,'Networking and Relationship Building Workshops','2020-04-20','Pending'),
(5193706,6320001579,'Problem-Solving Techniques Training','2020-06-04','Completed'),
(5348456,6320001580,'Performance Appraisal and Feedback Training','2020-01-05','Completed'),
(5992694,6320001581,'Resilience Building Seminars','2020-01-03','Completed'),
(5185187,6320001582,'Performance Management Training','2020-03-27','Pending'),
(5109990,6320001583,'Emotional Intelligence Workshops','2020-03-15','Pending'),
(5091983,6320001584,'Problem-Solving Techniques Training','2020-01-26','Pending'),
(5970253,6320001585,'Personal Branding and Visibility Workshops','2020-02-05','Completed'),
(5429671,6320001586,'Ethical Decision-Making Workshops','2020-02-10','Pending'),
(5718710,6320001587,'Public Relations and Media Management Training','2020-01-14','Completed'),
(5670302,6320001588,'Continuous Learning Programs','2020-04-16','Completed'),
(5311786,6320001589,'Networking and Relationship Building Workshops','2020-04-12','Pending'),
(5137458,6320001590,'Technology Adoption Workshops','2020-04-04','Pending'),
(5055184,6320001591,'Market Research and Analysis Training','2020-05-07','Pending'),
(5918987,6320001592,'Presentation Skills Workshops','2020-05-13','Pending'),
(5767330,6320001593,'Health and Wellness Initiatives','2020-02-27','Pending'),
(5287759,6320001594,'Resilience Building Seminars','2020-01-28','Completed'),
(5629514,6320001595,'Strategic Planning Seminars','2020-05-19','Completed'),
(5291299,6320001596,'Financial Literacy Workshops','2020-06-21','Pending'),
(5154177,6320001597,'Market Research and Analysis Training','2020-04-12','Completed'),
(5658686,6320001598,'Change Leadership Workshops','2020-04-08','Completed'),
(5626956,6320001599,'Conflict Resolution Through Mediation Workshops','2020-01-02','Pending');

select * from ProbationEmployeesTraining;

-- (5) Table to store department information
CREATE TABLE IF NOT EXISTS Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

INSERT INTO Department 
VALUES 
(1, 'Inc'),
(2, 'PLC'),
(3, 'LLC'),
(4, 'Ltd'),
(5, 'LLC'),
(6, 'LLC'),
(7, 'Ltd'),
(8, 'LLC'),
(9, 'and Sons');

-- (6) Table to track attendance of employees
CREATE TABLE IF NOT EXISTS Attendance (
    AttendanceID INT PRIMARY KEY,
    EmployeeID BIGINT,
    AttendanceDate DATE,
    StartTime TIME,
    EndTime TIME,
    FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

INSERT INTO Attendance (    AttendanceID,    EmployeeID,    AttendanceDate,    StartTime,    EndTime) VALUES
(15000104,6320001500,'2020-01-04','09:44:05','19:09:29'),
(15010109,6320001501,'2020-01-09','10:16:03','19:09:08'),
(15020109,6320001502,'2020-01-09','09:02:36','19:45:14'),
(15030128,6320001503,'2020-01-28','10:00:38','19:36:04'),
(15040126,6320001504,'2020-01-26','08:36:01','18:43:11'),
(15050128,6320001505,'2020-01-28','08:16:31','19:42:23'),
(15060103,6320001506,'2020-01-03','10:40:04','19:17:39'),
(15070108,6320001507,'2020-01-08','08:32:42','18:18:15'),
(15080122,6320001508,'2020-01-22','08:53:54','18:44:11'),
(15090109,6320001509,'2020-01-09','10:23:14','19:27:12'),
(15100108,6320001510,'2020-01-08','10:34:42','18:03:24'),
(15110119,6320001511,'2020-01-19','09:15:06','19:03:15'),
(15120126,6320001512,'2020-01-26','08:43:27','19:01:55'),
(15130111,6320001513,'2020-01-11','10:41:47','19:18:32'),
(15140123,6320001514,'2020-01-23','10:17:52','19:01:19'),
(15150102,6320001515,'2020-01-02','09:31:38','19:14:33'),
(15160117,6320001516,'2020-01-17','08:39:01','18:33:03'),
(15170124,6320001517,'2020-01-24','08:37:23','18:56:03'),
(15180109,6320001518,'2020-01-09','09:33:10','19:42:27'),
(15190109,6320001519,'2020-01-09','10:51:04','18:24:56'),
(15200106,6320001520,'2020-01-06','09:29:21','18:06:21'),
(15210102,6320001521,'2020-01-02','10:13:45','19:54:23'),
(15220123,6320001522,'2020-01-23','10:08:39','19:39:52'),
(15230114,6320001523,'2020-01-14','08:27:02','18:17:27'),
(15240113,6320001524,'2020-01-13','10:38:45','18:18:45'),
(15250123,6320001525,'2020-01-23','09:48:25','18:22:39'),
(15260101,6320001526,'2020-01-01','08:42:22','19:52:52'),
(15270126,6320001527,'2020-01-26','10:00:13','19:34:59'),
(15280114,6320001528,'2020-01-14','08:51:38','18:00:06'),
(15290113,6320001529,'2020-01-13','09:55:37','19:32:06'),
(15300122,6320001530,'2020-01-22','08:33:32','19:22:47'),
(15310118,6320001531,'2020-01-18','09:25:36','19:49:09'),
(15320113,6320001532,'2020-01-13','09:54:31','19:48:01'),
(15330108,6320001533,'2020-01-08','08:26:31','19:39:06'),
(15340109,6320001534,'2020-01-09','08:02:42','19:26:30'),
(15350121,6320001535,'2020-01-21','09:39:00','18:25:55'),
(15360103,6320001536,'2020-01-03','09:59:52','18:39:26'),
(15370111,6320001537,'2020-01-11','08:51:48','19:01:09'),
(15380124,6320001538,'2020-01-24','08:58:38','18:35:01'),
(15390111,6320001539,'2020-01-11','08:54:27','19:08:39'),
(15400118,6320001540,'2020-01-18','08:28:41','19:08:15'),
(15410107,6320001541,'2020-01-07','10:55:27','19:23:07'),
(15420112,6320001542,'2020-01-12','09:01:07','19:47:53'),
(15430103,6320001543,'2020-01-03','10:12:17','19:11:16'),
(15440125,6320001544,'2020-01-25','08:17:22','19:32:21'),
(15450121,6320001545,'2020-01-21','10:11:59','19:24:33'),
(15460111,6320001546,'2020-01-11','10:56:04','19:14:52'),
(15470121,6320001547,'2020-01-21','08:24:17','19:20:41'),
(15480112,6320001548,'2020-01-12','09:45:30','19:14:03'),
(15490107,6320001549,'2020-01-07','09:50:46','19:37:51'),
(15500121,6320001550,'2020-01-21','08:35:03','19:44:50'),
(15510122,6320001551,'2020-01-22','09:28:51','18:23:53'),
(15520115,6320001552,'2020-01-15','08:29:45','18:23:22'),
(15530102,6320001553,'2020-01-02','10:17:16','19:56:40'),
(15540115,6320001554,'2020-01-15','09:10:29','19:58:28'),
(15550123,6320001555,'2020-01-23','09:10:55','19:45:18'),
(15560117,6320001556,'2020-01-17','08:45:05','19:09:46'),
(15570112,6320001557,'2020-01-12','09:37:22','18:59:34'),
(15580116,6320001558,'2020-01-16','09:34:21','18:21:26'),
(15590114,6320001559,'2020-01-14','08:08:06','18:11:08'),
(15600107,6320001560,'2020-01-07','09:29:43','18:26:21'),
(15610105,6320001561,'2020-01-05','10:36:43','18:46:17'),
(15620118,6320001562,'2020-01-18','10:23:03','19:08:52'),
(15630117,6320001563,'2020-01-17','10:30:27','18:27:46'),
(15640103,6320001564,'2020-01-03','09:24:31','19:48:58'),
(15650107,6320001565,'2020-01-07','09:31:41','19:07:01'),
(15660112,6320001566,'2020-01-12','09:33:05','19:01:03'),
(15670104,6320001567,'2020-01-04','10:15:11','19:00:45'),
(15680113,6320001568,'2020-01-13','08:55:57','19:36:44'),
(15690123,6320001569,'2020-01-23','10:07:37','19:08:01'),
(15700124,6320001570,'2020-01-24','08:38:50','19:05:32'),
(15710105,6320001571,'2020-01-05','08:48:39','18:33:49'),
(15720109,6320001572,'2020-01-09','10:46:48','18:27:10'),
(15730114,6320001573,'2020-01-14','09:59:22','18:59:57'),
(15740124,6320001574,'2020-01-24','10:43:36','19:44:18'),
(15750117,6320001575,'2020-01-17','09:27:36','19:45:36'),
(15760101,6320001576,'2020-01-01','08:36:02','18:49:46'),
(15770117,6320001577,'2020-01-17','09:54:47','18:57:23'),
(15780110,6320001578,'2020-01-10','10:52:40','19:09:44'),
(15790106,6320001579,'2020-01-06','08:48:08','18:32:38'),
(15800116,6320001580,'2020-01-16','09:41:40','19:35:39'),
(15810118,6320001581,'2020-01-18','09:27:15','19:00:50'),
(15820108,6320001582,'2020-01-08','10:25:00','19:35:04'),
(15830103,6320001583,'2020-01-03','10:47:18','19:04:41'),
(15840109,6320001584,'2020-01-09','10:50:34','18:08:53'),
(15850125,6320001585,'2020-01-25','08:26:36','18:37:28'),
(15860125,6320001586,'2020-01-25','08:13:48','18:16:58'),
(15870128,6320001587,'2020-01-28','10:57:12','18:22:12'),
(15880117,6320001588,'2020-01-17','09:58:38','19:31:29'),
(15890115,6320001589,'2020-01-15','08:31:17','19:28:23'),
(15900111,6320001590,'2020-01-11','08:12:13','19:32:52'),
(15910119,6320001591,'2020-01-19','10:47:20','18:39:04'),
(15920114,6320001592,'2020-01-14','08:50:47','18:04:25'),
(15930106,6320001593,'2020-01-06','08:17:28','18:58:53'),
(15940123,6320001594,'2020-01-23','10:43:48','19:07:32'),
(15950121,6320001595,'2020-01-21','08:25:01','19:23:09'),
(15960118,6320001596,'2020-01-18','10:33:46','19:39:23'),
(15970104,6320001597,'2020-01-04','10:50:51','18:15:12'),
(15980117,6320001598,'2020-01-17','08:02:41','18:10:46'),
(15990112,6320001599,'2020-01-12','09:15:52','19:14:01'),
(15000226,6320001500,'2020-02-26','08:53:31','19:56:53'),
(15010208,6320001501,'2020-02-08','09:33:25','19:37:52'),
(15020226,6320001502,'2020-02-26','08:29:47','19:20:52'),
(15030223,6320001503,'2020-02-23','08:24:46','19:45:50'),
(15040226,6320001504,'2020-02-26','10:32:40','18:47:02'),
(15050211,6320001505,'2020-02-11','09:00:55','19:14:05'),
(15060223,6320001506,'2020-02-23','09:07:55','19:02:54'),
(15070222,6320001507,'2020-02-22','09:45:28','19:01:32'),
(15080224,6320001508,'2020-02-24','09:39:23','18:02:40'),
(15090212,6320001509,'2020-02-12','08:07:04','19:50:24'),
(15100212,6320001510,'2020-02-12','08:39:51','19:56:47'),
(15110217,6320001511,'2020-02-17','08:39:47','19:49:50'),
(15120218,6320001512,'2020-02-18','08:38:54','19:35:18'),
(15130206,6320001513,'2020-02-06','08:55:47','18:34:53'),
(15140205,6320001514,'2020-02-05','08:20:54','19:51:35'),
(15150221,6320001515,'2020-02-21','09:06:49','18:18:45'),
(15160217,6320001516,'2020-02-17','08:48:29','19:18:31'),
(15170222,6320001517,'2020-02-22','10:16:13','19:32:05'),
(15180213,6320001518,'2020-02-13','09:46:25','19:33:11'),
(15190210,6320001519,'2020-02-10','10:36:22','18:35:18'),
(15200226,6320001520,'2020-02-26','10:53:40','18:31:23'),
(15210221,6320001521,'2020-02-21','10:35:31','19:58:08'),
(15220213,6320001522,'2020-02-13','08:41:59','18:06:12'),
(15230224,6320001523,'2020-02-24','08:56:42','18:12:29'),
(15240224,6320001524,'2020-02-24','08:54:22','18:14:52'),
(15250218,6320001525,'2020-02-18','08:34:36','18:08:07'),
(15260219,6320001526,'2020-02-19','09:49:26','18:04:31'),
(15270210,6320001527,'2020-02-10','09:54:31','18:52:52'),
(15280221,6320001528,'2020-02-21','08:28:31','19:32:26'),
(15290207,6320001529,'2020-02-07','09:21:42','19:27:35'),
(15300217,6320001530,'2020-02-17','08:18:51','18:22:42'),
(15310222,6320001531,'2020-02-22','08:23:24','18:12:05'),
(15320221,6320001532,'2020-02-21','09:38:35','18:02:09'),
(15330207,6320001533,'2020-02-07','08:46:26','18:16:51'),
(15340224,6320001534,'2020-02-24','09:21:13','18:11:32'),
(15350209,6320001535,'2020-02-09','10:19:05','19:49:40'),
(15360203,6320001536,'2020-02-03','08:56:20','19:11:07'),
(15370227,6320001537,'2020-02-27','10:00:25','19:08:41'),
(15380223,6320001538,'2020-02-23','10:47:27','18:26:45'),
(15390206,6320001539,'2020-02-06','08:20:32','18:53:15'),
(15400209,6320001540,'2020-02-09','09:56:46','18:00:00'),
(15410226,6320001541,'2020-02-26','08:29:44','18:54:01'),
(15420224,6320001542,'2020-02-24','09:08:32','18:51:24'),
(15430226,6320001543,'2020-02-26','09:27:25','19:33:42'),
(15440226,6320001544,'2020-02-26','09:35:29','18:48:05'),
(15450217,6320001545,'2020-02-17','09:51:49','18:18:05'),
(15460218,6320001546,'2020-02-18','10:05:42','19:38:12'),
(15470219,6320001547,'2020-02-19','10:06:13','18:09:41'),
(15480202,6320001548,'2020-02-02','10:43:40','18:01:48'),
(15490225,6320001549,'2020-02-25','08:41:11','19:52:16'),
(15500203,6320001550,'2020-02-03','08:15:38','18:32:46'),
(15510206,6320001551,'2020-02-06','10:29:39','18:05:11'),
(15520211,6320001552,'2020-02-11','09:51:43','18:11:26'),
(15530215,6320001553,'2020-02-15','09:58:14','19:35:53'),
(15540227,6320001554,'2020-02-27','09:38:52','19:59:28'),
(15550211,6320001555,'2020-02-11','10:44:26','18:20:45'),
(15560220,6320001556,'2020-02-20','10:32:36','18:21:47'),
(15570225,6320001557,'2020-02-25','10:42:35','19:10:29'),
(15580203,6320001558,'2020-02-03','09:03:05','19:22:13'),
(15590211,6320001559,'2020-02-11','09:06:25','18:30:11'),
(15600210,6320001560,'2020-02-10','09:39:31','19:36:30'),
(15610227,6320001561,'2020-02-27','09:05:26','18:39:42'),
(15620215,6320001562,'2020-02-15','10:30:42','19:18:17'),
(15630218,6320001563,'2020-02-18','09:31:21','18:09:12'),
(15640209,6320001564,'2020-02-09','10:55:25','18:13:45'),
(15650222,6320001565,'2020-02-22','08:53:59','18:12:50'),
(15660217,6320001566,'2020-02-17','10:58:22','19:25:41'),
(15670222,6320001567,'2020-02-22','08:44:54','19:26:22'),
(15680209,6320001568,'2020-02-09','08:56:53','19:37:37'),
(15690226,6320001569,'2020-02-26','08:34:24','18:08:20'),
(15700219,6320001570,'2020-02-19','08:00:27','18:25:09'),
(15710201,6320001571,'2020-02-01','10:42:34','19:07:51'),
(15720214,6320001572,'2020-02-14','09:53:52','18:05:22'),
(15730212,6320001573,'2020-02-12','08:16:51','19:07:42'),
(15740227,6320001574,'2020-02-27','08:36:37','18:05:48'),
(15750221,6320001575,'2020-02-21','09:46:37','18:08:46'),
(15760210,6320001576,'2020-02-10','08:07:31','18:28:39'),
(15770228,6320001577,'2020-02-28','08:35:35','18:11:12'),
(15780211,6320001578,'2020-02-11','10:14:56','19:43:05'),
(15790223,6320001579,'2020-02-23','09:07:02','19:57:23'),
(15800224,6320001580,'2020-02-24','08:52:27','19:43:49'),
(15810226,6320001581,'2020-02-26','10:55:44','19:04:17'),
(15820227,6320001582,'2020-02-27','10:41:27','19:08:26'),
(15830204,6320001583,'2020-02-04','09:14:22','18:32:05'),
(15840221,6320001584,'2020-02-21','08:53:50','18:09:34'),
(15850217,6320001585,'2020-02-17','08:05:15','19:25:20'),
(15860226,6320001586,'2020-02-26','08:38:10','19:23:21'),
(15870209,6320001587,'2020-02-09','08:10:51','18:25:56'),
(15880208,6320001588,'2020-02-08','08:02:53','18:30:10'),
(15890207,6320001589,'2020-02-07','08:38:50','19:00:05'),
(15900220,6320001590,'2020-02-20','10:15:32','19:54:21'),
(15910210,6320001591,'2020-02-10','09:04:23','18:20:50'),
(15920203,6320001592,'2020-02-03','08:02:46','18:20:41'),
(15930227,6320001593,'2020-02-27','08:41:09','19:00:08'),
(15940213,6320001594,'2020-02-13','10:59:01','18:45:30'),
(15950227,6320001595,'2020-02-27','08:03:57','19:22:10'),
(15960209,6320001596,'2020-02-09','09:32:04','18:45:47'),
(15970225,6320001597,'2020-02-25','09:13:14','18:31:10'),
(15980227,6320001598,'2020-02-27','08:20:18','19:20:46'),
(15990223,6320001599,'2020-02-23','10:08:29','18:14:09');

select * from attendance;

-- (7) Table to log historical events or changes

CREATE TABLE IF NOT EXISTS HistoryLog_EmployeeInformation (
    LogID INT PRIMARY KEY auto_increment,
    LogType VARCHAR(100),
    LogDate DATETIME,
    LogDetails TEXT,
    EmployeeID BIGINT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

-- (8) Table to track Pay Grades
CREATE TABLE IF NOT EXISTS Pay_Grades(
PayGradeID VARCHAR(100) PRIMARY KEY ,
GradeName VARCHAR(100),
MinSalary DECIMAL(15,2),
MaxSalary DECIMAL(15,2));

INSERT INTO Pay_Grades VALUES ('PG001', 'Financial manager', 36747.31, 53107.44),
('PG002', 'Risk analyst', 63704.07, 88679.23),
('PG003', 'Drilling engineer', 73123.83, 85742.86),
('PG004', 'Office manager', 59656.2, 81422.35),
('PG005', 'Building surveyor', 63549.49, 86440.81),
 ('PG006', 'Actuary', 36866.8, 49849.31),
('PG007', 'Secretary/administrator', 71527.31, 83527.69),
('PG008', 'Financial risk analyst', 47585.97, 81995.3),
('PG009', 'Translator', 75275.77, 101249.75),
('PG0010', 'Media planner', 70018.65, 85729.64);

SELECT * FROM pAY_gRADES;

-- (9) Table to track Benefits provided by the company
 CREATE TABLE IF NOT EXISTS Benefits(
BenefitID VARCHAR(100) PRIMARY KEY,
PayGradeID VARCHAR(100),
BenefitType VARCHAR(100),
BenefitAmount DECIMAL(15,2),
FOREIGN KEY (PayGradeID) REFERENCES Pay_Grades(PayGradeID) 
);

INSERT INTO Benefits VALUES
('B001', 'PG001', 'Health Insurance - Bronze', 5000),
('B002', 'PG002', 'Health Insurance - Silver', 6000),
('B003', 'PG003', 'Health Insurance - Silver Plus', 7000),
('B004', 'PG004', 'Health Insurance - Gold', 8500),
('B005', 'PG005', 'Health Insurance - Gold Plus', 10000),
('B006', 'PG006', 'Health Insurance - Platinum', 13000),
('B007', 'PG003', 'Tuition Reimbursement', 13000),
('B008', 'PG004', 'Tuition Reimbursement - Plus', 18000),
('B009', 'PG001', 'Retirement Plans - Junior', 3000),
('B010', 'PG002', 'Retirement Plans - Intermediate', 4000),
('B011', 'PG003', 'Retirement Plans - Senior', 6000),
('B012', 'PG004', 'Retirement Plans - Managerial', 9000),
('B013', 'PG005', 'Retirement Plans - Upper Managerial', 12000),
('B014', 'PG006', 'Retirement Plans - Executive', 18000);

select * from benefits;

-- (10) Table to track Deductions provided by the company
CREATE TABLE IF NOT EXISTS Deductions(
    DeductionID VARCHAR(100) PRIMARY KEY,
    DeductionType VARCHAR(100),
    DeductionRate DECIMAL(15,2)
);

INSERT INTO Deductions VALUES
('D001', 'Federal Tax Rate Bracket @ 12%', 12.00),
('D002', 'Federal Tax Rate Bracket @ 22%', 22.00),
('D003', 'Federal Tax Rate Bracket @ 24%', 24.00),
('D004', 'Federal Tax Rate Bracket @ 32%', 32.00),
('D005', 'Federal Tax Rate Bracket @ 35%', 35.00),
('D006', 'Federal Tax Rate Bracket @ 37%', 37.00);

select * from deductions;
-- (11) Table to track Salaries and related components
CREATE TABLE IF NOT EXISTS Salaries(
EmployeeID BIGINT,
SalaryID BIGINT PRIMARY KEY NOT NULL,
PayGradeID VARCHAR(250),
BaseSalary DECIMAL(10,2),
Bonus DECIMAL(10,2),
DeductionID VARCHAR(250),
BenefitAmount DECIMAL(10,2),
FOREIGN KEY (PayGradeID) REFERENCES Pay_Grades(PayGradeID),
FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID),
FOREIGN KEY (DeductionID) REFERENCES Deductions(DeductionID) 
);

INSERT INTO Salaries (EmployeeID,SalaryID,PayGradeID,BaseSalary,Bonus,DeductionID,BenefitAmount) VALUES
 (6320001500,15000903,'PG009',92286.12,2501.40999999999,'D003',2807),
 (6320001501,15010902,'PG009',78051.38,2128.06,'D002',9351),
 (6320001502,15020401,'PG004',65324.15,1662.55,'D001',4947),
 (6320001503,15030702,'PG007',75646.92,1357.14999999999,'D002',9900),
 (6320001504,15040702,'PG007',80396.5,6746.09,'D002',5231),
 (6320001505,15050502,'PG005',79696.58,7582.28,'D002',4013),
 (6320001506,15060601,'PG006',41494.89,2369.3,'D001',8443),
 (6320001507,15070903,'PG009',86895.61,8143.36,'D003',9889),
 (6320001508,15080201,'PG002',65522.59,612.879999999997,'D001',5754),
 (6320001509,15090201,'PG002',64943.21,278.75,'D001',7256),
 (6320001510,15100903,'PG009',93046.58,15773.96,'D003',4973),
 (6320001511,15110302,'PG003',82811.34,3022,'D002',6012),
 (6320001512,15120401,'PG004',64342.33,3750.16,'D001',7234),
 (6320001513,15130801,'PG008',70119.32,18958.75,'D001',6986),
 (6320001514,15140601,'PG006',46264.68,310.779999999999,'D001',5267),
 (6320001515,15150402,'PG004',80620.4,16381.59,'D002',4406),
 (6320001516,15160201,'PG002',72499.73,3614.87999999999,'D001',6186),
 (6320001517,15170101,'PG001',38738.11,835.389999999999,'D001',6420),
 (6320001518,15180302,'PG003',77028.02,3131.72,'D002',2963),
 (6320001519,15190303,'PG003',83589.13,3022.42,'D003',2767),
 (6320001520,15200501,'PG005',64682.16,244.170000000006,'D001',1441),
 (6320001521,15210401,'PG004',61774.98,1349.03000000001,'D001',8087),
 (6320001522,15221001,'PG0010',52645.17,257.93,'D001',9860),
 (6320001523,15230101,'PG001',50253.9,13274.15,'D001',2059),
 (6320001524,15240802,'PG008',74781.4,13780,'D002',5291),
 (6320001525,15250303,'PG003',83785.45,7785.19,'D003',2187),
 (6320001526,15260601,'PG006',38146.38,446.68,'D001',5487),
 (6320001527,15270902,'PG009',77131.46,861.25,'D002',2540),
 (6320001528,15280501,'PG005',72952.19,8032.23,'D001',1137),
 (6320001529,15290702,'PG007',78802.83,5269.50999999999,'D002',9096),
 (6320001530,15300203,'PG002',84482.48,47.4899999999907,'D003',5328),
 (6320001531,15310903,'PG009',87569.55,2595.78,'D003',5458),
 (6320001532,15321001,'PG0010',45604.22,7992.04,'D001',9460),
 (6320001533,15330202,'PG002',78822.81,3810.69,'D002',3970),
 (6320001534,15340802,'PG008',79511.04,13169.94,'D002',1026),
 (6320001535,15350601,'PG006',43084.87,2035.45,'D001',4171),
 (6320001536,15360501,'PG005',69366.48,1969.2,'D001',3103),
 (6320001537,15370801,'PG008',57035.11,4979.99,'D001',1534),
 (6320001538,15381001,'PG0010',50956.01,12366.78,'D001',2145),
 (6320001539,15390904,'PG009',99374.75,367.020000000004,'D004',7913),
 (6320001540,15400101,'PG001',47316.06,3403.73,'D001',3778),
 (6320001541,15411001,'PG0010',39379.04,1796.29,'D001',7489),
 (6320001542,15420601,'PG006',37832.68,313.279999999999,'D001',4645),
 (6320001543,15430501,'PG005',69367.24,2255.09000000001,'D001',8126),
 (6320001544,15440801,'PG008',72526.51,9567.37,'D001',5627),
 (6320001545,15450801,'PG008',58481.79,4154.98,'D001',3429),
 (6320001546,15460402,'PG004',81379.05,5904.22,'D002',7816),
 (6320001547,15470401,'PG004',63114.46,1673.71,'D001',5480),
 (6320001548,15480904,'PG009',99474.13,13515.43,'D004',9839),
 (6320001549,15490601,'PG006',49504.09,5341.88,'D001',2325),
 (6320001550,15501001,'PG0010',49444.61,11099.18,'D001',8433),
 (6320001551,15510101,'PG001',42622.33,4251.01,'D001',8436),
 (6320001552,15520302,'PG003',76997.1,809.700000000012,'D002',8725),
 (6320001553,15530903,'PG009',91357.77,2474.42,'D003',8642),
 (6320001554,15540401,'PG004',66505.18,5970.80999999999,'D001',7623),
 (6320001555,15550903,'PG009',85629.11,3053.31,'D003',2184),
 (6320001556,15560601,'PG006',41393.07,2191.2,'D001',7943),
 (6320001557,15570202,'PG002',75099.66,7983.49000000001,'D002',7180),
 (6320001558,15580601,'PG006',38822.32,61.8700000000026,'D001',7919),
 (6320001559,15590101,'PG001',45563.51,2992.33,'D001',7336),
 (6320001560,15601001,'PG0010',49424.37,1918.47,'D001',9444),
 (6320001561,15610903,'PG009',84691.9,4740.25999999999,'D003',9317),
 (6320001562,15620701,'PG007',71987.77,319.279999999999,'D001',6778),
 (6320001563,15631001,'PG0010',48418.95,5086.21999999999,'D001',2305),
 (6320001564,15640401,'PG004',63850.92,937.669999999998,'D001',5711),
 (6320001565,15651001,'PG0010',51397.45,8286.81,'D001',8010),
 (6320001566,15660401,'PG004',72889.87,10054.99,'D001',4568),
 (6320001567,15670601,'PG006',36897.8,25.010000000002,'D001',1132),
 (6320001568,15680402,'PG004',77593.67,16991.5,'D002',8428),
 (6320001569,15690101,'PG001',44767.79,3299.68,'D001',9191),
 (6320001570,15700702,'PG007',81454.9,5774.26999999999,'D002',4138),
 (6320001571,15710801,'PG008',59074.12,4729.41,'D001',5874),
 (6320001572,15720902,'PG009',76740.37,555.179999999993,'D002',6445),
 (6320001573,15730702,'PG007',79675.44,2794.51000000001,'D002',2826),
 (6320001574,15741001,'PG0010',44258.5,4559.64,'D001',2472),
 (6320001575,15750601,'PG006',37196.16,85.6300000000047,'D001',2223),
 (6320001576,15760201,'PG002',70762.28,5529.62,'D001',4977),
 (6320001577,15771001,'PG0010',44849.61,5751.85,'D001',5788),
 (6320001578,15780601,'PG006',48257.1,8746.36,'D001',1825),
 (6320001579,15790302,'PG003',81968.38,8808.47,'D002',2335),
 (6320001580,15801001,'PG0010',39991.67,1311.42,'D001',9380),
 (6320001581,15810903,'PG009',90648.21,10007.91,'D003',8617),
 (6320001582,15821001,'PG0010',37697.01,476.870000000003,'D001',6961),
 (6320001583,15830801,'PG008',55806.68,1423.21,'D001',6960),
 (6320001584,15840903,'PG009',93614.29,5144.39,'D003',6411),
 (6320001585,15850501,'PG005',68551.79,4254.89999999999,'D001',5443),
 (6320001586,15860601,'PG006',47067.97,1391.31,'D001',5234),
 (6320001587,15870302,'PG003',81629.43,2573.15999999999,'D002',3502),
 (6320001588,15880502,'PG005',78295.74,6234.53,'D002',9836),
 (6320001589,15890303,'PG003',84192.12,3532.84999999999,'D003',6630),
 (6320001590,15900401,'PG004',64210.16,3312.83,'D001',2990),
 (6320001591,15910902,'PG009',81669.32,785.790000000008,'D002',4841),
 (6320001592,15920203,'PG002',87575.85,9079.23000000001,'D003',5915),
 (6320001593,15930601,'PG006',42055.73,2763.88,'D001',8467),
 (6320001594,15940401,'PG004',60339.87,303.720000000001,'D001',2773),
 (6320001595,15950303,'PG003',85717.33,3290.54000000001,'D003',8188),
 (6320001596,15960201,'PG002',71039.21,5095.90000000001,'D001',8879),
 (6320001597,15970202,'PG002',80764.13,14637.89,'D002',3889),
 (6320001598,15980801,'PG008',70579.99,13793.23,'D001',2089),
 (6320001599,15990601,'PG006',40805.73,3136.31,'D001',7161);

select * from salaries;

-- (12) Table to track Positions in the company

CREATE TABLE Positions (
PositionID VARCHAR(250) PRIMARY KEY NOT NULL, 
PayGradeID VARCHAR(250),
PositionTitle VARCHAR(250), 
Responsibilities VARCHAR(250), 
Qualification VARCHAR(250), 
DepartmentID INT,
FOREIGN KEY (DepartmentID) REFERENCES department(DepartmentID), 
FOREIGN KEY (PayGradeID) REFERENCES Pay_Grades(PayGradeID)
);

INSERT INTO Positions (PositionID,PayGradeID,PositionTitle,Responsibilities,Qualification,DepartmentID) VALUES
 ('15533G001','PG001','Management','Develop and implement strategic plans to achieve company goals','Bachelors degree in Science',3),
 ('13019G002','PG002','Analyst','Lead and oversee departmental operations and activities','Masters degree or MBA (Master of Business Administration)',9),
 ('16631G003','PG003','Engineering','Collaborate with cross-functional teams to drive projects forward','Relevant professional certification (e.g., CPA, PMP, SHRM-CP)',1),
 ('14365G004','PG004','Executive','Provide guidance and mentorship to team members','Strong analytical and problem-solving skills',5),
 ('19661G005','PG005','Survey','Analyze financial data and prepare reports for management review','Excellent communication and interpersonal skills',1),
 ('14731G006','PG006','Analyst','Manage client relationships and address customer inquiries','Proven leadership experience',1),
 ('11692G007','PG007','Admin','Develop and execute marketing campaigns to promote products or services','Proficiency in Microsoft Office suite',2),
 ('14088G008','PG008','Analyst','Research market trends and identify potential business opportunities','Experience with project management software (e.g., Microsoft Project)',8),
 ('11592G009','PG009','Media','Coordinate logistics and ensure timely delivery of goods or services','Knowledge of financial principles and practices',2),
 ('162560010','PG0010','Media','Maintain accurate records of transactions and financial activities','Ability to work effectively in a team environment',6),
 ('14158G002','PG002','Analyst','Conduct employee performance evaluations and provide feedback','Strong attention to detail and organizational skills',8),
 ('11831G004','PG004','Executive','Monitor and enforce compliance with company policies and regulations','Experience with data analysis and reporting tools',1),
 ('19569G006','PG006','Analyst','Develop and implement training programs for employee skill development','Knowledge of industry regulations and compliance requirements',9),
 ('17121G002','PG002','Analyst','Design and develop software applications to meet business needs','Ability to prioritize and manage multiple tasks simultaneously',1),
 ('14679G006','PG006','Analyst','Manage and maintain IT infrastructure and systems','Strong customer service orientation',9),
 ('11033G002','PG002','Analyst','Provide technical support and troubleshooting assistance to users','Proficiency in programming languages (e.g., Java, Python)',3),
 ('13089G006','PG006','Analyst','Conduct market analysis and develop pricing strategies','Experience with database management systems (e.g., SQL)',9),
 ('11927G005','PG005','Survey','Negotiate contracts and agreements with vendors and suppliers','Ability to adapt to changing priorities and deadlines',7),
 ('15637G006','PG006','Analyst','Develop and maintain relationships with key stakeholders','Knowledge of marketing principles and strategies',7),
 ('17493G007','PG007','Admin','Lead and coordinate corporate events and functions','Experience with social media platforms and digital marketing',3),
 ('165550010','PG0010','Media','Coordinate and oversee the recruitment and hiring process','Understanding of supply chain management principles',5),
 ('12249G003','PG003','Engineering','Develop and implement safety policies and procedures','Knowledge of human resources policies and procedures',9),
 ('19521G007','PG007','Admin','Conduct research and analyze data to support decision-making','Experience with employee relations and performance management',1),
 ('18864G001','PG001','Management','Design and develop creative assets for marketing campaigns','Familiarity with legal and regulatory requirements',4),
 ('14586G004','PG004','Executive','Develop and maintain company websites and digital platforms','Ability to develop and deliver effective training programs',6),
 ('16686G005','PG005','Survey','Manage inventory levels and optimize supply chain processes','Experience with web development languages and frameworks (e.g., HTML, CSS, JavaScript)',6),
 ('19159G004','PG004','Executive','Provide legal advice and support on corporate matters','Knowledge of networking and IT infrastructure',9),
 ('169730010','PG0010','Media','Develop and execute employee engagement initiatives','Experience with customer relationship management (CRM) software',3),
 ('17916G008','PG008','Analyst','Coordinate travel arrangements and accommodations for employees','Ability to conduct market research and analysis',6),
 ('17398G009','PG009','Media','Manage and oversee facilities and office operations','Proficiency in foreign languages (e.g., Spanish, Mandarin)',8),
 ('15288G001','PG001','Management','Develop and maintain relationships with media outlets and journalists','Experience with event planning and coordination',8),
 ('18775G008','PG008','Analyst','Develop and implement quality control processes and procedures','Understanding of environmental sustainability principles',5),
 ('16246G001','PG001','Management','Conduct market research and analyze competitor activities','Knowledge of risk management and mitigation strategies',6),
 ('12152G001','PG001','Management','Develop and execute social media marketing strategies','Ability to develop and maintain strategic partnerships',2),
 ('19931G009','PG009','Media','Conduct financial analysis and forecasting to support decision-making','Experience with public speaking and presentations',1),
 ('17099G004','PG004','Executive','Develop and maintain relationships with government agencies and regulators','Understanding of corporate finance and accounting principles',9),
 ('15045G002','PG002','Analyst','Develop and implement environmental sustainability initiatives','Proficiency in statistical analysis software (e.g., SPSS, SAS)',5),
 ('14597G004','PG004','Executive','Manage and oversee corporate training and development programs','Experience with quality assurance and control processes',7),
 ('12736G006','PG006','Analyst','Develop and implement corporate branding and identity strategies','Knowledge of organizational development principles',6),
 ('14733G002','PG002','Analyst','Coordinate and oversee corporate sponsorship and partnership activities','Understanding of change management methodologies',3),
 ('13656G001','PG001','Management','Develop and implement corporate social responsibility programs','Experience with agile and lean principles',6),
 ('15325G008','PG008','Analyst','Manage and oversee corporate communications and public relations activities','Ability to develop and execute marketing campaigns',5),
 ('11169G004','PG004','Executive','Develop and implement employee wellness programs','Knowledge of digital advertising platforms and metrics',9),
 ('18139G008','PG008','Analyst','Manage and oversee corporate philanthropy and charitable giving initiatives','Experience with content management systems (CMS)',9),
 ('14649G002','PG002','Analyst','Develop and maintain relationships with industry associations and organizations','Familiarity with customer experience (CX) principles',9),
 ('17639G005','PG005','Survey','Coordinate and oversee corporate volunteering and community outreach programs','Understanding of business process reengineering (BPR)',9),
 ('13034G001','PG001','Management','Develop and maintain relationships with investors and financial institutions','Experience with mergers and acquisitions (M&A) processes',4);
 
 
 -- (13) Table to track Leave Requests of Employees
 
 CREATE TABLE Leaves_Request (
LeaveRequestID VARCHAR(100) PRIMARY KEY NOT NULL,
EmployeeID BIGINT,
LeaveType VARCHAR(100), 
StartDate DATE, 
Number_Of_Leaves_Requested INT,
ApprovalStatus VARCHAR(20),
FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

INSERT INTO Leaves_Request (LeaveRequestID,EmployeeID,LeaveType,StartDate,Number_Of_Leaves_Requested,ApprovalStatus) VALUES
 (1520785,6320001520,'Maternity','2021-11-12',8,'Approved'),
 (1558715,6320001558,'PTO','2021-04-21',14,'Denied'),
 (1585646,6320001585,'Sick Day','2021-12-17',13,'Approved'),
 (1511561,6320001511,'Vacation / Annual Leave','2021-03-16',7,'Approved'),
 (1580109,6320001580,'Jury Duty Leave','2020-11-18',7,'Approved'),
 (1555696,6320001555,'Sick Day','2021-07-09',2,'Pending'),
 (1540547,6320001540,'Maternity','2020-10-19',7,'Pending'),
 (1568866,6320001568,'Maternity','2020-06-06',12,'Pending'),
 (1520291,6320001520,'Jury Duty Leave','2021-01-08',11,'Approved'),
 (1583909,6320001583,'PTO','2021-06-07',4,'Approved'),
 (1538233,6320001538,'Jury Duty Leave','2021-04-11',9,'Pending'),
 (1594922,6320001594,'Vacation / Annual Leave','2020-08-06',5,'Denied'),
 (1513827,6320001513,'Jury Duty Leave','2021-10-02',3,'Approved'),
 (1540388,6320001540,'Sick Day','2020-03-10',5,'Approved'),
 (1554885,6320001554,'Sick Day','2020-11-04',2,'Approved'),
 (1536764,6320001536,'PTO','2021-07-02',7,'Denied'),
 (1592424,6320001592,'Maternity','2021-07-08',1,'Denied'),
 (1556626,6320001556,'Vacation / Annual Leave','2020-06-17',3,'Approved'),
 (1573533,6320001573,'Vacation / Annual Leave','2020-04-07',6,'Approved'),
 (1518811,6320001518,'Vacation / Annual Leave','2021-07-02',1,'Denied'),
 (1536726,6320001536,'Jury Duty Leave','2021-08-09',5,'Pending'),
 (1500964,6320001500,'Maternity','2021-08-26',4,'Pending'),
 (1554872,6320001554,'Jury Duty Leave','2020-01-27',12,'Approved'),
 (1578155,6320001578,'Vacation / Annual Leave','2020-10-21',10,'Approved'),
 (1563286,6320001563,'Sick Day','2020-11-15',1,'Approved'),
 (1500499,6320001500,'Maternity','2020-02-08',8,'Approved'),
 (1589217,6320001589,'PTO','2020-09-24',3,'Approved'),
 (1554732,6320001554,'PTO','2020-08-22',15,'Approved'),
 (1577574,6320001577,'Vacation / Annual Leave','2021-07-08',15,'Approved'),
 (1546703,6320001546,'Jury Duty Leave','2020-06-11',4,'Approved'),
 (1577726,6320001577,'Jury Duty Leave','2020-12-13',10,'Approved'),
 (1538437,6320001538,'Vacation / Annual Leave','2021-04-08',15,'Denied'),
 (1594577,6320001594,'Jury Duty Leave','2020-05-03',11,'Approved'),
 (1506989,6320001506,'Sick Day','2020-01-04',8,'Approved'),
 (1556497,6320001556,'Sick Day','2021-07-22',11,'Pending'),
 (1510730,6320001510,'Jury Duty Leave','2021-12-02',9,'Pending'),
 (1521204,6320001521,'PTO','2020-05-01',3,'Pending'),
 (1508686,6320001508,'Maternity','2021-06-25',4,'Pending'),
 (1572610,6320001572,'Jury Duty Leave','2021-04-16',6,'Approved'),
 (1520205,6320001520,'PTO','2020-08-20',9,'Approved'),
 (1544797,6320001544,'Vacation / Annual Leave','2020-11-26',4,'Approved'),
 (1580826,6320001580,'Maternity','2021-04-22',4,'Approved'),
 (1518830,6320001518,'Vacation / Annual Leave','2021-01-17',5,'Approved'),
 (1517853,6320001517,'Sick Day','2021-01-23',5,'Pending'),
 (1528993,6320001528,'Jury Duty Leave','2020-06-10',3,'Approved'),
 (1590678,6320001590,'Sick Day','2020-08-17',9,'Pending'),
 (1526420,6320001526,'Jury Duty Leave','2020-09-10',4,'Approved');

select * from Leaves_Request;

-- (14) Table to track Leave Transactions of Employees in the company

CREATE TABLE IF NOT EXISTS Employee_Leaves_Log (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    LeaveRequestID VARCHAR(100),
    EmployeeID BIGINT,
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (LeaveRequestID) REFERENCES Leaves_Request(LeaveRequestID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

-- (15) Table to track Employee Payroll in the company

CREATE TABLE Payroll (
PayrollId BIGINT,
EmployeeID BIGINT,
PayPeriodStartDate DATE, 
PayPeriodEndDate DATE,
FOREIGN KEY (EmployeeID) REFERENCES Employee_Information(EmployeeID)
);

INSERT INTO Payroll (PayrollId,EmployeeID,PayPeriodStartDate,PayPeriodEndDate) VALUES
(15003722,6320001500,'2020-01-01','2020-12-31'),
(15011724,6320001501,'2020-01-01','2020-12-31'),
(15023492,6320001502,'2020-01-01','2020-12-31'),
(15034152,6320001503,'2020-01-01','2020-12-31'),
(15042228,6320001504,'2020-01-01','2020-12-31'),
(15057618,6320001505,'2020-01-01','2020-12-31'),
(15062013,6320001506,'2020-01-01','2020-12-31'),
(15073362,6320001507,'2020-01-01','2020-12-31'),
(15081399,6320001508,'2020-01-01','2020-12-31'),
(15095752,6320001509,'2020-01-01','2020-12-31'),
(15102717,6320001510,'2020-01-01','2020-12-31'),
(15115498,6320001511,'2020-01-01','2020-12-31'),
(15121724,6320001512,'2020-01-01','2020-12-31'),
(15137968,6320001513,'2020-01-01','2020-12-31'),
(15144633,6320001514,'2020-01-01','2020-12-31'),
(15153634,6320001515,'2020-01-01','2020-12-31'),
(15163126,6320001516,'2020-01-01','2020-12-31'),
(15177239,6320001517,'2020-01-01','2020-12-31'),
(15185072,6320001518,'2020-01-01','2020-12-31'),
(15196273,6320001519,'2020-01-01','2020-12-31'),
(15201733,6320001520,'2020-01-01','2020-12-31'),
(15213588,6320001521,'2020-01-01','2020-12-31'),
(15227059,6320001522,'2020-01-01','2020-12-31'),
(15234003,6320001523,'2020-01-01','2020-12-31'),
(15247943,6320001524,'2020-01-01','2020-12-31'),
(15255924,6320001525,'2020-01-01','2020-12-31'),
(15262032,6320001526,'2020-01-01','2020-12-31'),
(15274122,6320001527,'2020-01-01','2020-12-31'),
(15285391,6320001528,'2020-01-01','2020-12-31'),
(15296003,6320001529,'2020-01-01','2020-12-31'),
(15304139,6320001530,'2020-01-01','2020-12-31'),
(15313808,6320001531,'2020-01-01','2020-12-31'),
(15321943,6320001532,'2020-01-01','2020-12-31'),
(15336837,6320001533,'2020-01-01','2020-12-31'),
(15346105,6320001534,'2020-01-01','2020-12-31'),
(15355758,6320001535,'2020-01-01','2020-12-31'),
(15368983,6320001536,'2020-01-01','2020-12-31'),
(15376595,6320001537,'2020-01-01','2020-12-31'),
(15386265,6320001538,'2020-01-01','2020-12-31'),
(15392431,6320001539,'2020-01-01','2020-12-31'),
(15408090,6320001540,'2020-01-01','2020-12-31'),
(15417887,6320001541,'2020-01-01','2020-12-31'),
(15423081,6320001542,'2020-01-01','2020-12-31'),
(15431580,6320001543,'2020-01-01','2020-12-31'),
(15447332,6320001544,'2020-01-01','2020-12-31'),
(15454990,6320001545,'2020-01-01','2020-12-31'),
(15468960,6320001546,'2020-01-01','2020-12-31'),
(15471281,6320001547,'2020-01-01','2020-12-31'),
(15483316,6320001548,'2020-01-01','2020-12-31'),
(15492939,6320001549,'2020-01-01','2020-12-31'),
(15503816,6320001550,'2020-01-01','2020-12-31'),
(15517271,6320001551,'2020-01-01','2020-12-31'),
(15521423,6320001552,'2020-01-01','2020-12-31'),
(15538174,6320001553,'2020-01-01','2020-12-31'),
(15543266,6320001554,'2020-01-01','2020-12-31'),
(15557724,6320001555,'2020-01-01','2020-12-31'),
(15562701,6320001556,'2020-01-01','2020-12-31'),
(15577343,6320001557,'2020-01-01','2020-12-31'),
(15584402,6320001558,'2020-01-01','2020-12-31'),
(15598876,6320001559,'2020-01-01','2020-12-31'),
(15602443,6320001560,'2020-01-01','2020-12-31'),
(15614055,6320001561,'2020-01-01','2020-12-31'),
(15625601,6320001562,'2020-01-01','2020-12-31'),
(15638508,6320001563,'2020-01-01','2020-12-31'),
(15646672,6320001564,'2020-01-01','2020-12-31'),
(15655664,6320001565,'2020-01-01','2020-12-31'),
(15669671,6320001566,'2020-01-01','2020-12-31'),
(15671656,6320001567,'2020-01-01','2020-12-31'),
(15689321,6320001568,'2020-01-01','2020-12-31'),
(15694499,6320001569,'2020-01-01','2020-12-31'),
(15707881,6320001570,'2020-01-01','2020-12-31'),
(15713132,6320001571,'2020-01-01','2020-12-31'),
(15726611,6320001572,'2020-01-01','2020-12-31'),
(15737505,6320001573,'2020-01-01','2020-12-31'),
(15746215,6320001574,'2020-01-01','2020-12-31'),
(15757155,6320001575,'2020-01-01','2020-12-31'),
(15769755,6320001576,'2020-01-01','2020-12-31'),
(15776656,6320001577,'2020-01-01','2020-12-31'),
(15785209,6320001578,'2020-01-01','2020-12-31'),
(15792664,6320001579,'2020-01-01','2020-12-31'),
(15802393,6320001580,'2020-01-01','2020-12-31'),
(15812371,6320001581,'2020-01-01','2020-12-31'),
(15824162,6320001582,'2020-01-01','2020-12-31'),
(15835685,6320001583,'2020-01-01','2020-12-31'),
(15846270,6320001584,'2020-01-01','2020-12-31'),
(15857303,6320001585,'2020-01-01','2020-12-31'),
(15867430,6320001586,'2020-01-01','2020-12-31'),
(15871565,6320001587,'2020-01-01','2020-12-31'),
(15883385,6320001588,'2020-01-01','2020-12-31'),
(15895696,6320001589,'2020-01-01','2020-12-31'),
(15902946,6320001590,'2020-01-01','2020-12-31'),
(15913049,6320001591,'2020-01-01','2020-12-31'),
(15922469,6320001592,'2020-01-01','2020-12-31'),
(15939347,6320001593,'2020-01-01','2020-12-31'),
(15948818,6320001594,'2020-01-01','2020-12-31'),
(15955638,6320001595,'2020-01-01','2020-12-31'),
(15961704,6320001596,'2020-01-01','2020-12-31'),
(15976599,6320001597,'2020-01-01','2020-12-31'),
(15989411,6320001598,'2020-01-01','2020-12-31'),
(15997327,6320001599,'2020-01-01','2020-12-31'),
(15005958,6320001500,'2021-01-01','2021-12-31'),
(15014654,6320001501,'2021-01-01','2021-12-31'),
(15027376,6320001502,'2021-01-01','2021-12-31'),
(15038209,6320001503,'2021-01-01','2021-12-31'),
(15043561,6320001504,'2021-01-01','2021-12-31'),
(15054020,6320001505,'2021-01-01','2021-12-31'),
(15066292,6320001506,'2021-01-01','2021-12-31'),
(15078136,6320001507,'2021-01-01','2021-12-31'),
(15083620,6320001508,'2021-01-01','2021-12-31'),
(15092313,6320001509,'2021-01-01','2021-12-31'),
(15105764,6320001510,'2021-01-01','2021-12-31'),
(15113221,6320001511,'2021-01-01','2021-12-31'),
(15122885,6320001512,'2021-01-01','2021-12-31'),
(15139397,6320001513,'2021-01-01','2021-12-31'),
(15145584,6320001514,'2021-01-01','2021-12-31'),
(15155176,6320001515,'2021-01-01','2021-12-31'),
(15167485,6320001516,'2021-01-01','2021-12-31'),
(15171828,6320001517,'2021-01-01','2021-12-31'),
(15183098,6320001518,'2021-01-01','2021-12-31'),
(15192931,6320001519,'2021-01-01','2021-12-31'),
(15207940,6320001520,'2021-01-01','2021-12-31'),
(15219650,6320001521,'2021-01-01','2021-12-31'),
(15225389,6320001522,'2021-01-01','2021-12-31'),
(15236387,6320001523,'2021-01-01','2021-12-31'),
(15247288,6320001524,'2021-01-01','2021-12-31'),
(15254372,6320001525,'2021-01-01','2021-12-31'),
(15266336,6320001526,'2021-01-01','2021-12-31'),
(15278573,6320001527,'2021-01-01','2021-12-31'),
(15289835,6320001528,'2021-01-01','2021-12-31'),
(15297751,6320001529,'2021-01-01','2021-12-31'),
(15308680,6320001530,'2021-01-01','2021-12-31'),
(15318198,6320001531,'2021-01-01','2021-12-31'),
(15322302,6320001532,'2021-01-01','2021-12-31'),
(15333940,6320001533,'2021-01-01','2021-12-31'),
(15346245,6320001534,'2021-01-01','2021-12-31'),
(15357169,6320001535,'2021-01-01','2021-12-31'),
(15368999,6320001536,'2021-01-01','2021-12-31'),
(15371011,6320001537,'2021-01-01','2021-12-31'),
(15383297,6320001538,'2021-01-01','2021-12-31'),
(15397038,6320001539,'2021-01-01','2021-12-31'),
(15408204,6320001540,'2021-01-01','2021-12-31'),
(15419638,6320001541,'2021-01-01','2021-12-31'),
(15421068,6320001542,'2021-01-01','2021-12-31'),
(15436289,6320001543,'2021-01-01','2021-12-31'),
(15447357,6320001544,'2021-01-01','2021-12-31'),
(15455235,6320001545,'2021-01-01','2021-12-31'),
(15464699,6320001546,'2021-01-01','2021-12-31'),
(15471691,6320001547,'2021-01-01','2021-12-31'),
(15487884,6320001548,'2021-01-01','2021-12-31'),
(15494862,6320001549,'2021-01-01','2021-12-31'),
(15505643,6320001550,'2021-01-01','2021-12-31'),
(15516943,6320001551,'2021-01-01','2021-12-31'),
(15522813,6320001552,'2021-01-01','2021-12-31'),
(15531763,6320001553,'2021-01-01','2021-12-31'),
(15544521,6320001554,'2021-01-01','2021-12-31'),
(15552340,6320001555,'2021-01-01','2021-12-31'),
(15564801,6320001556,'2021-01-01','2021-12-31'),
(15578898,6320001557,'2021-01-01','2021-12-31'),
(15582748,6320001558,'2021-01-01','2021-12-31'),
(15591946,6320001559,'2021-01-01','2021-12-31'),
(15607880,6320001560,'2021-01-01','2021-12-31'),
(15611444,6320001561,'2021-01-01','2021-12-31'),
(15627130,6320001562,'2021-01-01','2021-12-31'),
(15634681,6320001563,'2021-01-01','2021-12-31'),
(15648348,6320001564,'2021-01-01','2021-12-31'),
(15658459,6320001565,'2021-01-01','2021-12-31'),
(15661487,6320001566,'2021-01-01','2021-12-31'),
(15671393,6320001567,'2021-01-01','2021-12-31'),
(15689442,6320001568,'2021-01-01','2021-12-31'),
(15695445,6320001569,'2021-01-01','2021-12-31'),
(15705589,6320001570,'2021-01-01','2021-12-31'),
(15715217,6320001571,'2021-01-01','2021-12-31'),
(15726646,6320001572,'2021-01-01','2021-12-31'),
(15735797,6320001573,'2021-01-01','2021-12-31'),
(15741122,6320001574,'2021-01-01','2021-12-31'),
(15754821,6320001575,'2021-01-01','2021-12-31'),
(15769101,6320001576,'2021-01-01','2021-12-31'),
(15777778,6320001577,'2021-01-01','2021-12-31'),
(15782677,6320001578,'2021-01-01','2021-12-31'),
(15794063,6320001579,'2021-01-01','2021-12-31'),
(15805860,6320001580,'2021-01-01','2021-12-31'),
(15818158,6320001581,'2021-01-01','2021-12-31'),
(15821311,6320001582,'2021-01-01','2021-12-31'),
(15835195,6320001583,'2021-01-01','2021-12-31'),
(15848584,6320001584,'2021-01-01','2021-12-31'),
(15852411,6320001585,'2021-01-01','2021-12-31'),
(15862332,6320001586,'2021-01-01','2021-12-31'),
(15873154,6320001587,'2021-01-01','2021-12-31'),
(15883893,6320001588,'2021-01-01','2021-12-31'),
(15892323,6320001589,'2021-01-01','2021-12-31'),
(15903642,6320001590,'2021-01-01','2021-12-31'),
(15914192,6320001591,'2021-01-01','2021-12-31'),
(15922087,6320001592,'2021-01-01','2021-12-31'),
(15938193,6320001593,'2021-01-01','2021-12-31'),
(15948470,6320001594,'2021-01-01','2021-12-31'),
(15956618,6320001595,'2021-01-01','2021-12-31'),
(15969484,6320001596,'2021-01-01','2021-12-31'),
(15971523,6320001597,'2021-01-01','2021-12-31'),
(15983722,6320001598,'2021-01-01','2021-12-31'),
(15997853,6320001599,'2021-01-01','2021-12-31');


-- Calculations for payroll 

alter table payroll
add Base_Salary Decimal(10,2),
add Deductions Decimal(10,2),
add Benefits Decimal(10,2),
add Total_Salary Decimal(10,2);

-- Complex Query #3
update payroll
left join salaries on payroll.EmployeeID=salaries.EmployeeID
Set payroll.Base_Salary=salaries.BaseSalary,
	payroll.Benefits=(salaries.BenefitAmount+salaries.Bonus);

-- Complex Query #4
update payroll
left join (select salaries.EmployeeID, deductions.DeductionRate 
			from salaries 
            left join deductions 
            on salaries.DeductionID=deductions.DeductionID) as Employee_Rates
on payroll.EmployeeID=Employee_Rates.EmployeeID
set payroll.deductions=(Employee_Rates.DeductionRate*payroll.Base_Salary/100);

update payroll
set Total_Salary=Base_Salary+Benefits-Deductions;



-- Calculations for Salary Table

alter table salaries
add TotalSalary Decimal(10,2);

-- Complex Query #5
update salaries
left join (select salaries.EmployeeID, deductions.DeductionRate 
			from salaries 
            left join deductions 
            on salaries.DeductionID=deductions.DeductionID) as Employee_Rates
on salaries.EmployeeID=Employee_Rates.EmployeeID
set salaries.TotalSalary=salaries.BaseSalary+salaries.Bonus+salaries.BenefitAmount-(Employee_Rates.DeductionRate*salaries.BaseSalary/100);

-- Complex Query #6
-- Check how much an employee worked on a certain date
SELECT attendance.EmployeeID,Employee_information.First_Name,Employee_information.Last_Name,attendance.AttendanceDate,TIMEDIFF(EndTime, StartTime) AS Time_Worked 
	from attendance
	left join Employee_information
	on attendance.EmployeeID=Employee_information.EmployeeID;


-- Function #1 (CheckTimeGreaterThan8Hours)

Delimiter //
CREATE FUNCTION CheckTimeGreaterThan8Hours(time_column TIME) RETURNS BOOLEAN DETERMINISTIC
BEGIN
    DECLARE hour_diff INT;
    SET hour_diff = HOUR(time_column);
    RETURN hour_diff > 8;
END;
//
Delimiter ;


SELECT EmployeeID,First_Name,Last_Name,AttendanceDate,Time_Worked,CheckTimeGreaterThan8Hours(Time_Worked) as Overtime
FROM (SELECT attendance.EmployeeID,Employee_information.First_Name,Employee_information.Last_Name,attendance.AttendanceDate,TIMEDIFF(EndTime, StartTime) AS Time_Worked 
	from attendance
	left join Employee_information
	on attendance.EmployeeID=Employee_information.EmployeeID) as Employee_Work;
    
-- Complex Query #7 (Check the Average Performance Metrics of Employees on a YOY Basis
-- select * from performancemetrics;

select Employee_information.EmployeeID,Employee_information.First_Name,Employee_information.Last_Name,
Project_Completion_Rate,Sales_Revenue, Hours_Worked, Punctuality,Performance,  Year 
from Employee_information
left join (SELECT EmployeeID, 
			AVG(Project_Completion_Rate) as Project_Completion_Rate,
			AVG(Sales_Revenue) as Sales_Revenue, 
			AVG(Hours_Worked) as Hours_Worked, 
			AVG(Punctuality) as Punctuality,
			AVG(Performance) as Performance,  
			YEAR(Cycle_Start_Date) as Year
			FROM performancemetrics
			group by EmployeeID, Year) as YOY_Rollup
on Employee_Information.EmployeeID=YOY_Rollup.EmployeeID;

-- Function #2
-- drop function OvertimeHours; 

Delimiter //
CREATE FUNCTION OvertimeHours(time_column TIME) RETURNS DECIMAL(10,2) DETERMINISTIC
BEGIN
    DECLARE hour_diff INT;
    Declare min_diff DECIMAL(10,2);
    SET min_diff= minute(time_column)/100;
    SET hour_diff = HOUR(time_column);
    IF (hour_diff+min_diff) > 8 THEN
        RETURN hour_diff+min_diff - 8;
    ELSE
        RETURN 0;
    END IF;
END;
//
Delimiter ;

SELECT EmployeeID,First_Name,Last_Name,AttendanceDate,Time_Worked,CheckTimeGreaterThan8Hours(Time_Worked) as Overtime, OvertimeHours(Time_Worked) as OvertimeHours
FROM (SELECT attendance.EmployeeID,Employee_information.First_Name,Employee_information.Last_Name,attendance.AttendanceDate,TIMEDIFF(EndTime, StartTime) AS Time_Worked 
	from attendance
	left join Employee_information
	on attendance.EmployeeID=Employee_information.EmployeeID) as Employee_Work;


-- overtime pay=(Amount worked overtime)/8 * base_Salary
-- Function #3

select * from salaries;
-- drop function CalculateOvertimePay;
DELIMITER //
CREATE FUNCTION CalculateOvertimePay(base_salary DECIMAL(10, 2), overtime_hours DECIMAL(10, 2)) RETURNS DECIMAL(10, 2) deterministic
BEGIN
    DECLARE overtime_pay DECIMAL(10, 2);
    -- Calculate overtime pay
    SET overtime_pay = (overtime_hours / (8*30)) * base_salary;
    RETURN overtime_pay;
END //
DELIMITER ;

-- Complex Query #8
Select Salaries.EmployeeID,AttendanceDate,OvertimeHours, 
CalculateOvertimePay(basesalary , overtimehours ) as OvertimePay
from Salaries
left join (SELECT EmployeeID,First_Name,Last_Name,AttendanceDate,Time_Worked,CheckTimeGreaterThan8Hours(Time_Worked) as Overtime, OvertimeHours(Time_Worked) as OvertimeHours
			FROM (SELECT attendance.EmployeeID,Employee_information.First_Name,Employee_information.Last_Name,attendance.AttendanceDate,TIMEDIFF(EndTime, StartTime) AS Time_Worked 
			from attendance
			left join Employee_information
			on attendance.EmployeeID=Employee_information.EmployeeID) as Employee_Work) as OvertimeTable
on Salaries.EmployeeID=OvertimeTable.EmployeeID;


-- Function #4
-- Calculate hourly Base pay (Base Salary/(Workdays *8))
DELIMITER //
CREATE FUNCTION CalculateHourlyBasePay(BaseSalary DECIMAL(10, 2), Workdays INT) 
RETURNS DECIMAL(10, 2)
deterministic
BEGIN
    DECLARE HourlyBasePay DECIMAL(10, 2);
    
    SET HourlyBasePay = BaseSalary / (Workdays * 8);
    
    RETURN HourlyBasePay;
END;
//
DELIMITER ;

-- Complex Query #9
-- Assumption made here that the total workdays in a year is 241
select salaries.EmployeeID,
CalculateHourlyBasePay(salaries.BaseSalary, 241) as Hourly_Pay,
Number_Of_Leaves_Requested as Leaves_ ,
(CalculateHourlyBasePay(salaries.BaseSalary, 241)*Number_Of_Leaves_Requested*8) as Revenue_Loss_From_Leaves
from (select * from leaves_request where ApprovalStatus in ('Approved')) as approved_leaves
left join salaries
on salaries.EmployeeID=approved_leaves.EmployeeID;

-- Function #5
-- Function to Calculate Age
DELIMITER //

CREATE FUNCTION CalculateAge(dob DATE, DB_DATE DATE) RETURNS INT DETERMINISTIC
BEGIN
    DECLARE age INT;

    SET age = YEAR(DB_DATE) - YEAR(dob);
    IF MONTH(DB_DATE) < MONTH(dob) OR (MONTH(DB_DATE) = MONTH(dob) AND DAY(DB_DATE) < DAY(dob)) THEN
        SET age = age - 1;
    END IF;

    RETURN age;
END;
//
DELIMITER ;

-- Complex Query #11
-- Calculate Age of Employee
SELECT EmployeeID,First_Name,Last_Name,DOB,
    CalculateAge(DOB,'2022-01-01') AS Age,
    CASE
        WHEN (-CalculateAge(DOB,'2022-01-01') + 62) < 0 THEN 0
        ELSE (-CalculateAge(DOB,'2022-01-01') + 62)
    END AS YearsToRetire
FROM employee_information;

-- Complex Query #10
-- To Calculate Retirement Funds

select Retirement.EmployeeID, RetirementFundsPerYear, Age, (YearsToRetire*RetirementFundsPerYear) as PendingRetirementFunds
from (select EmployeeID,(TotalSalary*0.10) as RetirementFundsperYear from salaries) as Retirement
left join (SELECT EmployeeID,First_Name,Last_Name,DOB,
    CalculateAge(DOB,'2022-01-01') AS Age,
    CASE
        WHEN (-CalculateAge(DOB,'2022-01-01') + 62) < 0 THEN 0
        ELSE (-CalculateAge(DOB,'2022-01-01') + 62)
    END AS YearsToRetire
FROM employee_information) as AgeTable
on Retirement.EmployeeID=AgeTable.EmployeeID;



-- Stored Procedure #1 - Add a new employee
DELIMITER //

CREATE PROCEDURE Add_New_Employee (
  IN p_Employee_ID BIGINT,	
  IN p_FirstName VARCHAR(255),
  IN p_LastName VARCHAR(255),
  IN p_DOB DATE,
  IN p_Address VARCHAR(255),
  IN p_City VARCHAR(255),
  IN p_Zipcode INT,
  IN p_Gender VARCHAR(255),
  IN p_Mobile VARCHAR(255),
  IN p_SSN BIGINT
)
BEGIN
  DECLARE v_Company_Email VARCHAR(255);
  DECLARE v_Personal_Email VARCHAR(255);
  
  SET v_Company_Email = CONCAT(LOWER(LEFT(p_FirstName, 1)), 'x', LOWER(LEFT(p_LastName, 1)), RIGHT(p_Employee_ID, 3), '@dbmscorp.com');
  SET v_Personal_Email = CONCAT(LOWER(p_FirstName), '.', LOWER(p_LastName), '@gmail.com');
  
  INSERT INTO Employee_Information (
    EmployeeID,
    First_Name,
    Last_Name,
    DOB,
    Address,
    City,
    Zipcode,
    Gender,
    Mobile,
    SSN,
    Company_Email,
    Personal_Email
  )
  VALUES (
    p_Employee_ID,
    p_FirstName,
    p_LastName,
    p_DOB,
    p_Address,
    p_City,
    p_Zipcode,
    p_Gender,
    p_Mobile,
    p_SSN,
    v_Company_Email,
    v_Personal_Email
  );

END //
DELIMITER ;



-- Stored Procedure #2 - Update Employee Information
DELIMITER //

CREATE PROCEDURE Update_Employee_Parameter (
  IN p_Employee_ID BIGINT,
  IN p_Parameter VARCHAR(255),
  IN p_Value VARCHAR(255)
)
BEGIN
  DECLARE v_ColumnName VARCHAR(255);
  
  CASE p_Parameter
    WHEN 'First_Name' THEN SET v_ColumnName = 'First_Name';
    WHEN 'Last_Name' THEN SET v_ColumnName = 'Last_Name';
    WHEN 'DOB' THEN SET v_ColumnName = 'DOB';
    WHEN 'Address' THEN SET v_ColumnName = 'Address';
    WHEN 'City' THEN SET v_ColumnName = 'City';
    WHEN 'Zipcode' THEN SET v_ColumnName = 'Zipcode';
    WHEN 'Gender' THEN SET v_ColumnName = 'Gender';
    WHEN 'Mobile' THEN SET v_ColumnName = 'Mobile';
    WHEN 'SSN' THEN SET v_ColumnName = 'SSN';
    WHEN 'Company_Email' THEN SET v_ColumnName = 'Company_Email';
    WHEN 'Personal_Email' THEN SET v_ColumnName = 'Personal_Email';
    ELSE SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid parameter provided';
  END CASE;

  SET @sql = CONCAT('UPDATE Employee_Information SET ', v_ColumnName, ' = ? WHERE EmployeeID = ?');
  PREPARE stmt FROM @sql;
  SET @p_Value = p_Value;
  SET @p_Employee_ID = p_Employee_ID;
  EXECUTE stmt USING @p_Value, @p_Employee_ID;
  DEALLOCATE PREPARE stmt;
  
END //

DELIMITER ;



-- Stored Procedure #3 - Adding Records to Performance Metrics
DELIMITER //

CREATE PROCEDURE Add_Performance_Metrics (
  IN p_EmployeeID BIGINT, 
  IN p_PerformanceID BIGINT,
  IN p_Cycle_Start_Date DATE,
  IN p_Cycle_End_Date DATE,
  IN p_Days_in_cycle INT,
  IN p_Sales_Revenue INT,
  IN p_Hours_Worked INT,
  IN p_Project_Completion_Rate DECIMAL(3, 1),
  IN p_Milestones VARCHAR(255)
)
BEGIN
  -- Declare variables
  DECLARE v_Punctuality DECIMAL(5, 2);
  DECLARE v_Efficiency DECIMAL(5, 2);

  SET v_Punctuality = p_Hours_Worked / (p_Days_in_cycle * 8);
  SET v_Efficiency = p_Sales_Revenue / p_Hours_Worked;
  
  INSERT INTO PerformanceMetrics (
    EmployeeID,
    PerformanceID,
    Cycle_Start_Date,
    Cycle_End_Date,
    Days_in_cycle,
    Sales_Revenue,
    Hours_Worked,
    Project_Completion_Rate,
    Milestones,
    Punctuality,
    Efficiency
  )
  VALUES (
    p_EmployeeID,
    p_PerformanceID,
    p_Cycle_Start_Date,
    p_Cycle_End_Date,
    p_Days_in_cycle,
    p_Sales_Revenue,
    p_Hours_Worked,
    p_Project_Completion_Rate,
    p_Milestones,
    v_Punctuality,
    v_Efficiency
  );

  UPDATE PerformanceMetrics AS pm
  JOIN (SELECT MAX(efficiency) AS max_efficiency FROM PerformanceMetrics) AS max_eff
  SET pm.norm_efficiency = pm.efficiency / max_eff.max_efficiency;
  
END //

DELIMITER ;



-- Stored Procedure #4 - Calculate Employee Salary
DELIMITER //

CREATE PROCEDURE Calculate_Employee_Salary (
  IN p_Employee_ID BIGINT
)
BEGIN
  DECLARE v_BaseSalary DECIMAL(10,2);
  DECLARE v_Bonus DECIMAL(10,2);
  DECLARE v_BenefitAmount DECIMAL(10,2);
  DECLARE v_DeductionRate DECIMAL(15,2);
  DECLARE v_Deduction_Amount DECIMAL(10,2);
  DECLARE v_Total_Salary DECIMAL(10,2);
  
  -- Retrieve BaseSalary, Bonus, and BenefitAmount from Salaries table
  SELECT BaseSalary, Bonus, BenefitAmount INTO v_BaseSalary, v_Bonus, v_BenefitAmount
  FROM Salaries
  WHERE EmployeeID = p_Employee_ID;
  
  -- Retrieve DeductionRate from Deductions table
  SELECT DeductionRate INTO v_DeductionRate
  FROM Deductions
  WHERE DeductionID = (SELECT DeductionID FROM Salaries WHERE EmployeeID = p_Employee_ID);
  
  -- Calculate Deduction_Amount
  SET v_Deduction_Amount = (v_DeductionRate/100) * v_BaseSalary;
  
  -- Calculate Total_Salary
  SET v_Total_Salary = v_BaseSalary - v_Deduction_Amount + v_Bonus + v_BenefitAmount;
  
  -- Display the calculated salary
  SELECT 
    v_BaseSalary AS Base_Salary,
    v_Bonus AS Bonus,
    v_BenefitAmount AS Benefit_Amount,
    v_DeductionRate AS Deduction_Rate,
    v_Deduction_Amount AS Deduction_Amount,
    v_Total_Salary AS Total_Salary;
    
END //

DELIMITER ;


-- Stored Procedure #5 - Adding Records to Review
DELIMITER //

CREATE PROCEDURE Add_Review (
  IN p_ReviewID BIGINT,
  IN p_EmployeeID BIGINT,
  IN p_ReviewerID BIGINT,
  IN p_ReviewDate DATE,
  IN p_ReviewPeriod VARCHAR(255),
  IN p_PerformanceRatings DECIMAL(5, 2),
  IN p_GoalsTargets VARCHAR(255),
  IN p_Strengths VARCHAR(255),
  IN p_AreasForImprovement VARCHAR(255),
  IN p_ActionableSteps VARCHAR(255),
  IN p_TrainingDevelopmentNeeds VARCHAR(255),
  IN p_CareerAspirations VARCHAR(255),
  IN p_OverallAssessment VARCHAR(255)
)
BEGIN
  INSERT INTO Review (
    ReviewID,
    EmployeeID,
    ReviewerID,
    ReviewDate,
    ReviewPeriod,
    PerformanceRatings,
    GoalsTargets,
    Strengths,
    AreasForImprovement,
    ActionableSteps,
    TrainingDevelopmentNeeds,
    CareerAspirations,
    OverallAssessment
  )
  VALUES (
    p_ReviewID,
    p_EmployeeID,
    p_ReviewerID,
    p_ReviewDate,
    p_ReviewPeriod,
    p_PerformanceRatings,
    p_GoalsTargets,
    p_Strengths,
    p_AreasForImprovement,
    p_ActionableSteps,
    p_TrainingDevelopmentNeeds,
    p_CareerAspirations,
    p_OverallAssessment
  );
END //
DELIMITER ;



-- Trigger #1 - Update Log After Employee Is Added
DELIMITER //

CREATE TRIGGER trg_After_Insert_Employee
AFTER INSERT ON Employee_Information
FOR EACH ROW
BEGIN
  INSERT INTO HistoryLog_EmployeeInformation (LogType, LogDate, LogDetails, EmployeeID)
  VALUES ('Employee Added', NOW(), CONCAT('Employee ', NEW.EmployeeID, ' added to Employee_Information table'), NEW.EmployeeID);
END //
DELIMITER ;

-- Call Statements
CALL Add_New_Employee (6320001600, 'Naveen', 'Jindal', '1985-10-22', '7575, Frankford Road', 'Dallas', 75252, 'M','+19729463967', 585468123);
Select * from Employee_Information;
SELECT * FROM HistoryLog_EmployeeInformation;



-- Trigger #2 - Update Log After Update in Employee Parameter
DELIMITER //
CREATE TRIGGER trg_After_Update_Employee_Parameter
AFTER UPDATE ON Employee_Information
FOR EACH ROW
BEGIN
  -- Check if the stored procedure Update_Employee_Parameter was called
  IF OLD.First_Name != NEW.First_Name OR
     OLD.Last_Name != NEW.Last_Name OR
     OLD.DOB != NEW.DOB OR
     OLD.Address != NEW.Address OR
     OLD.City != NEW.City OR
     OLD.Zipcode != NEW.Zipcode OR
     OLD.Gender != NEW.Gender OR
     OLD.Mobile != NEW.Mobile OR
     OLD.SSN != NEW.SSN OR
     OLD.Company_Email != NEW.Company_Email OR
     OLD.Personal_Email != NEW.Personal_Email THEN
    
    -- Insert into the history log table
    INSERT INTO HistoryLog_EmployeeInformation (LogType, LogDate, LogDetails, EmployeeID)
    VALUES ('Employee Parameter Updated', NOW(), CONCAT('Employee ', NEW.EmployeeID, ' parameter updated'), NEW.EmployeeID);
  END IF;
END //
DELIMITER ;

-- Call Statements
CALL Update_Employee_Parameter(6320001599, 'City', 'Austin');
CALL Update_Employee_Parameter(6320001599, 'Zipcode', '98467');
Select * from Employee_Information;
SELECT * FROM HistoryLog_EmployeeInformation;



-- Trigger #3 - Update Log for every Performance Metric Added 
DELIMITER //

CREATE TRIGGER trg_After_Insert_PerformanceMetrics
AFTER INSERT ON PerformanceMetrics
FOR EACH ROW
BEGIN
  INSERT INTO HistoryLog_EmployeeInformation (LogType, LogDate, LogDetails, EmployeeID)
  VALUES ('Performance Metrics Added', NOW(), CONCAT('Performance metrics added for Employee ', NEW.EmployeeID), NEW.EmployeeID);
END //

DELIMITER ;

-- Call Statements
CALL Add_Performance_Metrics(6320001599,1599542120,'2020-01-01','2020-03-31',90,18826,657,0.8,'Track key performance indicators (KPIs)');
Select * from performancemetrics;
SELECT * FROM HistoryLog_EmployeeInformation;




-- Trigger #4 - Update Log everytime a leave is approved
DELIMITER //

CREATE TRIGGER trg_Log_Approved_Leaves
AFTER UPDATE ON Leaves_Request
FOR EACH ROW
BEGIN
    IF NEW.ApprovalStatus = 'Approved' THEN
        -- Insert into Employee_Leaves_Log
        INSERT INTO Employee_Leaves_Log (LeaveRequestID, EmployeeID, StartDate, EndDate)
        VALUES (NEW.LeaveRequestID, NEW.EmployeeID, NEW.StartDate, DATE_ADD(NEW.StartDate, INTERVAL NEW.Number_Of_Leaves_Requested - 1 DAY));
    END IF;
END //
DELIMITER ;

-- Call Statements
INSERT INTO Leaves_Request VALUES (1520789,6320001520,'Maternity Extended Thrice','2021-12-12',8,'Pending');
UPDATE Leaves_Request SET ApprovalStatus = 'Approved' WHERE LeaveRequestID = '1520789';
SELECT * FROM Leaves_Request;
SELECT * FROM Employee_Leaves_Log;




-- Trigger #5 - Update Log everytime Review is Added
DELIMITER //

CREATE TRIGGER trg_After_Insert_Review
AFTER INSERT ON Review
FOR EACH ROW
BEGIN
  INSERT INTO HistoryLog_EmployeeInformation (LogType, LogDate, LogDetails, EmployeeID)
  VALUES ('Review Added', NOW(), CONCAT('Review added for Employee ', NEW.EmployeeID), NEW.EmployeeID);
END //

DELIMITER ;

-- Call Statements
CALL Add_Review(638, 6320001598, 6320001867, '2022-12-31','Annual Review',4.5,'Exceeds Expectations','Leadership Skills','Time Management','Set clear and achievable performance goals with the employee.','Leadership skills development','Obtain a leadership role within the company.','Exceeds expectations in all key performance areas.');
select * from review;
SELECT * FROM HistoryLog_EmployeeInformation;
