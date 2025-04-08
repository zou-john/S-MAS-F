from langchain_core.prompts import PromptTemplate

# define the template for the data science workflow
data_science_workflow_template = """
Given multiple CSV files, execute the following data science workflow:

1. **Ingest & Validate**: Load the CSV files into DataFrames and check for missing values, data types, and consistency.
2. **Clean & Transform**: Handle missing data, outliers, and apply necessary feature engineering (e.g., encoding, scaling).
3. **Statistical Analysis**: Generate descriptive stats, correlation matrix, and conduct hypothesis tests if needed.
4. **Machine Learning**: Preprocess data, split into training/test sets, train a model, and evaluate performance using metrics (e.g., accuracy, precision).
5. **Visualizations**: Create key plots (e.g., histograms, scatter plots, heatmaps) to visualize data and model performance.
6. **Report**: Summarize findings, analysis, model results, and visualizations in a report (PDF or HTML).
"""

# create a Langchain PromptTemplate instance
data_science_workflow_prompt = PromptTemplate(template=data_science_workflow_template, input_variables=[])

