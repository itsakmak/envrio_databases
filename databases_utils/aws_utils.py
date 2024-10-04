__version__='1.0.1'
__author__=['Ioannis Tsakmakis']
__date_created__='2024-09-28'
__last_updated__='2024-10-02'

import boto3, base64, json
from botocore.exceptions import ClientError
from typing import Union
from .logger import aws_utils

'''AWS Secrets Manager'''
class SecretsManager:
    def __init__(self, region_name='eu-west-1'):
        self.client = boto3.client('secretsmanager', region_name=region_name)

    def store_secret(self, secret_name: str, secret_value: Union[str,dict]) -> dict:
        if isinstance(secret_value, dict):
            secret_value = json.dumps(secret_value)
        try:
            # Store a new secret
            response = self.client.create_secret(
                Name=secret_name,
                SecretString=secret_value
            )
            aws_utils.info(f"\nSecret stored successfully: {response['ARN']}\n")
            return {"message":f"Secret stored successfully: {response['ARN']}"}
        except ClientError as e:
            aws_utils.error(f"\nError storing secret: {e}\n")
            return {"message":f"Error storing secret: {e}"}
        
    def update_secret(self, secret_name: str, secret_value: Union[str,dict]) -> dict:
        if isinstance(secret_value, dict):
            secret_value = json.dumps(secret_value)
        try:
            # Store a new secret
            response = self.client.update_secret(
                SecretId=secret_name,
                SecretString=secret_value
            )
            aws_utils.info(f"\nSecret updated successfully: {response['ARN']}\n")
            return {"message":f"Secret updated successfully: {response['ARN']}"}
        except ClientError as e:
            aws_utils.error(f"\nError updating secret: {e}\n")
            return {"message":f"Error updating secret: {e}"}
    
    def get_secret(self, secret_name: str) -> Union[str,dict]:
        try:
            # Fetch the secret from Secrets Manager
            get_secret_value_response = self.client.get_secret_value(SecretId=secret_name)

            # Decrypts secret using the associated KMS key
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                try:
                    secret = json.loads(secret)
                except TypeError:
                    secret = secret
            else:
                # Handle binary secrets if necessary
                secret = get_secret_value_response['SecretBinary']

            return secret

        except ClientError as e:
            # Handle any exceptions here
            aws_utils.error(f"\nError retrieving secret: {e}\n")
            return None

'''Amazon Key Management Service utilities'''
class KeyManagementService():
    def __init__(self):
        self.kms_client = boto3.client('kms')
        self.sm = SecretsManager()

    def create_new_key(self, key_secret_name: str):
        # Create a KMS key
        response = self.kms_client.create_key(
            Description='My encryption key for sensitive data',
            KeyUsage='ENCRYPT_DECRYPT',  # Key is used for both encryption and decryption
            Origin='AWS_KMS'  # Specifies that AWS manages the key
        )

        # Extract the key ID
        key_id = {
            "key_id":response['KeyMetadata']['KeyId']
            }
        
        self.sm.store_secret(secret_name=key_secret_name, secret_value=key_id['key_id'])

        aws_utils.info(f"The key saved successfully in SecretsManager")

    def encrypt_data(self, unencrypted_text: str, key_secret_name: str) -> str:
        
        # Read the key_id
        key_id = self.sm.get_secret(secret_name=key_secret_name)

        # Encrypt the data using the KMS key
        encrypt_response = self.kms_client.encrypt(
            KeyId=key_id,  # Use the Key ID from the previous step
            Plaintext=unencrypted_text.encode('utf-8')
        )

        # Get the encrypted ciphertext (base64-encoded for easier storage/transmission)
        return base64.b64encode(encrypt_response['CiphertextBlob']).decode('utf-8')
    
    def decrypt_data(self, encrypted_text: str):
        
        # Decode the base64-encoded ciphertext back to its original binary format
        ciphertext_blob = base64.b64decode(encrypted_text)

        # Decrypt the ciphertext
        decrypt_response = self.kms_client.decrypt(
            CiphertextBlob=ciphertext_blob
        )

        # Extract the decrypted plaintext
        return decrypt_response['Plaintext'].decode('utf-8')

