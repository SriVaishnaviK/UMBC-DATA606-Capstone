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
- Columns bedrooms, bathrooms,sqft_living,sqft_lot, condition, grade,yr_built,yr_renovated, lat, long, and zipcode may be used as features for the ML model.

## 3. Exploratory Data Analysis(EDA)
- There were no missing or duplicated values in the dataset.
- To ensure data consistency and compatibility with the analysis, type conversions were performed on certain columns. Specifically, all the data were converted to integers wherever  necessary. This step was crucial for standardizing the data format and facilitating accurate analysis.
- Frequency Distribution of target Variable(Price)
  ![image](https://github.com/SriVaishnaviK/UMBC-DATA606-Capstone/assets/101724857/e01212f0-88a9-478c-850e-8366364a28d6)

