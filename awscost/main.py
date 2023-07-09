import boto3
from botocore.exceptions import BotoCoreError, ClientError


def get_costs():
    client = boto3.client('ce', region_name='us-east-1')

    try:
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': '2023-06-01',
                'End': '2023-06-30'
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[
                {
                    'Type': 'DIMENSION',
                    'Key': 'SERVICE'
                },
            ]
        )
    except (BotoCoreError, ClientError) as error:
        print(f'An error occurred: {error}')
        return None

    response_model = CostExplorerResponse(**response)

    cost_dict = {}
    for result in response_model.ResultsByTime:
        for group in result.Groups:
            cost = group.Metrics.UnblendedCost['Amount']
            service = group.Keys[0]
            cost_dict[service] = cost

    return cost_dict
