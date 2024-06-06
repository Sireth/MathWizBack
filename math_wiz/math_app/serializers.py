from rest_framework import serializers


class VariableSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=['string', 'integer', 'boolean'])
    value = serializers.JSONField()

    def validate(self, data):
        var_type = data.get('type')
        value = data.get('value')

        if var_type == 'string' and not isinstance(value, str):
            raise serializers.ValidationError({'value_error': "Value must be a string."})
        elif var_type == 'integer' and not isinstance(value, int):
            raise serializers.ValidationError({'value_error': "Value must be an integer."})
        elif var_type == 'boolean' and not isinstance(value, bool):
            raise serializers.ValidationError({'value_error': "Value must be a boolean."})
        return data


class EvaluationSerializer(serializers.Serializer):
    variables = serializers.ListField(child=VariableSerializer(), required=False)
    expression = serializers.CharField(max_length=200)
