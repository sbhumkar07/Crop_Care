# Crop Disease Detection Web Application

## Goal
The primary goal of this project is to assist farmers in early detection of crop diseases, enabling timely intervention and treatment. The user interface is designed to be simple and accessible, with disease information and possible solutions provided in Marathi, the native language of many users. This project also emphasizes the creation of a custom dataset and collaboration with crop healthcare centers to ensure accurate and practical disease solutions.

## About the Project
This web application uses image classification to detect diseases in crops. By leveraging Transfer Learning techniques with VGG16 and MobileNet models, the application identifies diseases from images uploaded by users. When an image is uploaded, the application processes it and, if a disease is detected, displays the disease name along with a possible cure on the user interface.

### Key Features:
- **User-Friendly Interface:** Simple and intuitive design for easy navigation.
- **Bilingual Support:** Disease names and solutions are provided in Marathi.
- **Accurate Detection:** The model has been trained on a custom dataset for high accuracy.
- **Practical Solutions:** Solutions are derived from expert consultations with crop healthcare centers.

## Tech Stack
- **Libraries & Software:** NumPy, Matplotlib, TensorFlow, Keras, Flask, Anaconda, Google Cloud Platform.
- **Programming Languages:** Python 3.7, HTML, JavaScript.
- **Models:** VGG16, MobileNet.
- **Framework:** Flask.

## Implementation
### Steps Involved:
1. **Dataset Creation:** A custom dataset was developed by collecting images of various crops from agricultural sources.
2. **Model Training:** The image classification model was trained using VGG16 and MobileNet architectures, leveraging Transfer Learning to achieve high accuracy with a relatively small dataset.
3. **Web Application Development:** The front-end was created using HTML, CSS, and JavaScript. Flask was used for setting up routing and integrating the models into the application.
4. **Deployment:** The application was deployed using Google Cloud Platform, ensuring scalability and reliability.

### Setup Instructions
1. **Clone the Repository:**
   git clone https://github.com/yourusername/Crop_Disease_Detection.git
   cd Crop_Disease_Detection
2. **Set Up a Virtual Environment:**

    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install Required Libraries:**
    pip install -r requirements.txt

4. **Download the Model Weights:**
    Ensure that you have the .h5 model files in the static/weights directory. If not, download them or train your models as required.

### How to Run the Project
Start the Flask Application: python new_core_app.py
Access the Web Application: Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.

### How to Use the Application
Upload an Image: Navigate to the crop-specific page (e.g., Corn, Potato) using the navigation menu. Upload an image of the crop by clicking on the "Upload" button.
Analyze the Image:Click on the "Analyze Image" button to process the uploaded image. The application will display the detected disease and a suggested treatment.

## Details About the Models
VGG16: A pre-trained model used for fine-tuning with the custom dataset. It provides a strong baseline for image classification.
MobileNet: A lightweight model optimized for mobile devices, ensuring faster inference without sacrificing accuracy.
Model Accuracy
The models have been fine-tuned on a custom dataset, achieving high accuracy on common crop diseases. However, the accuracy may vary with the quality and diversity of the input images.

### Running Tests
Python Tests: To run the Python tests, navigate to the project directory and run: python -m unittest discover tests

## Tech Stack
- **Libraries & Software:** Jumpy, Matplotlib, TensorFlow, Keras, Flask Framework, Anaconda Prompt, Google Cloud Platform.
- **Programming Languages:** Python 3.7, HTML, JavaScript.
- **Models:** VGG16, MobileNet.
- **Framework:** Flask.

## Future Improvements
- **Model Enhancement:** Continuously improve the model’s accuracy by incorporating more diverse data.
- **Multilingual Support:** Expand language support beyond Marathi to other regional languages.
- **Mobile Application:** Develop a mobile version of the application for easier accessibility.
- **Real-time Updates:** Integrate a system to provide real-time updates on new diseases and treatment methods.

## How to Use
1. Clone the repository to your local machine.
2. Set up a virtual environment and install the required libraries.
3. Run the Flask application and navigate to the provided local URL.
4. Upload an image of a crop, and the application will display the disease and a possible cure.
