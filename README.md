# Telecommunications
Applying Machine Learning techniques to extract useful insights and predict the network traffic intensities from a multi-source dataset of urban life in the city of Milan and the Province of Trentino Dataverse

The datasets are available here: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EGZHFV in the form of .txt files, each of which represents a day in the 2 month period between 01.11.2013 and 30.12.2013. There are hence overall 59 datasets.

The columns in each txt file are as follows: 

Square id: identification string of a given square of Milan/Trentino GRID;

Time Interval: start interval time expressed in milliseconds. The end interval time can be obtained by adding 600,000 milliseconds (10 min) to this value;

Country code: the phone country code of the nation.

SMS-in activity: activity proportional to the amount of received SMSs inside a given Square id and during a given Time interval. The SMSs are sent from the nation identified by the Country code;

SMS-out activity: activity proportional to the amount of sent SMSs inside a given Square id during a given Time interval. The SMSs are received in the nation identified by the Country code;

Call-in activity: activity proportional to the amount of received calls inside the Square id during a given Time interval. The calls are issued from the nation identified by the Country code;

Call-out activity: activity proportional to the amount of issued calls inside a given Square id during a given Time interval. The calls are received in the nation identified by the Country code;

Internet traffic activity: number of CDRs generated inside a given Square id during a given Time interval. The Internet traffic is initiated from the nation identified by the Country code;


