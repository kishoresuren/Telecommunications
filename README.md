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

Tasks :
a. A plot of the PDF, computed over 10,000 samples that each represent the total two-month traffic in one geographical area.
b. Figures of the time series of network traffic during the first 2 weeks in 3 areas, namely:
(i) the area with the highest total traffic during the two-month period,
(ii) the area with Square id 4159, and
(iii) the area with Square id 4556
c. Build a LSTM based Neural network which takesi n a time series of previous traffic intensities and predicts the intensities for the week from December 16 to 22
d. Three plots reporting the time series of the original traffic and predicted traffic in the week from December 16 to 22
e. Mean Absolute Error (MAE) and the Mean Absolute Percentage Error (MAPE) computed for the time series corresponding to the above week


