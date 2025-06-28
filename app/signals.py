from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import Team
from app.serializers import TeamModelSerializer


@receiver(post_save, sender=Team)
def team_change(sender,instance, **kwargs):
    channel_layer = get_channel_layer()

    team_board =  Team.objects.filter(league=instance.league)
    print(team_board)
    serializer = TeamModelSerializer(team_board, many=True)
    async_to_sync(channel_layer.group_send)(
        f"league_{instance.league.pk}",
        {
            "type": "team_update",
            "data": serializer.data
        }
    )


