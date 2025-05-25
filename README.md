# Career Advancement Tool (CAT) 🚀<!-- Largest title: h1 -->
  BECAUSE OF A PROBLEM WITH VIEWING THE NOTEBOOK IN A NORMAL FORMAT, WE ARE KINDLY ASKING YOU TO DONWLOAD THE HTML OR IPYNB FILE IN ORDER TO VIEW OUR WORK.
## Introduction 📝<!-- Second largest title: h2 -->
CAT is an innovative feature within LinkedIn, designed to increase job marketability by aligning user resumes with current industry standards and suggesting skill enhancements through Machine Learning and Large Language Models (LLM). The tool focuses on bridging the gap between current professional skills and the ever-evolving job market requirements.

## Data Collection and Integration <!-- h3 -->
Data sources include LinkedIn's profile dataset complemented by web scraping for real-time job market demands and LinkedIn Learning courses. We strategically focus on the data science sector, integrating a neural network to predict relevant skills, which achieved over 90% accuracy on our datasets.

Top frequent skill count in the kaggle job postings dataset:
![image](https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT/assets/81235287/93d66362-50cb-43fe-849a-1a3c72eae86f)

Feature distribution from profiles dataset:
![image](https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT/assets/81235287/2638f24e-827f-43e2-8fac-8b33fd57874a)


## AI Methodologies 💡<!-- h4 -->
The project leverages several AI techniques:

DistilBert for tokenizing job titles into vectors.
Neural Network for predicting skills from job titles and company names.
Bucketed Random Projection LSH and KNN for matching user profiles to job opportunities.
Gemini LLM for extracting skills, generating insights, and recommending courses, with an adjusted selection of 750 courses to fit token limits.

Gemini's Insights and course recommendation output example:
![image](https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT/assets/81235287/2891d644-0b9d-41d9-87e9-dbf2a99c6bff)

KNN output for 5 nearest neighbors:
![image](https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT/assets/81235287/b68c1d9b-2fbe-4ad9-a1e3-0f4e70c7ed90)


## Evaluation and Results <!-- h5 -->
The neural network shows strong predictive performance. The combination of BRP LSH and KNN provides precise profile matching. Gemini's recommendations have led to positive user engagement and profile improvements.

Neural Net training process:
![image](https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT/assets/81235287/4aa553e7-6543-416a-aa42-c42796073fc0)
Skills sets distribution (of the scrapped data and the predicted data):
![image](https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT/assets/81235287/1924ada4-d183-4f7b-af3d-1524f2d82a87)

## Limitations and Reflections <!-- Smallest title: h6 -->
Challenges such as unavailable skills data, initial KNN implementation hurdles, and computational performance were addressed through innovative solutions, including a neural network for skill prediction and a refined two-step matching process.

## Conclusion <!-- Back to h2 for section consistency -->
CAT has demonstrated the potential to enhance career development significantly. Despite limitations, the tool has successfully provided personalized guidance and recommendations, establishing itself as a valuable asset in the job-seeking process.



## Usage

This project is designed to work with linkedin profiles dataset that is not publicly available. We provided a snippet to this dataset in the "Other Resources" section below.
Remember to replace all the file paths in the notebook to your local file paths.

### Running the Project 🏃

To run the project, you will need Jupyter Notebook to open the `.ipynb` file. Follow these steps:

1. Ensure that you have Jupyter Notebook installed. If not, install it using `pip`:

    ```bash
    pip install notebook
    ```

2. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yogev-namir/Linkedin-Career-Advancement-Tool-CAT
    ```

3. Navigate to the cloned repository's directory.

4. Place the provided datasets into this directory (profiles dataset, kaggle's job postings and scraped courses dataset)

5. Open the Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

6. In the Jupyter interface, open `Project Python Notebook.ipynb`.

7. Run the cells in sequence to execute the analysis.

### Other Resources

- View the project report: `Project_Report.pdf`
- Check the web scraping script: `courses_scrapping.py` for details on how LinkedIn Learning courses data is collected.
- Check the job postings parsing script : 'job_postings_parsing' for details on how job postings are parsed and ordered.
- Kaggle's job postings dataset - https://www.kaggle.com/datasets/asaniczka/data-science-job-postings-and-skills?select=job_skills.csv
- Linkedin profiles snippet dataset - https://www.kaggle.com/datasets/manishkumar7432698/linkedinuserprofiles

## Contributing

We welcome contributions and suggestions for improvements! If you have ideas on how to enhance the Career Advancement Tool (CAT), please feel free to:

- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Make your changes.
- Commit your changes (`git commit -am 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Create a new Pull Request.

Your contributions will help make our project even better. If you have any questions or need further assistance, please open an issue in the repository.

## Contact 📬
yonatansabag@gmail.com

yogevnamir97@gmail.com

oribar1812@gmail.com
