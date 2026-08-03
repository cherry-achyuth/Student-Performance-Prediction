# Deploy to Render

This repository is configured for a Docker-based Render web service. The trained
model files in `artifacts/` are included in the image.

1. Create a new GitHub repository and upload the contents of this folder (not
   the enclosing `Student-Performance-Prediction-main` folder itself).
2. In Render, select **New > Web Service**, connect GitHub, and select the
   repository.
3. Set **Language** to **Docker**. Keep the Dockerfile path as `./Dockerfile`.
4. Choose a unique service name and click **Deploy Web Service**.
5. Once the build completes, open the generated `onrender.com` URL and select
   **Predict Student Performance**.

Render uses the `CMD` in the Dockerfile, which starts the application with
Gunicorn and listens on Render's assigned `PORT`. No environment variables are
required for this project.

For deployment from the `render.yaml` file instead, choose **New > Blueprint**
and select the same repository.
