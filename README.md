# Multi-Agent System: Planning Errors Framework

## Context
This framework is used for reasoning errors in the **planning phase** and does not cover other types of errors, such as runtime, communication, or other types of failures.

## Key Areas to Address

### 1. Planning Errors
These are errors that arise specifically in the planning phase of the system's operation. They can occur when the planning process fails to properly address certain aspects of the task or agent capabilities.

### 2. Ambiguity in Understanding the Scope and Granularity of the Task or Steps
- Sometimes, the scope of the task or the individual steps in the plan might not be well-defined or understood by the agents.
- Granularity refers to the level of detail in each step of the plan, and improper granularity can lead to confusion or mistakes during execution.

### 3. Agent Availability
- The plan may assume that an agent is available for a particular task, but the agent might not be present or may not be available due to other constraints (e.g., scheduling conflicts, lack of resources, etc.).
- Errors can occur when assumptions about agent availability are incorrect or not properly validated.

---

## Step 1: Create an Initial Framework of Agents and Tasks

### 1.1 Framework of Agents
- Define the agents that will be involved in the process.
- Specify their capabilities, availability, and limitations.
- Create a model for how agents interact with one another during the planning and execution phases.

### 1.2 Task Definition
- Develop a complex and robust task that involves a lot of steps.
- The task should be complex enough to generate errors during the planning phase, ensuring the model accounts for potential planning errors.
- The task should be designed such that it is susceptible to errors in planning (e.g., errors due to ambiguity, miscommunication, or incorrect assumptions).

### 1.3 Error-Prone Planning
- The task should be structured in a way that the planning process is error-prone—this could be due to the complexity, number of steps, or dependencies between tasks.
- It’s important that the framework be tested under conditions where errors are likely to emerge, providing insights into the planning challenges and areas for improvement.

### 1.4 Forward (Drafting) vs Backward (LURER)

# Data Science Life Cycle for Multi-Agent System (LLM)

## 1. Process the CSV Files
### 1.1 Get File Path
- Accept multiple CSV files as input.
- **Input**: List of file paths.
- **Action**: Check if the input is a valid file path.
- **Output**: Path(s) of CSV files or error if invalid paths are detected.

### 1.2 Check if it's a Valid CSV
- Validate if each file is a proper CSV format.
- **Input**: File(s) from **1.1**.
- **Action**: Use Python’s `os.path` and `pandas` `read_csv` to verify the integrity of each file.
- **Output**: Confirmation of valid CSV or error message.

### 1.3 Convert CSV to Pandas DataFrame
- Convert each valid CSV file into a `pandas` DataFrame.
- **Input**: Valid CSV file(s).
- **Action**: Use `pd.read_csv()` to load data into a pandas DataFrame.
- **Output**: List of pandas DataFrames, one per CSV.

---

## 2. Data Cleaning
### 2.1 Identify and Handle Missing Data
- Check for null values or missing data in each DataFrame.
- **Input**: DataFrames from **1.3**.
- **Action**: Handle missing data with imputation or removal (`df.fillna()` or `df.dropna()`).
- **Output**: Cleaned DataFrame(s) with no missing values.

### 2.2 Remove Duplicates
- Check for duplicate rows and remove them.
- **Input**: DataFrames from **1.3**.
- **Action**: Use `df.drop_duplicates()` to eliminate duplicate entries.
- **Output**: DataFrame(s) without duplicates.

### 2.3 Correct Data Types
- Ensure each column has the correct data type (e.g., numerical columns are floats/ints, categorical columns are strings).
- **Input**: DataFrames from **1.3**.
- **Action**: Use `df.astype()` to correct column data types.
- **Output**: Corrected DataFrame(s) with appropriate data types.

### 2.4 Prompt the User for Further Actions
- Ask the user if additional custom cleaning steps are required (e.g., outlier handling, normalization).
- **Input**: Cleaned DataFrame(s).
- **Action**: Provide a list of potential cleaning steps (e.g., "Remove outliers", "Normalize columns").
- **Output**: User input for further cleaning actions.

---

## 3. Aggregation and Transformation
### 3.1 Aggregating Data (if multiple CSVs are provided and `aggregate` is True)
- Check if aggregation is required (boolean flag).
- **Input**: List of DataFrames, aggregation flag.
- **Action**: 
  - Merge the DataFrames if the flag is `True` (`pd.concat()` or `pd.merge()`).
  - If not aggregated, retain separate DataFrames.
- **Output**: Aggregated DataFrame or separate DataFrames.

### 3.2 Extract the Size and Columns
- Extract the dimensions (size) of the DataFrames and their columns for analysis.
- **Input**: Aggregated DataFrame(s).
- **Action**: Use `df.shape` and `df.columns` to extract size and columns.
- **Output**: Tuple of size (rows, columns) and column names.

### 3.3 Pivoting Data
- Depending on the need, pivot the data longer or wider.
- **Input**: DataFrame(s) to be pivoted.
- **Action**: Use `df.pivot()` or `df.melt()` to adjust the shape of the DataFrame.
- **Output**: Pivoted DataFrame(s).

---

## 4. Statistical Findings
### 4.1 List of Columns and Desired Analysis
- Allow the user to select columns for statistical analysis.
- **Input**: DataFrame(s) with cleaned data.
- **Action**: Display column names and prompt user to select columns to analyze.
- **Output**: List of selected columns.

### 4.2 Generate Statistical Findings
- Generate statistics for the selected columns (mean, median, standard deviation, etc.).
- **Input**: Selected columns.
- **Action**: Use `df.describe()` and custom statistical functions to generate the findings.
- **Output**: Summary of statistical findings.

### 4.3 Code Generation for Statistical Analysis
- Automatically generate code snippets for common statistical tasks.
- **Input**: User request or predefined tasks (e.g., correlation, regression).
- **Action**: Use predefined templates or code generation techniques to create Python code.
- **Output**: Generated Python code for statistical analysis.

---

## 5. Machine Learning Application
### 5.1 Choose a Machine Learning Library (e.g., Scikit-learn)
- Provide the user with options for machine learning libraries (e.g., Scikit-learn).
- **Input**: User choice of library or default to Scikit-learn.
- **Action**: Import the chosen library.
- **Output**: Selected machine learning library.

### 5.2 Allow User to Specify Model
- Allow the user to specify which model to use (e.g., Linear Regression, Decision Tree).
- **Input**: Model choice (e.g., `LogisticRegression()`, `RandomForestClassifier()`).
- **Action**: Implement the specified model using the chosen library.
- **Output**: Trained machine learning model.

### 5.3 Train and Evaluate Model
- Train the model using the training data and evaluate it on test data.
- **Input**: Cleaned data and model.
- **Action**: Use `model.fit()` and `model.score()` to train and evaluate the model.
- **Output**: Model performance metrics (e.g., accuracy, RMSE).

---

## 6. Visualization
### 6.1 Visualization Setup
- Provide an output directory where visualizations (e.g., plots, charts) will be saved.
- **Input**: Output directory.
- **Action**: Create an output folder for saving visualizations.
- **Output**: Directory for saving plots.

### 6.2 Generate Visualizations
- Create various visualizations like histograms, scatter plots, box plots, etc.
- **Input**: Data to visualize (e.g., DataFrame, statistical findings).
- **Action**: Use libraries like `matplotlib`, `seaborn`, or `plotly` to generate visualizations.
- **Output**: Saved visualization files (e.g., PNG, PDF).

---

## 7. Report Writing
### 7.1 Compile Findings and Visualizations
- Compile statistical findings and visualizations into a structured report.
- **Input**: Statistical findings, visualizations.
- **Action**: Generate a markdown or LaTeX document with findings and charts.
- **Output**: Structured report (e.g., Markdown, PDF).

### 7.2 Determine Importance of Findings
- Assess whether the findings are important for decision-making.
- **Input**: Statistical and visualization outputs.
- **Action**: Use heuristics or model-based approaches to classify findings as important or not.
- **Output**: Highlighted important findings in the report.

---

## Summary of Data Science Life Cycle:
This cycle handles multiple CSV files, processes the data, cleans and aggregates it, performs statistical analysis, applies machine learning, generates visualizations, and writes reports. The system uses a combination of predefined steps, user interactions, and automated processes to create a robust workflow.
