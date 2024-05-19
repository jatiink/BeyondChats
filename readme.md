# API Response Citation Finder

This project is a Streamlit application that fetches data from an API and extracts citations from responses. It allows users to navigate through different responses and view the corresponding citations.

## Features

- Fetch data from a paginated API endpoint
- Handle API rate limits with exponential backoff
- Extract and display citations from responses
- User-friendly interface with Streamlit


## Setup

1. **Install Dependencies**

    Install the required packages using pip.

    ```
    pip install streamlit request
    ```

## Running the Application

Run the Streamlit application using the following command:

```
streamlit run app.py
```