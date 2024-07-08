from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    display_name = serializers.CharField(max_length=100)
    profile_image = serializers.URLField()
    object_detected = serializers.BooleanField()
    bounding_boxes = serializers.ListField(
        child=serializers.DictField(), required=False
    )
    detection_time_ms = serializers.FloatField()
