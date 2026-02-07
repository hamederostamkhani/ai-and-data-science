import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets

from model import CNNMNIST
from preprocessing import get_preprocessing_pipeline


def train():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform = get_preprocessing_pipeline()

    train_dataset = datasets.MNIST(
        root="data",
        train=True,
        download=True, # If you have the training dataset, you should change this to 'False'
        transform=transform
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=64,
        shuffle=True
    )

    model = CNNMNIST().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    num_epochs = 5

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch [{epoch+1}/{num_epochs}], "
              f"Loss: {running_loss / len(train_loader):.4f}")

    torch.save(model.state_dict(), "models/cnn_mnist.pth")
    print("Model saved to models/cnn_mnist.pth")


if __name__ == "__main__":
    train()