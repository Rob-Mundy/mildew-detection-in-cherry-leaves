## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and Validation

### Hypothesis

- We suspect that leaves affected by mildew display identifiable traits, typically in the form of white, powdery patches of fungus that spread on either the upper or lower surfaces of the leaf. These distinct indicators will be adequate for training a machine learning model as they effectively distinguish between infected leaves and those that are fungus-free.
- Conducting an average image analysis can assist in further investigating the matter.
- We propose that employing binary classification would be the most suitable approach for discerning the distinction between infected and healthy leaves.

### Validation

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business Requirement 1: The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
  - "Mean" and "standard deviation" images will be displayed for healthy leaves and those presenting powdery mildew.
  - The difference between an average healthy leaf and the average mildew-infected leaf will be displayed.
  - An image montgage will follow for the selected label: healthy / powdery_mildew.
- Business Requirement 2: The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
  - We want to predict whether a random sample leaf image is presenting powdery mildew or is healthy.
  - We want to build a ML model with binary classification and report on the results.

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

### Page 1 - Project Executive Summary

- Succinct project summary
  - General Information
    - According to [The Royal Horticultural Society](https://www.rhs.org.uk/disease/powdery-mildews)
      powdery mildews are a group of related fungi which attack a wide range
      of plants, causing a white, dusty coating on leaves, stems and flowers.
    - The fungus sends feeding structures into the surface cells, greatly
      reducing the vigour of the plant.
    - If left unchecked, the fungus often spreads to a plant's fruits,
      compromising the quality.
    - Manual observations and visual verifications are currently required
      taking an average of 30 mins per tree.
  - Project Dataset
    - The available dataset contains 4208 images provided by the client from their manual observations, with equal quantities of both healthy and mildew-infected leaves.
  - Link to additional information in project README file
  - Business Requirements
    - 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    - 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2 - Leaf Health Visualiser

- To satisy business requirement 1: The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Difference between average leaf presenting powdery mildew and average healthy leaf
  - Checkbox 3 - Image Montage

### Page 3 - Mildew Detector

- To satisy business requirement 2: The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
  - Link to dataset where user can download a random sample of images for live prediction.
  - File uploader widget for user to upload sample images for live prediction.
    - Sample image(s) displayed with accompanying image dimensions.
  - The outcome of predictive analysis stating the likelihood of sample leaf exhibiting mildew or being in a healthy state.
    - Propability results in graphical form.
  - Table containing sample name and prediction.
  - Link to download csv file of predictions performed during session.

### Page 4 - Project Hypothesis and Validation

- Project Hypothesis
  - We suspect that leaves affected by mildew display identifiable traits, typically in the form of white, powdery patches of fungus that spread on either the upper or lower surfaces of the leaf. These distinct indicators will be adequate for training a machine learning model as they effectively distinguish between infected leaves and those that are fungus-free.
  - Conducting an average image analysis can assist in further investigating the matter.
  - We propose that employing binary classification would be the most suitable approach for discerning the distinction between infected and healthy leaves.
- Validation
  - xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### Page 5 - ML Performance Metrics

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- Given their busiess case similarities, Walkthrough Project 1: Malaria Detector was followed to conduct the study, build the ML model and construct the Streamlit site.

### Content

- General information about powdery mildew in the Executive Summary was sourced from [The Royal Horticultural Society](https://www.rhs.org.uk/disease/powdery-mildews)

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people that provided support throughout this project.
