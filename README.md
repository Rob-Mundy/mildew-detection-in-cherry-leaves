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

xxxxxxxxxxxxxxxxxxxx

## Bugs

### Fixed Bugs

- The depolyed app's Mildew Detector was producing the following error when attempting to predict on new images: **AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'**.This ws resolved by specifying a different version **Pillow==9.5.0** in the requirements.txt file as instructed in this [StackOverflow](https://stackoverflow.com/questions/76616042/attributeerror-module-pil-image-has-no-attribute-antialias) article.

### Unfixed Bugs

- There are no unfixed bugs

## Deployment

### Heroku

- The App live link is: [rm-mildew-app](https://rm-mildew-app-4f738e29404d.herokuapp.com/)
- The project was deployed to Heroku using the following steps:

1. Create new app via CLI so that heroku-20 stack is specified which is compatible with python 3.8.12: $ heroku create rm-mildew-app --stack heroku-20 --region eu
2. At the Deploy tab, select GitHub as the deployment method.
3. Select repository name and click Search. Once it is found, click Connect.
4. Select Main and Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access App.
6. Add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

The following libraries and resources were used during the project (code examples provided):

- **Kaggle** was both the source and means of downloading the project dataset:
  [kaggle_data_retrieval](/workspaces/mildew-detection-in-cherry-leaves/assets/images/kaggle_dataset_download_image.png)

- **Numpy/Pandas** were used to convert images to arrays to allow classification predictions on new images, and

- **Matplotlib** was used to display graphical information and to construct the image montages throughout the project, such as this snippet from the image_montage function:
  [matplotlib_image_montage_code](/workspaces/mildew-detection-in-cherry-leaves/assets/images/matplotlib_image_montage_code_snippet.png)

- **Seaborn** was used for data visualisation, namely displaying and styling graphical data e.g.:
  [seaborn_styling_example_code](/workspaces/mildew-detection-in-cherry-leaves/assets/images/seaborn_styling_example_code.png)

- **TensorFlow** was used to load image files into an array (tensor) to enable data analysis and image processing as well as model creation and training e.g.:
  [tensorflow_array_code_example](/workspaces/mildew-detection-in-cherry-leaves/assets/images/tensorflow_array_code_example.png)

  [tensorflow_keras_model_creation_code_example](/workspaces/mildew-detection-in-cherry-leaves/assets/images/tensorflow_keras_model_creation_code_example.png)

  [tensorflow_keras_model_training_code_example](/workspaces/mildew-detection-in-cherry-leaves/assets/images/tensorflow_keras_model_training_code_example.png)

## Credits

- Given their busiess case similarities, Walkthrough Project 1: Malaria Detector was followed to conduct the study, build the ML model and construct the Streamlit site.

### Content

- General information about powdery mildew in the Executive Summary was sourced from [The Royal Horticultural Society](https://www.rhs.org.uk/disease/powdery-mildews)

### Media

- The images used for the dataset were sourced from this [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves) site.

## Acknowledgements (optional)

- Thank the people that provided support throughout this project.
