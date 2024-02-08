## 1. Title and Author

- House Price Prediction
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Sri Vaishnavi Kudikala
- Github:https://github.com/SriVaishnaviK
- LinkedIn:https://www.linkedin.com/in/vaishnavikudikala
- Presentation:
- Youtube:
    
## 2. Background


This project centers on predicting house prices by leveraging diverse factors such as location, construction details, and interior features, drawing insights from a dataset obtained from the UCI Machine Learning Repository. The comprehensive dataset enables a thorough examination of trends in house pricing. The significance lies in providing a valuable tool for potential buyers and sellers to make well-informed decisions. Additionally, it aids real estate professionals in strategically setting competitive prices, fostering efficiency in the market. The project's broader impact lies in enhancing transparency within the real estate sector, where a nuanced understanding of the various factors influencing housing prices contributes to a more informed and responsive market.
#### Research Questions
- Temporal Price Trends: Explore house price changes over time, identifying significant fluctuations and underlying drivers.
- Geographical Price Analysis: Correlate location (latitude, longitude, zip code) with prices, identifying high/low areas and reasons for spatial variations.
- Impact of Interior Features: Analyze bedrooms, bathrooms, and square footage influence on prices, identifying key contributors.
- Quality and Condition Impact: Investigate how construction grade and property condition affect prices, assessing higher-grade property premiums.
- Waterfront and View Analysis: Explore how waterfront and view index influence prices, assessing the value of desirable views.
- Renovation Effects: Examine how renovations impact prices, determining if recent renovations correlate with higher property values.

## 3. Data 


- The dataset originates from the UCI Machine Learning Repository and is sourced from [Kaggle](https://www.kaggle.com/datasets/astronautelvis/kc-house-data/data).
- The dataset size is 2.03MB.
- Data shape: (21613, 21)
- Data Dictionary:
| Column Name     | Definition                                                | Data Type |
|-----------------|-----------------------------------------------------------|-----------|
| Unnamed: 0      | Index or identifier for each home sold                    | `int64`   |
| id              | Unique ID for each home sold                               | `int64`   |
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

 
  
- Which variable/column will be your target/label in your ML model?
- Which variables/columns may be selected as features/predictors for your ML models?
