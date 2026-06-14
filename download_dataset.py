import kagglehub

path = kagglehub.dataset_download(
    "emmarex/plantdisease"
)

print("Dataset downloaded to:")
print(path)