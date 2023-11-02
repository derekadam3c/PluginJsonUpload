import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def az_storage_setup(container_name="data", local_file_path = "C:\\Users\\DerekAdam\\Documents\\dadamAz\\az-py-blob-test\\requirements.txt", blob_name = "uploaded-file.txt"):
    """ Takes container_name, local_file_path, blob_name and uploads file to Azure Blob Storage"""
    # Azure Blob Storage connection string
    try:
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        
    except AttributeError:
        exit

    blob_name, extension = blob_name.split(".")
    blob_name += "_" + str(uuid.uuid4()) + "." + extension

    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # Get the container client
    container_client = blob_service_client.get_container_client(container_name)

        # Upload the file
    with open(local_file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
        filename = local_file_path.split("\\")[-1]
        print("{0} uploaded successfully to {1}!".format(filename, blob_name))

    return (filename, blob_name)

def main():
    print("Running func az_storage_setup")
    az_storage_setup()

if __name__ == "__main__":
    main()