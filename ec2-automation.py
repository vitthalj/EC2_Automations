import boto3
import sys
import time
from botocore.exceptions import ClientError

region = 'ap-south-1'

print('The region is: ',region)
action = (input('Please enter action START or STOP: ')).upper()
instance_Id = "i-134134n1egdgg" 
device = '/dev/sda1'
volume_id = "vol-svuj345134n1egdgg"


ec2 = boto3.client('ec2',region_name=region)

def start_instance():

    try:
        response = ec2.start_instances(InstanceIds = [instance_Id])
        print(response)
        print('instance is started',instance_Id)
    except ClientError as e:
        print(e)
    return 


def stop_instance():
    
    
    try:
        response = ec2.stop_instances(InstanceIds = [instance_Id])
        print(response)
        print('instance is stopped',instance_Id)
    except ClientError as e:
        print(e)
    return 

def attach_volume():
  try:
        response= ec2.attach_volume( Device = device, InstanceId = instance_Id, VolumeId = volume_id ) 
        print('attached volume to instance ', instance_Id)
  except ClientError as e:
          print(e) 
  return        

def detach_volume():
  try:
        response= ec2.detach_volume( Device = device, InstanceId = instance_Id, VolumeId = volume_id ) 
        print('detached volume from instance ', instance_Id)
  except ClientError as e:
          print(e) 
  return 

if action == 'START':
    attach_volume()
    time.sleep(30)
    start_instance()

elif action == 'STOP':
    stop_instance()
    time.sleep(30)
    detach_volume()    
