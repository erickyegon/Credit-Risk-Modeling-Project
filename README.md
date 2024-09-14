# Insurance Premium Prediction Project

## Project Background

Shield Insurance Company, operating in the insurance industry for over 20 years, faced a challenge in accurately predicting insurance premiums for its customers, particularly for younger age groups (25 and under). The company offers various insurance plans based on customer risk profiles and medical histories, but inaccurate premium predictions led to customer dissatisfaction and operational inefficiencies.

Key business metrics include:
- **Active Years:** 20+
- **Business Model:** Insurance services for individual and business clients
- **Key Metrics:** Customer retention, premium accuracy, claims ratio

The company's primary focus is ensuring fair and accurate premium pricing across all customer segments, with particular attention to younger customers, where the highest error margins were observed.

---

## Insights and Recommendations:

### Category 1: Model Performance
- **Main Insight 1:** The existing model had a 92% overall accuracy, but 30% of predictions had error margins exceeding 10%.
- **Main Insight 2:** Some predictions, especially for younger customers (25 and under), had error margins as high as 87%.
- **Main Insight 3:** The XGBoost model used for customers over 25 achieved a 99% accuracy rate.
- **Main Insight 4:** Linear regression, used for younger customers, provided a baseline accuracy of 60%, indicating the need for further improvements in this segment.

### Category 2: Customer Segmentation
- **Main Insight 1:** Segmenting the model by age group led to a significant reduction in prediction errors for older customers.
- **Main Insight 2:** Model B, tailored for customers over 25, significantly improved prediction accuracy, meeting the company’s goal for high accuracy (>97%).
- **Main Insight 3:** Model A, targeted at younger customers, identified areas for improvement, particularly in incorporating lifestyle factors and genetic risk scores.
- **Main Insight 4:** Segmentation allowed for more tailored feature engineering, improving the relevance of predictions across different age groups.

### Category 3: Error Analysis and Feature Importance
- **Main Insight 1:** Error analysis identified specific features, such as medical history and lifestyle, that caused the most prediction errors for younger customers.
- **Main Insight 2:** Introducing a risk score based on medical history improved model performance, contributing significantly to accuracy.
- **Main Insight 3:** Error rates were analyzed using histograms and distribution plots, identifying patterns that helped refine the models.
- **Main Insight 4:** Iterative improvements through continuous error analysis and feedback from stakeholders led to better alignment with business needs.

### Category 4: Cloud Deployment and Model Access
- **Main Insight 1:** The model was successfully deployed using Streamlit, providing real-time premium predictions for insurance underwriters.
- **Main Insight 2:** Cloud deployment ensures that underwriters can access the model from any location, streamlining operations and improving efficiency.
- **Main Insight 3:** By optimizing for larger datasets and multiple users, the Streamlit deployment will scale as usage increases.
- **Main Insight 4:** The model’s deployment on Streamlit ensures seamless integration with the company’s operational workflows.

---

## Data Structure & Initial Checks

The company's main database structure consists of four tables: 
- **Table 1: Customers** - Contains demographic and medical history data.
- **Table 2: Policies** - Records of the insurance policies held by each customer.
- **Table 3: Claims** - Data on insurance claims made by customers.
- **Table 4: Premiums** - Details on premium amounts and historical predictions.

[Entity Relationship Diagram here]

---

## Executive Summary

### Overview of Findings
The overarching findings from the analysis suggest that a segmented model approach is necessary for accurate premium prediction. For customers over 25, XGBoost provided highly accurate predictions, while for customers aged 25 and under, additional feature engineering and data collection are required. Age and medical history were key factors in determining premium accuracy.

**Three Key Insights:**
1. Age-based segmentation is critical for improving prediction accuracy.
2. Medical history, especially when encoded as a risk score, significantly impacts premium prediction accuracy.
3. Cloud deployment via Streamlit enhanced accessibility for underwriters, improving operational efficiency.

[Visualization: Snapshot of the overall premium prediction accuracy trends]

---

## Insights Deep Dive

### Category 1: Model Performance
- **Main Insight 1:** The overall model achieved 92% accuracy, but younger customers experienced higher error rates.
- **Main Insight 2:** XGBoost provided 99% accuracy for older customers, surpassing the 97% target.
- **Main Insight 3:** Linear regression for younger customers (Model A) achieved only 60% accuracy.
- **Main Insight 4:** Continuous model refinement is required to improve predictions for younger age groups.

[Visualization specific to Model Performance]

### Category 2: Customer Segmentation
- **Main Insight 1:** Segmenting by age groups improved the model's accuracy and reduced error rates.
- **Main Insight 2:** The risk score created from medical history proved essential in improving predictions.
- **Main Insight 3:** Feature engineering, such as encoding lifestyle factors, is necessary to improve the accuracy of Model A.
- **Main Insight 4:** Segmentation allowed the model to cater to distinct age groups' characteristics, enhancing overall accuracy.

[Visualization specific to Customer Segmentation]

### Category 3: Error Analysis and Feature Importance
- **Main Insight 1:** Error patterns revealed a need for better feature representation for younger customers.
- **Main Insight 2:** The risk score feature contributed significantly to model performance improvements for all age groups.
- **Main Insight 3:** Histograms and distribution plots helped identify and analyze error patterns.
- **Main Insight 4:** New features, such as genetic risk and past claims, will further improve model performance.

[Visualization specific to Error Analysis]

### Category 4: Cloud Deployment and Model Access
- **Main Insight 1:** The Streamlit deployment allows real-time premium predictions for insurance underwriters.
- **Main Insight 2:** Cloud deployment ensures accessibility from any location, streamlining operational workflows.
- **Main Insight 3:** Scaling the Streamlit deployment for larger datasets will improve performance as usage grows.
- **Main Insight 4:** Integrating with the company’s systems ensures a seamless transition for operational staff.

[Visualization specific to Deployment]

---

## Recommendations:

Based on the insights and findings above, we recommend the [Stakeholder Team] consider the following:

- **Observation:** Model A accuracy is suboptimal for customers aged 25 and under.  
  **Recommendation:** Further data collection and feature engineering (e.g., lifestyle factors) are necessary to improve Model A.
  
- **Observation:** Model B has achieved optimal accuracy for older customers.  
  **Recommendation:** Focus on maintaining and scaling Model B’s performance as more data becomes available.

- **Observation:** Real-time predictions are crucial for operational efficiency.  
  **Recommendation:** Continue enhancing the Streamlit deployment to handle more data and users as the company scales.

- **Observation:** Error analysis has identified critical areas for improvement.  
  **Recommendation:** Focus on improving the risk score calculation and incorporating new features like genetic risk.

---

## Assumptions and Caveats:

Throughout the analysis, several assumptions were made to address challenges with the data. These assumptions include:

- **Assumption 1:** Missing values for certain demographic fields were replaced with the median values for customers in similar categories.
- **Assumption 2:** Medical history data from 2021 was missing and imputed using historical trends and available data from 2020.
- **Assumption 3:** Outliers with extremely high premium predictions were removed to ensure model performance accuracy.

---

## Conclusion

By using a segmented model approach, tailored feature engineering, and deploying the model via Streamlit, we have significantly improved Shield Insurance’s ability to predict insurance premiums. While Model B achieved optimal accuracy, Model A requires further refinement. These efforts will continue to ensure accurate predictions for all customer segments, enhancing overall customer satisfaction and operational efficiency.
