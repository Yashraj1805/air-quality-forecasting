# Air Quality Forecasting API

A Flask API for predicting Air Quality Index (AQI) based on air pollutant measurements.

## GitHub and Railway Deployment

### Prerequisites
- A [GitHub](https://github.com) account
- A [Railway.app](https://railway.app) account

### Deployment Steps

1. Create a new GitHub repository:
   - Go to https://github.com/new
   - Name your repository (e.g., "air-quality-forecasting")
   - Don't initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

2. Push your local repository to GitHub:
   ```
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```
   Replace YOUR_USERNAME and YOUR_REPO_NAME with your GitHub information.

3. Deploy from GitHub to Railway:
   - Go to https://railway.app/ and sign in
   - Click "New Project" 
   - Select "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect your Procfile and deploy your app
   - After deployment, you can find your API URL in the project settings

## API Endpoints

- GET `/get`: Check if the model is running
- POST `/predict`: Predict AQI based on air pollutant values

Example request to `/predict`:
```json
{
  "PM2.5": 35.0,
  "PM10": 70.0,
  "NO2": 80.0,
  "CO": 1.2,
  "SO2": 40.0,
  "O3": 50.0
}
```

Example response:
```json
{
  "AQI": 125.5
}
```

## Testing the Deployed API

Once deployed, test your API with:

```
curl -X GET https://your-railway-app-url.railway.app/get
```

For predictions:
```
curl -X POST -H "Content-Type: application/json" -d '{"PM2.5": 35.0, "PM10": 70.0, "NO2": 80.0, "CO": 1.2, "SO2": 40.0, "O3": 50.0}' https://your-railway-app-url.railway.app/predict
```

## CORS Configuration

The API is now configured to accept requests from specific origins. If you want to restrict it to specific origins later, you can modify the CORS configuration like this:

```python
from flask_cors import CORS

CORS(app, origins=['https://your-frontend-domain.com'])
``` 