# Coffee Shop Chatbot System

## Overview

This repository contains the code and resources for a chatbot system designed for a coffee shop app. The system utilizes advanced AI models to provide personalized product suggestions and engage users effectively. It serves as a bridge between a React Native frontend and a robust backend, leveraging various technologies to ensure a smooth and dynamic user experience.

## Directory Structure

- **API**  
  This folder contains the code for the API that handles requests to the chatbot agent system. It serves as the bridge between the React Native app and the backend functionality.

- **Dataset**  
  This folder includes the downloaded dataset from Kaggle used for training the recommendation engine. It serves as the foundation for generating personalized product suggestions.

- **Products**  
  Contains product information utilized in the app, including names, prices, descriptions, and images. This data is essential for displaying products within the app and for the chatbot's responses.

- **Notebooks**  
  - **build_vector_database.ipynb**: A Jupyter notebook that constructs the vector database for the Retrieval-Augmented Generation (RAG) model, facilitating efficient data retrieval for the chatbot.
  
  - **firebase_uploader.ipynb**: A Jupyter notebook that uploads product data to Firebase, enabling the React Native app to fetch this data dynamically.
  
  - **recommendation_engine_training.ipynb**: A Jupyter notebook that trains the market basket analysis recommendation model, which is used by the recommendation agent to provide personalized product suggestions.

- **Python Code for Coffee Shop Chatbot**  
  This folder contains the Python code and notebooks necessary for building and deploying the chatbot system for the coffee shop app. The code is organized into several components, each serving a specific function within the overall project.

## Technologies Used

- **Language Model**: LLama 3
- **Data Storage**: Firebase
- **Vector Database**: Pinecone
- **Jupyter Notebooks**: For data processing and model training
- **Backend**: Python

## Getting Started

1. **Clone the Repository**  
   Clone this repository to your local machine using:
   ```bash
   git clone <repository-url>
2. **Set Up Firebase**
Configure Firebase for your project and update the necessary credentials in the application.

3. **Run Jupyter Notebooks**
Use Jupyter to run the notebooks in the Notebooks directory to set up your vector database and train the recommendation engine.

4. **Start the API**
Launch the API server to handle requests from the React Native app.

5. **Launch the React Native App**
Follow the React Native documentation to run the app on your device or emulator.

## Acknowledgments
Kaggle for the datasets
Firebase for data storage solutions
Pinecone for vector database services
