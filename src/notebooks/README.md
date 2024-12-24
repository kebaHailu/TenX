## TellCo Telecom Analysis

### Overview

This report provides a detailed analysis of TellCo, a mobile service provider in the Republic of Pefkakia, to assess its potential for acquisition. The analysis focuses on customer activities and behaviors derived from a month's aggregation of xDR records. The goal is to identify opportunities for growth and profitability by understanding the underlying data and making informed recommendations.

### Data Source

The dataset consists of xDR records, which include detailed information about customer interactions on the network. The data is stored in a PostgreSQL database, and the schema along with the SQL file for extraction is provided.

### Learning Outcomes

1. **Business Context Understanding**: Analyze the telecom market and identify key metrics that drive profitability.
2. **Data Insight Extraction**: Utilize various techniques to explore the dataset, including statistical analysis and visualizations.
3. **Dashboard Development**: Create an interactive dashboard using Streamlit to present findings and insights effectively.

### Project Objectives

The project is divided into four main objectives:

1. **User Overview Analysis**: Understand customer demographics and behaviors.
2. **User Engagement Analysis**: Measure customer engagement through various metrics.
3. **User Experience Analysis**: Evaluate network performance and customer satisfaction.
4. **Satisfaction Analysis**: Assess overall customer satisfaction based on engagement and experience metrics.

### Methodology

#### User Overview Analysis

- Identify the top 10 handsets and the top 3 manufacturers.
- Analyze user behavior across applications (Social Media, Google, Email, etc.).
- Conduct exploratory data analysis (EDA) to identify missing values and outliers.

#### User Engagement Analysis

- Aggregate metrics such as session frequency, duration, and total traffic per customer.
- Normalize engagement metrics and apply k-means clustering to classify customers.

#### User Experience Analysis

- Analyze network parameters (TCP retransmission, RTT, Throughput) and their impact on user experience.
- Perform k-means clustering to segment users based on experience metrics.

#### Satisfaction Analysis

- Calculate engagement and experience scores for each user.
- Build a regression model to predict satisfaction scores and analyze the results.

### Conclusion

This analysis aims to provide actionable insights that can guide the investor in making an informed decision regarding the acquisition of TellCo. By focusing on the most profitable aspects of the business, such as user engagement and satisfaction, the investor can drive significant growth and profitability.

### Next Steps

- Develop a comprehensive dashboard to visualize the findings.
- Prepare a detailed report summarizing the analysis and recommendations for the investor.
