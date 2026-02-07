import torch
from model import CNNMNIST
from preprocessing import get_preprocessing_pipeline


def load_model(model_path="models/cnn_mnist.pth"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CNNMNIST().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model, device


def predict(image):
    model, device = load_model()
    transform = get_preprocessing_pipeline()

    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        prediction = torch.argmax(output, dim=1).item()

    return prediction