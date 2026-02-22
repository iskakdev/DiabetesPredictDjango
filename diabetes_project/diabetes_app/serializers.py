from rest_framework import serializers

class DiabetesSerializers(serializers.Serializer):
    Pregnancies = serializers.IntegerField()
    Glucose = serializers.IntegerField()
    BloodPressure = serializers.IntegerField()
    SkinThickness = serializers.IntegerField()
    Insulin = serializers.IntegerField()
    BMI = serializers.FloatField()
    DiabetesPedigreeFunction = serializers.FloatField()
    Age = serializers.IntegerField()
