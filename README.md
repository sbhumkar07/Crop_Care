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

## Implementation
### Steps Involved:
1. **Dataset Creation:** A custom dataset was developed by collecting images of various crops from agricultural sources.
2. **Model Training:** The image classification model was trained using VGG16 and MobileNet architectures, taking advantage of Transfer Learning to achieve high accuracy with a relatively small dataset.
3. **Web Application Development:** The front-end was created using HTML, CSS, and JavaScript. Flask was used for setting up routing and integrating the MobileNet model into the application.
4. **Deployment:** The application was deployed using Google Cloud Platform, ensuring scalability and reliability.

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
