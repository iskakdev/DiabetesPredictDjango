from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import DiabetesSerializers
import joblib
import os
from django.conf import settings

scaler_path = os.path.join(settings.BASE_DIR, 'diabetes_scaler.pkl')
model_path = os.path.join(settings.BASE_DIR, 'diabetes_log_model.pkl')

scaler = joblib.load(scaler_path)
model = joblib.load(model_path)

class DiabetesPredict(views.APIView):
    def post(self, request):
        serializer = DiabetesSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = [data['Pregnancies'], data['Glucose'], data['BloodPressure'], data['SkinThickness'],
                        data['Insulin'], data['BMI'], data['DiabetesPedigreeFunction'], data['Age']]
            scaled_data = scaler.transform([features])
            proba = model.predict_proba(scaled_data)[0]
            probability = float(proba[1])
            if probability > 0.5:
                diabetes_label = 'Yes'
            else:
                diabetes_label = 'No'
            return Response({'Diabetes': diabetes_label, 'Probability': round(probability, 2)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
