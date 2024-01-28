# Multilabel-Quote-Classifier

A text classification model from data collection, model training, and deployment. <br/>
The model can classify **675** different types of quote tags <br/>The keys of `deployment\tag_types_encoded.json` shows the quote tags

 ## Data Collection

Data was collected from BrainyQuote Website Listing: [![brainyquotes](https://img.shields.io/badge/www.brainyquote.com-blue)](https://www.brainyquote.com/topics) <br/>The data collection process is divided into 3 steps:

- **Category & URL Scraping:** The quotes URLs were scraped with `scraper\quote_url_scraper.py` and the URLs are stored along with the quote title in `scraper\quotes_urls.csv`.
- **Quote Details Scraping:** Using the URLs, the quotes, the authors, the category and the description URLs are scraped with `scraper\detail_data_scraper.py` and they are stored in `scraper\quotes.csv`.
- **Tags Scraping:** The final part was tag scraping and it was the difficult one. I split the total data into mini-batches and scrap tags with `scraper\tags_scraper.py` and stored in `data\quotes_data.csv`.

In total, I scraped 1,01,243 quotes with their author's name, categories and relevant tags. 

## Data Preprocessing

Initially, there were *9129* different tags in the dataset. After some analysis, I found out *8454* of them are rare (probably custom tags by users). So, I removed those tags and then I have *675* tags. After that, there were some duplicated values and I got a total of 1,01,201 samples after dropping them.

## Model Training

Finetuned `distilroberta-base` and `bert-base-uncased` models from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed in `notebooks\quotes_data_prep_and_model_implement.ipynb` or [![Colab](https://img.shields.io/badge/-quotes_data_prep_and_model_implement.ipynb-blue?logo=googlecolab)](https://colab.research.google.com/drive/1GcgSEmS1FCtnuL6XmPLurVufQJcYaSsa?usp=sharing)

## Result Comparison

Models|Accuracy|F1 Score(Micro)|F1 Score(Macro)
:---:|:---:|:---:|:---:
Distil Roberta Base| 99.83 % | 84.89 % | 52.42%
Bert Base Uncased| 99.84% | 88.60 % | 67.15 %

## Model Compression and ONNX Inference

The trained model has a memory of 422+MB. I compressed this model using ONNX quantization and brought it under 106MB. 

## Model Deployment

The compressed model is deployed to the HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [![hf interface](https://img.shields.io/badge/Hugging_face-Interface-FFFF00)](https://huggingface.co/spaces/kavinh07/quote-classifier)

<img src = "deployment\hugging_face_interface.png" width="700" height="400">

## Web Deployment
Deployed a Flask App built to take descriptions and show the tags as output. Check `flask` branch. The website is live [![website link](https://img.shields.io/badge/www.multilabelquoteclassifier.onrender.com-blue)](https://multilabelquoteclassifier.onrender.com)

<img src = "deployment\webpage-1.png" width="800" height="600">
<img src = "deployment\webpage-2.png" width="800" height="600">
