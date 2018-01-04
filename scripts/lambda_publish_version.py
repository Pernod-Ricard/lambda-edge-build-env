from __future__ import print_function
import sys
import boto3
import argparse
from botocore.exceptions import ClientError

def publish_new_version(artifact, function):
    """
    Publishes new version of the AWS Lambda Function
    """
    try:
        client = boto3.client('lambda')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False

    try:
        response = client.update_function_code(
            FunctionName=function,
            ZipFile=open(artifact, 'rb').read(),
            Publish=True
        )
        return response
    except ClientError as err:
        print("Failed to update function code.\n" + str(err))
        return False
    except IOError as err:
        print("Failed to access " + artifact + ".\n" + str(err))
        return False

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", help="Name of the existing lambda artifact")
    parser.add_argument("function", help="Name of the lambda function to publish a new version")
    args = parser.parse_args()

    if not publish_new_version(args.artifact, args.function):
        sys.exit(1)

if __name__ == "__main__":
    main()
