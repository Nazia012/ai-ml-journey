1. What is machine learning?
2. AI/ML/DL
3. Types of machine learning
4. Batch learning /Offline machine learning
5. Online machine learning
6. Instance based / model based machine learning
7. Challenges in machine learning
8. Application of machine learning

9. Machine learning development cycle (MLDLC)
### **What is MLDLC?**
* **Definition:** Just like the Software Development Life Cycle (SDLC) provides guidelines for building standard software, the **Machine Learning Development Life Cycle (MLDLC)** is a structured, step-by-step set of guidelines for building end-to-end ML-based software products—from initial idea to final deployment.
* **Why It Matters:** Training a model and checking its accuracy in a notebook is only one small piece of the puzzle. Real-world data science roles and interviews require understanding the complete lifecycle of shipping and maintaining a working product.

### **The 9 Stages of MLDLC**

1. **Framing the Problem**
* Define the exact business problem, target customers, budget, team size, and expected end product before writing any code.
* Decide on the technical approach: supervised vs. unsupervised learning, online vs. batch learning, suitable algorithms, and potential data sources.

2. **Data Gathering**
* Collect and store data in a usable format (such as CSV) from real-world sources:
* **APIs:** Fetch data programmatically (typically in JSON format) and convert it.
* **Web Scraping:** Extract data directly from websites when public APIs aren't available.
* **Data Warehouses (ETL):** Extract, Transform, and Load data from live production databases into a warehouse so ML experiments don't crash or slow down live applications.
* **Big Data Clusters:** Query massive datasets stored across distributed tools like Apache Spark.

3. **Data Preprocessing**
* Raw data is rarely clean. Transform it into a format that ML algorithms can consume accurately:
* Remove duplicate records and handle missing values.
* Detect and remove outliers.
* **Feature Scaling / Standardization:** Bring numerical columns with vastly different ranges onto a common scale so distance-based algorithms aren't skewed.


4. **Exploratory Data Analysis (EDA)**
* Deeply explore and visualize the data to uncover hidden patterns and relationships between inputs and outputs before building a model:
* **Univariate Analysis:** Analyze single columns individually (mean, standard deviation, distribution curves).
* **Bivariate & Multivariate Analysis:** Study relationships across two or multiple columns together.
* Address **imbalanced datasets** (e.g., when one class has significantly more samples than another) and perform additional outlier handling.


5. **Feature Engineering & Feature Selection**
* **Feature Engineering:** Create new, more informative input columns from existing ones (e.g., combining separate room and bathroom counts into a single total square-footage feature).
* **Feature Selection:** Drop redundant or irrelevant input columns that don't impact the output. Removing unnecessary features improves model performance and reduces training time.

6. **Model Training, Evaluation & Selection**
* **Training:** Train multiple algorithms from different model families (linear models, tree-based models, neural networks, etc.) on the same dataset, as no single algorithm works best for every problem.
* **Evaluation:** Compare models using task-specific performance metrics (e.g., Accuracy for classification, Mean Squared Error for regression, Dunn Index for clustering).
* **Selection & Tuning:** Pick the top-performing model(s), optimize their settings via **Hyperparameter Tuning**, and optionally combine multiple models using **Ensemble Learning** (Bagging, Boosting, Stacking) for stronger predictions.


7. **Model Deployment**
* Turn the trained model into a live software service that users can interact with (via a website, mobile app, or desktop app):
* Export the model as a serialized binary file (e.g., using `pickle`).
* Wrap it inside an **API** that accepts user inputs and returns predictions (usually in JSON format).
* Host the application and backend on cloud platforms such as AWS, Google Cloud Platform (GCP), or Heroku.

8. **Testing**
* Roll out the deployed model to a small group of trusted or loyal users (**Beta Testing** or **A/B Testing**) to gather real-world feedback.
* If performance falls short, loop back to earlier stages (data quality, preprocessing, feature selection, or model choice) to diagnose and fix the issue before a full launch.

9. **Optimization & Maintenance**
* Once validated, launch to all users and set up production safeguards:
* **Backups & Rollbacks:** Maintain regular backups of data and models with automated rollback mechanisms in case of failure.
* **Load Balancing:** Distribute incoming user traffic efficiently to keep response times fast.
* **Combating Model Decay ("Rotting"):** Models degrade over time as real-world data evolves. Automate periodic retraining schedules (weekly, monthly, etc.) and continuously optimize infrastructure costs.

10. Data engineer vs ml engineer vs data analyst vs data scientist

