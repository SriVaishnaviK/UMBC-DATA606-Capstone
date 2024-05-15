## 1. Title and Author

- House Price Prediction
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Sri Vaishnavi Kudikala
- [Github](https://github.com/SriVaishnaviK)
- [LinkedIn](https://www.linkedin.com/in/vaishnavikudikala)
- Presentation:
- Youtube:
    
## 2. Background


This project centers on predicting house prices by leveraging diverse factors such as location, construction details, and interior features, drawing insights from them. The comprehensive dataset enables a thorough examination of trends in house pricing. The significance lies in providing a valuable tool for potential buyers and sellers to make well-informed decisions. Additionally, it aids real estate professionals in strategically setting competitive prices, fostering efficiency in the market. The project's broader impact lies in enhancing transparency within the real estate sector, where a detailed understanding of the various factors influencing housing prices contributes to a more informed and responsive market.
#### Research Questions
- What is the correlation between location (latitude, longitude, zip code) and house prices?
- What are the reasons for spatial variations in prices?
- How do the number of bedrooms, bathrooms, and square footage influence house prices, and what are the key contributors to these influences?
- How do the construction grade and property condition impact house prices, and is there an assessment of higher-grade property premiums?
- How do renovations affect house prices, and is there a correlation between recent renovations and higher property values?
## 3. Data 


- The dataset originates from the UCI Machine Learning Repository and is sourced from [Kaggle](https://www.kaggle.com/datasets/astronautelvis/kc-house-data/data).
- The size of the dataset is 2.03MB.
- Data shape: (21613, 21)
- Each row in the dataset represents information about a specific house sale.
- The period of the data ranges between 2014-2015.
- Data Dictionary:

  
| Column Name     | Definition                                                | Data Type |
|-----------------|-----------------------------------------------------------|-----------|
| id              | Unique ID for each home sold                               | `int64`   |
| date            | Date of the home sale                                      | `int64`   |
| price           | Price of each home sold                                    | `int64`   |
| bedrooms        | Number of bedrooms                                        | `int64`   |
| bathrooms       | Number of bathrooms, where .5 represents a room with a toilet but no shower | `float64` |
| sqft_living     | Square footage of the apartment interior living space     | `int64`   |
| sqft_lot        | Square footage of the land space                           | `int64`   |
| floors          | Number of floors                                          | `float64` |
| waterfront      | Dummy variable for whether the apartment overlooks the waterfront | `int64`   |
| view            | Index from 0 to 4 indicating the view of the property     | `int64`   |
| condition       | Index from 1 to 5 on the condition of the apartment       | `int64`   |
| grade           | Index from 1 to 13 indicating the quality of construction and design | `int64`   |
| sqft_above      | Square footage of the interior housing space above ground level | `int64`   |
| sqft_basement   | Square footage of the interior housing space below ground level | `int64`   |
| yr_built        | The year the house was initially built                     | `int64`   |
| yr_renovated    | The year of the house’s last renovation                    | `int64`   |
| zipcode         | What zipcode area the house is in                          | `int64`   |
| lat             | Latitude                                                  | `float64` |
| long            | Longitude                                                 | `float64` |
| sqft_living15   | Square footage of interior housing living space for the nearest 15 neighbors | `int64`   |
| sqft_lot15      | Square footage of land lots for the nearest 15 neighbors   | `int64`   |

 
  
- The column **price** is the target variable.
- Columns bedrooms, bathrooms,sqft_living,sqft_lot, condition, grade,yr_built,yr_renovated, lat, long, and zip code may be used as features for the ML model.

## 4. Exploratory Data Analysis(EDA)
- There were no missing or duplicated values in the dataset.
- To ensure data consistency and compatibility with the analysis, type conversions were performed on certain columns. Specifically, all the data were converted to integers wherever  necessary. This step was crucial for standardizing the data format and facilitating accurate analysis.
- Frequency Distribution of target Variable(Price)
  ![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/e01212f0-88a9-478c-850e-8366364a28d6)
The distribution exhibits a skewed pattern with the highest bars concentrated towards the lower end of the price range. This indicates that a large number of houses are priced at or near the lowest price point. As the prices increase along the x-axis, the bars representing the counts become progressively shorter, suggesting that fewer houses fall into the higher price ranges. The distribution has a long, gradually declining tail towards the right side, indicating that there are some houses priced at higher levels, but their frequency is much lower compared to the lower price points.
- A Base Map Indicating the locations of houses from the dataset
![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/39007266-a78a-4836-8414-d1e0db65a099)

- Average House Prices By Location
  
![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/7973e164-a684-4171-ad69-af5f265eef4e)

The graph suggests that there are significant variations in average prices across these different locations, which could be influenced by factors such as income levels, cost of living, and market dynamics in each area. The higher prices in Medina, Clyde Hill, and Yarrow Point may indicate more affluent neighborhoods or communities.

- Price VS Year Built
  
![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/357ec880-b7ba-4d8f-bce7-ccc4df16511f)

The analysis reveals distinct patterns in property prices relative to the year of construction. Properties built during specific decades, such as the early 1900s and late 1960s, tend to command higher prices, while those constructed in the late 1930s and mid-1990s typically have lower associated prices. This cyclical trend suggests the influence of various factors, including economic cycles and market conditions. However, individual property characteristics such as location, size, and condition may contribute to exceptions within this broader trend.

- Property Condition Vs Price
 
![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/3304cbe0-2dbe-4729-b789-fca0c52c8144)

The graph depicts a positive correlation between property condition and house prices, showing that as the condition rating improves, prices tend to rise consistently. Specifically, there's a noticeable increase in prices from the lowest (rating 1) to the highest (rating 5) condition. This underscores the market's preference for well-maintained properties, with buyers willing to pay premium prices for higher-quality homes.


## 5. Model Building
- Trained the data on various regression models namely, linear regression, random forest, gradient boosting, XGBoost, Ridge Regressor, and Lasso Regressor.
- The model was trained on 80% of the data and evaluated on the remaining 20%.
- Python packages used: scikit-learn, matplotlib, plotly, pandas, seaborn, numpy.
- Development Environment: Jupyter.
- Evaluated the model on  various metrics like r2score, mean squared error, mean absolute error, and root mean squared error.
  ![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/bf5e49e6-85d3-4678-a1cd-c05741013899)
- Conducted five-fold cross-validation to enhance model performance, observing improved results with random forest and XGBoost regressor.
- Further optimized model performance by varying the number of folds (3-12) specifically for Random Forest and XGBoost regressors.
- Ultimately, chose XGBoost regressor for model development due to its superior performance with 10-fold cross-validation. 


## 6. Application of Trained Models
- Developed a web application to deploy my model using the Django framework.
- Used pycharm as a development environment.

## 7. Conclusion
- Identified key trends such as location, construction year, and property condition influencing house prices.
- Optimized model performance using machine learning techniques and cross-validation, selecting XGBoost as the final model.
- Developed a user-friendly Django-based interface for buyers and sellers to obtain accurate price estimates, contributing to transparency and efficiency in the real estate market.
#### Future Scope
-Incorporating Real-Time Data and Economic Trends
Can integrate additional real-time data sources and economic indicators, automate data updates, and analyze macroeconomic trends to enhance the accuracy and timeliness of our house price predictions.
- Exploring the Impact of Emerging Technologies
Future efforts might focus on leveraging advanced AI techniques and integrating IoT data to improve predictive accuracy and understanding the impact of technology-driven market trends on housing values.
- Developing Personalized Price Prediction Models
We can plan to build detailed user profiles, create interactive tools for customized valuations, and implement feedback mechanisms to continuously refine our models based on user input and preferences.
















