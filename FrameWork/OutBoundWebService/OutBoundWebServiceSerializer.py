from rest_framework import serializers
from FrameWork.OutBoundWebService.models import BC_FW_CONFIG_VAR_B

class OutBoundWebServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model = BC_FW_CONFIG_VAR_B
		fields = '__all__'
		depth = 1

	def getValue(self,category):
		return BC_FW_CONFIG_VAR_B.objects.all().filter(category = category)

	def getValue(self,prop_id,category):
		return BC_FW_CONFIG_VAR_B.objects.all().filter(category = category,prop_id = prop_id)[0]
