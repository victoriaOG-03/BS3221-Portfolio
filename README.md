# BS3221 Summative Assignment

## Development environment instructions:

### Setting up the development environment:

Before running the application, make sure you have the necessary dependencies installed on your device. Follow these steps:

1. Open your terminal and navigate to the `Waqq.ly` folder.

2. Install pip if you haven't already by running the following command:
    ```
    pip install --upgrade pip
    ```

3. Install the required dependencies using the provided `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```

### Running the application:

Once you've set up the development environment, you can run the Flask application locally. Follow these steps:

1. Ensure you're in the `Waqq.ly` folder in your terminal.

2. Activate the virtual environment (if you're using one):
    ```
    source venv/bin/activate
    ```

3. Run the Flask application:
    ```
    flask run or python app.py
    ```
    
4. Click on the link in your terminal:
   ```
   after doing the instruction above you should be promted with the info below:

   file path % flask run
   Debug mode: off
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   Running on http://127.0.0.1:5000
   Press CTRL+C to quit

   the http link above is the link you should see if the system has successfully been placed on your device.
   ```

### Deployment instructions via azure portal:

To deploy the application through the Azure cloud portal, follow these steps:

1. Copy the following link: `https://waqqly-dogs.azurewebsites.net/`.

2. Open your web browser and paste the link into the address bar.

3. Press Enter to access the deployed application.

4. You should be able to see the website and have access to all the pages that are present.
