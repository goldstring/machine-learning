<h1 style='text-align:center;color:red;'>Loan Approval Prediction Using Machine Learning Python</h1>
<h1>Problem Statement</h1>
    <p>
        Design and implement a <strong>Loan Approval Prediction Model</strong> to determine whether a loan application should be approved or denied based on the applicant's demographic, financial, and credit history information. 
        The goal is to build a classification model that predicts the loan approval status (<code>loan_status</code>) using features such as the applicant's age, gender, education, income, employment experience, home ownership status, 
        loan amount, loan intent, interest rate, and credit history. This model can help financial institutions automate the loan approval process, reduce risk, and improve decision-making.
    </p>
    <h2>Dataset Description</h2>
    <p>
        The dataset contains detailed information about individuals applying for loans, their financial attributes, and loan-related metrics. Below is a description of the dataset:
    </p>
    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>person_age</code></td>
                <td>Age of the loan applicant in years.</td>
            </tr>
            <tr>
                <td><code>person_gender</code></td>
                <td>Gender of the loan applicant (male or female).</td>
            </tr>
            <tr>
                <td><code>person_education</code></td>
                <td>Education level of the loan applicant (e.g., High School, Bachelor, Master).</td>
            </tr>
            <tr>
                <td><code>person_income</code></td>
                <td>Annual income of the loan applicant (in USD).</td>
            </tr>
            <tr>
                <td><code>person_emp_exp</code></td>
                <td>Number of years of employment experience of the applicant.</td>
            </tr>
            <tr>
                <td><code>person_home_ownership</code></td>
                <td>Home ownership status of the applicant (e.g., RENT, OWN, MORTGAGE).</td>
            </tr>
            <tr>
                <td><code>loan_amnt</code></td>
                <td>Amount of loan requested (in USD).</td>
            </tr>
            <tr>
                <td><code>loan_intent</code></td>
                <td>The purpose or intent of the loan (e.g., PERSONAL, EDUCATION, MEDICAL).</td>
            </tr>
            <tr>
                <td><code>loan_int_rate</code></td>
                <td>Interest rate of the loan (as a percentage).</td>
            </tr>
            <tr>
                <td><code>loan_percent_income</code></td>
                <td>Loan amount as a percentage of the applicant's annual income.</td>
            </tr>
            <tr>
                <td><code>cb_person_cred_hist_length</code></td>
                <td>Length of the applicant's credit history (in years).</td>
            </tr>
            <tr>
                <td><code>credit_score</code></td>
                <td>Credit score of the applicant.</td>
            </tr>
            <tr>
                <td><code>previous_loan_defaults_on_file</code></td>
                <td>Whether the applicant has previous loan defaults on record (Yes or No).</td>
            </tr>
            <tr>
                <td><code>loan_status</code></td>
                <td>Target variable indicating whether the loan was approved (1) or denied (0).</td>
            </tr>
        </tbody>
    </table>
    <h2>Use Case</h2>
    <p>
        This model can assist financial institutions and lenders by:
    </p>
    <ul>
        <li>Automating the loan approval process for faster decision-making.</li>
        <li>Identifying high-risk loan applications based on applicant profiles.</li>
        <li>Improving customer satisfaction by minimizing manual interventions.</li>
        <li>Enhancing financial stability by reducing the likelihood of defaults.</li>
    </ul>
    <p>
        This system can be integrated into banking and financial software to streamline operations and support data-driven decisions.
    </p>
