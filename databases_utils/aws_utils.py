__version__='1.1.0'
__author__=['Ioannis Tsakmakis']
__date_created__='2024-09-28'
__last_updated__='2024-10-09'

import boto3, base64, json
from botocore.exceptions import ClientError
from typing import Union
# from logger import aws_utils
from .logger import aws_utils

class SecretsManager:
    def __init__(self, region_name='eu-west-1'):
        self.client = boto3.client('secretsmanager', region_name=region_name)

    def store_secret(self, secret_name: str, secret_value: Union[str,dict]):
        '''
        Saves a key - value pair of a secret name and a secret value to AWS Secrets Manager

        :param secret_name: A name that will used to retrieve the secret value
        :param secret_value: The dict or string that contains the actual sensitive data to be stored
        '''

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
        '''
        Updates a secret value for a given secret name to AWS Secrets Manager

        :param secret_name: The key of the secret value
        :param secret_value: The dict or string that contains the actual sensitive data to be persisted
        '''

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
        '''
        Returns a secret from AWS Secret Manager

        :param secret_name: Name of the secret to be retrieved.
        
        '''
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
        
    def delete_secret_in_secrets_manager(self, secret_name: str, recovery_window_in_days: int = 7, force_delete: bool = False):
        """
        Deletes a secret from AWS Secrets Manager.
        
        :param secret_name: Name of the secret to delete.
        :param recovery_window_in_days: Number of days to recover the secret before permanent deletion.
                                        Defaults to 30 days.
        :param force_delete: If set to True, the secret is deleted immediately without a recovery window.
        """
        try:
            if force_delete:
                # Permanently delete the secret immediately
                response = self.client.delete_secret(
                    SecretId=secret_name,
                    ForceDeleteWithoutRecovery=True
                )
                aws_utils.info(f"Secret {secret_name} permanently deleted.")
            else:
                # Soft-delete with recovery window
                response = self.client.delete_secret(
                    SecretId=secret_name,
                    RecoveryWindowInDays=recovery_window_in_days
                )
                aws_utils.info(f"Secret {secret_name} scheduled for deletion. It can be recovered within {recovery_window_in_days} days.")
            return response
        except ClientError as e:
            aws_utils.error(f"Error deleting secret: {e}")
            raise

class KeyManagementService():
    def __init__(self):
        self.kms_client = boto3.client('kms')

    def create_new_key(self):
        '''
        Creates a new key for encryption - decryption in the AWS Key Management Service
        and returns its id 
        '''
        # Create a KMS key
        try:
            response = self.kms_client.create_key(
                Description='My encryption key for sensitive data',
                KeyUsage='ENCRYPT_DECRYPT',  # Key is used for both encryption and decryption
                Origin='AWS_KMS'  # Specifies that AWS manages the key
            )
            aws_utils.info('Key created successfully')
            return response['KeyMetadata']['KeyId']
        
        except ClientError as e:
            aws_utils.error(f'Failed to create a key - {e}')
            return {'message': 'Failed to create a key', 'errors':[e]}

    def encrypt_data(self, unencrypted_text: str, key_id: str) -> str:
        '''
        Encrypts a string using a key from the AWS Key Management Service

        :param unencrypted_text: The string that will be encrypted
        :param key_id: The id of the key that will be used for the encryption
        '''

        # Encrypt the data using the KMS key
        try:
            encrypt_response = self.kms_client.encrypt(
                KeyId=key_id,  # Use the Key ID from the previous step
                Plaintext=unencrypted_text.encode('utf-8')
            )
            # Get the encrypted ciphertext (base64-encoded for easier storage/transmission)
            ciphertext = base64.b64encode(encrypt_response['CiphertextBlob']).decode('utf-8')
            aws_utils.info('Text encrypted successfully')
            return ciphertext
        
        except UnicodeEncodeError as e:
            aws_utils.error('Envryption failed - {e}')
            return {'message':'Encryption failed', 'errors':[{e}]}
    
    def decrypt_data(self, encrypted_text: str):
        '''
        Decrytps a string that was encrypted using a key from the AWS Key Management Service

        :param encrypted_text: The string that will be decrypted
        '''

        # Decode the base64-encoded ciphertext back to its original binary format
        try:
            ciphertext_blob = base64.b64decode(encrypted_text)

            # Decrypt the ciphertext
            decrypt_response = self.kms_client.decrypt(
                CiphertextBlob=ciphertext_blob
            )
            aws_utils.info('Decrypton completed successfully')
            # Extract the decrypted plaintext
            return decrypt_response['Plaintext'].decode('utf-8')
        except UnboundLocalError as e:
            aws_utils.error('Decrytpion failed - {e}')
            return {'message': 'Decrytpion failed','errors':[e]}
    
    def list_kms_keys(self):
        keys = []
        paginator = self.kms_client.get_paginator('list_keys')
        for page in paginator.paginate():
            keys.extend(page['Keys'])
        
        return keys