# Challenge-Data-Scientist---Luis-Ramirez

This repository contains all the code related to the analyses of flights delays

## The structure of the repository is as follows: 


- data
  - raw
  - interim
  - processed
- reports
  - EDA_base_report.html
  - EDA_mod_report.html
- utils
  - utils.py
- README.md
- solution.ipynb

Where:

* **solution.ipynb** is the main file 
* **data/** contains the dataset at different stages of processing and the data dictionaries used to encode the categorical features  
* **reports/** contains the reports created for the EDA 



## Variables description:

* Fecha-I: Scheduled date and time of the flight. 
* Vlo-I : Scheduled flight number. 
* Ori-I : Programmed origin city code. 
* Des-I : Programmed destination city code. 
* Emp-I : Scheduled flight airline code. 
* Fecha-O : Date and time of flight operation. 
* Vlo-O : Flight operation number of the flight. 
* Ori-O : Operation origin city code 
* Des-O : Operation destination city code. 
* Emp-O : Airline code of the operated flight. 
* DIA: Day of the month of flight operation. 
* MES : Number of the month of operation of the flight. 
* AÑO : Year of flight operation. 
* DIANOM : Day of the week of flight operation. 
* TIPOVUELO : Type of flight, I =International, N =National. 
* OPERA : Name of the airline that operates. 
* SIGLAORI: Name city of origin. 
* SIGLADES: Destination city name. 


